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
class Camera:
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
            filename = self.files.get_file_name("pre")

            self.pre_path = os.path.join(self.files.get_raw_path(), filename)
            img.save(self.pre_path)
            print(filename, "saved")

        if state == "post":
            if self.files.excitation == "green_excitation":
                img1 = Image.open("green_test_after.png")
            elif self.files.excitation == "red_excitation":
                img1 = Image.open("red_test_after.png")
            filename = self.files.get_file_name("post")

            self.post_path = os.path.join(self.files.get_raw_path(), filename)
            img1.save(self.post_path)
            print(filename, "saved")


    def check_recent_photos(self):
        raw = self.files.get_raw_path()
        #analysis = self.files.get_analysis_path()
        raw_files_list, numbers, methods = self.files.get_raw_images()
        if (not raw_files_list) or self.files.curr_file_ID == 0:
            print("No previously saved photos")
        else:
            pre, post = self.get_file_name()
            print("Looking for", pre, "and", post)
            p1=os.path.join(raw,pre)
            p2=os.path.join(raw,post)
            print(os.path.isfile(p1))
            print(os.path.isfile(p2))
            if os.path.isfile(p1) and os.path.isfile(p2):
                self.pre_path = p1
                self.post_path = p2
                self.generate_analysed_photos()


    def generate_analysed_photos(self):
        #Create and save normalised image
        pre = PIL.Image.open(self.pre_path)
        post = PIL.Image.open(self.post_path)
        norm = normalise_image(pre, post)
        norm_directory = self.files.get_analysis_path()
        norm_name = self.files.get_file_name("norm")
        norm_path = os.path.join(norm_directory, norm_name)
        print(norm_name, "saved")
        norm.save(norm_path)
        #Create and save masked image
        masked = Image.fromarray(masked_image(norm_path))
        masked_name = self.files.get_file_name("masked")
        masked_path = os.path.join(norm_directory, masked_name)
        print(masked_name, "saved")
        masked.save(masked_path)
        self.norm_path = norm_path
        self.masked_path = masked_path

    def get_file_name(self):
        pre_filename = "pre_"+str(self.files.method)+"_"+str(self.files.excitation[:-11])+"_"+str(self.files.curr_file_ID)+".png"
        post_filename = "post_"+str(self.files.method)+"_"+str(self.files.excitation[:-11])+"_"+str(self.files.curr_file_ID)+".png"
        return pre_filename, post_filename

    def export_files(self):
        norm = skimage.io.imread(self.norm_path)
        mask = skimage.io.imread(self.masked_path)
        return norm, mask


'''if __name__ == "__main__":
    f = Files("green_excitation", "pc")
    c = Camera(f)
    c.check_recent_photos()
    #c.take_photo("post")'''
