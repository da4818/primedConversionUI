#from picamera import PiCamera
from time import sleep
from PIL import Image
from function_programs.files import *
from function_programs.image_normalisation import *
'''
Raspberry pi ribbon should have blue side facing towards ethernet port
'''
#Note - do not call this file picamera.py as this will cause errors

''' CODE FUNCTIONALITY:
- takes and saves 2 raw photos in the correct directory: 1) pre conversion and 2) post conversion
- saves 2 analysed photos in the correct directory: 3) normalised and 4) masked
- returns images 1) and 4) to display to tkinter
'''
class camera:
    def __init__(self, files):
        self.files = files
        self.filename = ""
        self.state = ""
        self.pre_directory = ""
        self.post_directory = ""
        #camera = PiCamera() #initiatilse camera

    def take_photo(self, state):
        names = self.files.get_file_names()
        self.state = state
        if state == "pre":
            filename = names[0]
            self.filename = filename
            self.pre_directory = os.path.join(self.files.curr_path, self.filename)
            print(filename, "saved")
        elif state == "post":
            filename = names[1]
            self.filename = filename
            self.post_directory = os.path.join(self.files.curr_path, self.filename)
            print(filename, "saved")
            self.save_analysed_photos()

        '''
        camera.vflip = True #Sometimes the image is flipped upside down
        #camera.capture(filename)
        #camera.startrecord
        camera.start_preview(alpha=200) #alpha give transparency to the image to detect errors
        sleep(5)
        camera.stop_preview()'''
    def save_analysed_photos(self):
        #First created analysed images
        #pre = PIL.Image.open(self.pre_directory)
        #post = PIL.Image.open(self.post_directory)

        print("full directory of post:", self.post_directory)

        #norm = normalise_image(pre, post)
        # save normalised image
        norm_path = f.get_analysis_path(f.excitation)
        print(norm_path)
        #norm.save()





if __name__ == "__main__":
    f = files("green", "pc")
    c = camera(f)
    c.take_photo("pre")
    c.take_photo("post")