#from picamera import PiCamera
import PIL
from PIL import Image
from function_programs.files import *
from function_programs.image_normalisation import *
from function_programs.raspigpio import raspi_turnon, raspi_turnoff
'''
Raspberry pi ribbon should have blue side facing towards ethernet port
'''
#Note - do not call this file picamera.py as this will cause errors

''' CAMERA CLASS FUNCTIONALITY:
- takes and saves 2 raw photos in the correct directory: 1) pre conversion and 2) post conversion
- saves analysed photos in the correct directory: 3) normalised 
- returns images 1) and 4) to display to tkinter
'''

'''UPDATE: the green and red channel imagesshould have the same ID number (and the analysis page will display 2 graphs)
 1) The fluorescence ability (green channel)
 2) The primed/photo convertible ability (red channel)'''
class Camera:
    #def __init__(self, files_class, gpio_class):
    def __init__(self, files_class):
        self.files = files_class
        #self.gpio = gpio_class
        self.state = ""
        self.pre_path = ""
        self.post_path = ""
        self.norm_path = ""
        #self.camera = PiCamera() #initiatilse camera

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
            self.files.curr_filename = filename
            self.files.curr_filepath = self.pre_path
            print(filename, "saved")

        if state == "post":
            if self.files.excitation == "green_excitation":
                img1 = Image.open("green_test_after.png")
            elif self.files.excitation == "red_excitation":
                img1 = Image.open("red_test_after.png")
            filename = self.files.get_file_name("post")
            self.post_path = os.path.join(self.files.get_raw_path(), filename)
            img1.save(self.post_path)
            self.files.curr_filename = filename
            self.files.curr_filepath = self.post_path
            print(filename, "saved")

    def check_recent_photos(self):
        raw = self.files.get_raw_path()
        #Generate file names, corresponding ID number and method (pc or pr)
        raw_files_list, numbers, methods = self.files.get_raw_images()
        if (not raw_files_list) or self.files.curr_file_ID == 0:
            print("No previously saved photos")
        else:
            pre, post = self.get_file_name()
            print("Looking for", pre, "and", post)
            p1 = os.path.join(raw, pre)
            p2 = os.path.join(raw, post)
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
        norm.save(norm_path)
        print(norm_name, "saved")
        self.norm_path = norm_path
        self.files.curr_filename = norm_name
        self.files.curr_filepath = norm_path

    def get_file_name(self):
        pre_filename = "pre_"+str(self.files.method)+"_"+str(self.files.colour)+"_"+str(self.files.curr_file_ID)+".png"
        post_filename = "post_"+str(self.files.method)+"_"+str(self.files.colour)+"_"+str(self.files.curr_file_ID)+".png"
        return pre_filename, post_filename


'''if __name__ == "__main__":
    f = Files("green_excitation", "pc")
    c = Camera(f)
    c.check_recent_photos()
    #c.take_photo("post")'''


'''from picamera import PiCamera
from datetime import datetime

class Camera:
    def __init__(self):
        self.camera = PiCamera()
        print("Camera connected")

    def capture(self, ID):
        timestamp = datetime.now().isoformat()
        filename = "file" + str(ID) +".jpg"
        self.camera.capture('/home/pi/'+filename)
        print(filename+ " captured at", timestamp)
        self.camera.close()'''