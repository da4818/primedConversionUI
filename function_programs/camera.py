#from picamera import PiCamera
from PIL import Image
from function_programs.files import *
from function_programs.image_normalisation import *
from function_programs.image_analysis import *
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
    def __init__(self, files_class):
        self.files = files_class
        self.filename = ""
        self.state = ""
        self.pre_path = ""
        self.post_path = ""
        print("Preparing images for", f.excitation, "excitation...")
        #camera = PiCamera() #initiatilse camera

    def take_photo(self, state):
        names = self.files.get_file_names()
        self.state = state
        #placeholder whilst picamera isn't connected
        img = Image.new(mode = "RGB", size = (50, 50),color = (153, 153, 255))
        img1 = Image.new(mode = "RGB", size = (50, 50),color = (255, 153, 255)) #post will undergo normalisation

        if state == "pre":
            self.filename = names[0]
            self.pre_path = os.path.join(self.files.get_raw_path(f.excitation), self.filename)
            img.save(self.pre_path)
            print(names[0], "saved")
        elif state == "post":
            self.filename = names[1]
            self.post_path = os.path.join(self.files.get_raw_path(f.excitation), self.filename)
            print(names[1], "saved")
            img1.save(self.post_path)
            self.save_analysed_photos()


        '''
        camera.vflip = True #Sometimes the image is flipped upside down
        #camera.capture(filename)
        #camera.startrecord
        camera.start_preview(alpha=200) #alpha give transparency to the image to detect errors
        sleep(5)
        camera.stop_preview()'''
        
    def save_analysed_photos(self):
        #Create and save normalised image
        pre = PIL.Image.open(self.pre_path)
        post = PIL.Image.open(self.post_path)
        norm = normalise_image(pre, post)
        norm_directory = f.get_analysis_path(f.excitation)
        norm_name = f.names[2] #generate_file_ID() gives 1x4 vector of files names: index 2 holds normalised image filename
        norm_path = os.path.join(norm_directory, norm_name)
        print("normalised image: ",norm_path)
        norm.save(norm_path)

        #Create and save masked image
        masked = Image.fromarray(masked_image(norm_path))
        masked_path = os.path.join(norm_directory, f.names[3])
        print("masked image:", masked_path)
        masked.save(masked_path)


if __name__ == "__main__":
    f = files("green", "pc")
    c = camera(f)
    c.take_photo("pre")
    c.take_photo("post")
