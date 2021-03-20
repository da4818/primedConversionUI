from time import sleep
#from picamera import PiCamera
import PIL
from PIL import Image
from function_programs.files import *
from function_programs.image_normalisation import *
from function_programs.image_analysis import *
from function_programs.raspigpio import excitation_on, raspi_turnoff, set_filter

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
    def __init__(self, files_class, gpio_class):
        self.files = files_class
        self.gpio = gpio_class
        self.filename = ""
        self.state = ""
        self.pre_path = ""
        self.post_path = ""
        self.norm_path = ""
        self.masked_path = ""
        print("Camera on")

        #camera = PiCamera() #initiatilse camera
    """
    def excitation_photos(self, excitation):
        # changing files.excitation to force having both red and green photos taken
        # by calling function twice in take_photos, each time with diff excitation.
        # >>>> need to modify windows to not choose between green and red channel but just have an
        # 'image excitation channels' button instead
        self.files.excitation = excitation
        names = self.files.get_file_names()
        self.filename = names[0]
        # setting filter wheel to correct position through servo control
        set_filter(excitation, self.gpio.servo)
        # excitation light turns on
        excitation_on(self.files.excitation, self.gpio.excitation_leds)
        # camera.vflip = True #Sometimes the image is flipped upside down
        # image is taken and saved
        camera.capture(self.filename)
        camera.startrecord
        camera.start_preview(alpha=200) #alpha give transparency to the image to detect errors
        sleep(5)
        camera.stop_preview()
        # all leds turned off
        raspi_turnoff()
    """
    def take_photo(self, state):
        print("Preparing camera for", self.files.excitation, "channel...")
        names = self.files.get_file_names()
        self.state = state
        # self.excitation_photos(self, 'red_excitation')
        # self.excitation_photos(self, 'green_excitation')

        if state == "pre":
            #This is placeholder code to simulate taking an image - here it opens a previously saved image (actual code is in speech marks above)
            if self.files.excitation == "green_excitation":
                img = Image.open("test_images/green_test_before.png")
            elif self.files.excitation == "red_excitation":
                img = Image.open("test_images/red_test_before.png")

            self.filename = names[0]
            self.pre_path = os.path.join(self.files.get_raw_path(), self.filename)
            img.save(self.pre_path)
            print(names[0], "saved")


        if state == "post":
            if self.files.excitation == "green_excitation":
                img1 = Image.open("P1.png")
            elif self.files.excitation == "red_excitation":
                img1 = Image.open("P2.png")
            #img1 = Image.new(mode = "RGB", size = (50, 50), color = (255, 153, 255)) #post will undergo normalisation
            self.filename = names[1]
            self.post_path = os.path.join(self.files.get_raw_path(), self.filename)
            print(names[1], "saved")
            img1.save(self.post_path)
            self.save_analysed_photos()
        
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
        masked, _ = masked_image(norm_path)
        masked = Image.fromarray(masked)
        masked_path = os.path.join(norm_directory, self.files.names[3])
        print(self.files.names[3],"saved")
        masked.save(masked_path)
        self.norm_path = norm_path
        self.masked_path = masked_path
        
    def export_files(self):
        norm = skimage.io.imread(self.norm_path)
        mask = skimage.io.imread(self.masked_path)
        return norm, mask


'''if __name__ == "__main__":
    f = files("green_excitation", "pc")
    c = camera(f)
    c.take_photo("pre")'''
    #c.take_photo("post")
