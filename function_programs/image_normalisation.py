import PIL
import cv2
from PIL import Image
import numpy as np

# We will use this python script to perform image normalisation and return the image to other functions
def normalise_image(pre, post):
    '''if state == 'red':
        path = '/Users/debbie/python/GroupProject/raw_images/red' #The image should save to the correct location from the rasp pi camera
    elif state == 'green':
        path = '/Users/debbie/python/GroupProject/raw_images/green/'''

    #post = PIL.Image.open(path+"postpc1.png")
    ##post.show(title="New")
    pre = pre.convert("RGB")
    norm = post.convert("RGB")
    width, height = post.size

    #pre = PIL.Image.open(path+"prepc1.png")

    #pre.show(title="Original")
    ##show_color(R,G,B)
    ##print("Normalisation RGB value:",R,G,B)
    ##print(rgb_val)
    for x in range(width):
        for y in range(height):
            old_R,old_G,old_B = norm.getpixel((x,y))
            R,G,B = pre.getpixel((x,y))
            norm.putpixel((x,y),(old_R-R,old_B-B,old_G-G))
    #norm.show(title="Normalised")
    #cvImage=cv2.cvtColor(np.array(norm), cv2.COLOR_BGR2RGB)
    return norm
    #cv2.imwrite('normalised.png',cvImage)

if __name__ == "__main__":
    normalise_image("green")
