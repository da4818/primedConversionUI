#Using rasp pi camera
import os
import re
#from picamera import PiCamera
from time import sleep


def get_paths(state):

    if state == "red":
        path = '/Users/debbie/python/GroupProject/raw_images/red/'

    elif state == "green":
        path = '/Users/debbie/python/GroupProject/raw_images/green/'

    return path






def take_photo(state, num):
    path,num = get_paths(state, num)
    camera = PiCamera()
    camera.start_preview(alpha=200) #alpha give transparency to the image to detect errors
    sleep(5)
    filename=path+"pre"+str(num)+"png"
    camera.capture(filename)
    camera.stop_preview()

if __name__ == "__main__":
    print('test')