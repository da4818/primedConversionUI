#from picamera import PiCamera
import PIL
from PIL import Image
from function_programs.files import *
from function_programs.image_normalisation import *
from function_programs.image_analysis import *
from function_programs.raspigpio import raspi_turnon, raspi_turnoff
'''
Raspberry pi ribbon should have blue side facing towards ethernet port
'''
#Note - do not call this file picamera.py as this will cause errors

''' CAMERA CLASS FUNCTIONALITY:
- takes and saves 2 raw photos in the correct directory: 1) pre conversion and 2) post conversion
- saves 2 analysed photos in the correct directory: 3) normalised and 4) masked
- returns images 1) and 4) to display to tkinter
'''
class camera:
    #def __init__(self, files_class, gpio_class):
    def __init__(self, files_class):
        self.files = files_class
        #self.gpio = gpio_class
        self.state = ""
        self.pre_path = ""
        self.post_path = ""
        self.norm_path = ""
        self.masked_path = ""

        #camera = PiCamera() #initiatilse camera

    def take_photo(self, state):
        print("Camera on")
        print("Preparing camera for", self.files.excitation, "channel...")
        self.state = state
        if state == "pre":
            if self.files.excitation == "green_excitation":
                img = Image.open("green_test_before.png")
            elif self.files.excitation == "red_excitation":
                img = Image.open("red_test_before.png")
            filename = self.generate_file_name("pre")

            self.pre_path = os.path.join(self.files.get_raw_path(), filename)
            img.save(self.pre_path)
            print(filename, "saved")

        if state == "post":
            if self.files.excitation == "green_excitation":
                img1 = Image.open("P1.png")
            elif self.files.excitation == "red_excitation":
                img1 = Image.open("P2.png")
            filename = self.generate_file_name("post")

            self.post_path = os.path.join(self.files.get_raw_path(), filename)
            print(filename, "saved")
            img1.save(self.post_path)
            #self.save_analysed_photos()
        
    def save_analysed_photos(self):
        #Create and save normalised image
        pre = PIL.Image.open(self.pre_path)
        post = PIL.Image.open(self.post_path)
        norm = normalise_image(pre, post)
        norm_directory = self.files.get_analysis_path()
        norm_name = self.files.names[2] #generate_file_ID() gives 1x4 vector of files names: index 2 holds normalised image filename
        norm_path = os.path.join(norm_directory, norm_name)
        print(norm_name, "saved")
        norm.save(norm_path)

        #Create and save masked image
        masked = Image.fromarray(masked_image(norm_path))
        masked_path = os.path.join(norm_directory, self.files.names[3])
        print(self.files.names[3], "saved")
        masked.save(masked_path)
        self.norm_path = norm_path
        self.masked_path = masked_path


    def get_photos(self):

        raw = self.files.get_raw_path()
        #analysis = self.files.get_analysis_path()
        raw_files_list, numbers, methods = self.files.get_raw_images()
        if (not raw_files_list):
            print("No previously save photos")
        else:
            pre, post = self.get_file_name()
            #print("Looking for", pre, "and", post)
            p1=os.path.join(raw,pre)
            p2=os.path.join(raw,post)

            print(os.path.isfile(p1))
            print(os.path.isfile(p2))







        '''if (os.path.isdir(pre_path) == False):
            print("Pre file doesn't exist")
        if (os.path.isdir(post_path) == False):
            print("Post file doesn't exist")
        if(os.path.isdir(pre_path) == True and os.path.isdir(post_path) == True):
            pre = PIL.Image.open(pre_path)
            post = PIL.Image.open(post_path)
            pre.show()
            post.show()
            norm = normalise_image(pre, post)
            norm_directory = self.files.get_analysis_path()
            norm_name = self.files.names[2] #generate_file_ID() gives 1x4 vector of files names: index 2 holds normalised image filename
            norm_path = os.path.join(norm_directory, norm_name)
            print(norm_name, "saved")
            norm.save(norm_path)

            #Create and save masked image
            masked = Image.fromarray(masked_image(norm_path))
            masked_path = os.path.join(norm_directory, self.files.names[3])
            print(self.files.names[3], "saved")
            masked.save(masked_path)
            self.norm_path = norm_path
            self.masked_path = masked_path'''


    def generate_file_name(self, state):
        if state == "pre":
            filename = "pre_"+str(self.files.method)+"_"+str(self.files.excitation)+str(self.files.curr_file_ID+1)+".png"
        elif state == "post":
            filename = "post_"+str(self.files.method)+"_"+str(self.files.excitation)+str(self.files.curr_file_ID)+".png"
        elif state == "norm":
            filename = "norm_"+str(self.files.method)+"_"+str(self.files.excitation)+str(self.files.curr_file_ID)+".png"
        elif state == "masked":
            filename = "masked_"+str(self.files.method)+"_"+str(self.files.excitation)+str(self.files.curr_file_ID)+".png"
        return filename

    def get_file_name(self):
        pre_filename = "pre_"+str(self.files.method)+"_"+str(self.files.excitation)+str(self.files.curr_file_ID)+".png"
        post_filename = "post_"+str(self.files.method)+"_"+str(self.files.excitation)+str(self.files.curr_file_ID)+".png"

        return pre_filename, post_filename


    def export_files(self):
        norm = skimage.io.imread(self.norm_path)
        mask = skimage.io.imread(self.masked_path)
        return norm, mask


'''if __name__ == "__main__":
    f = files("green_excitation", "pc")
    c = camera(f)
    c.take_photo("pre")'''
    #c.take_photo("post")
