import PIL
import cv2
from PIL import Image
import numpy as np

# We will use this python script to perform the image analysis and display the results

#FUNCTIONALISED
def normalise_image(state):
    if state == 'red':
        path = '/Users/debbie/python/GroupProject/raw_images/red'
    elif state == 'green':
        path = '/Users/debbie/python/GroupProject/raw_images/green/'

    post = PIL.Image.open(path+"postpc.png")
    #post.show(title="New")
    norm = post.convert("RGB")
    width, height = post.size

    pre = PIL.Image.open(path+"prepc.png")
    pre = pre.convert("RGB")
    #pre.show(title="Original")
    #print(pre.size)
    ##show_color(R,G,B)
    #print("size:",width,",",height)
    ##print("Normalisation RGB value:",R,G,B)
    ##print(rgb_val)
    for x in range(width):
        for y in range(height):
            old_R,old_G,old_B = norm.getpixel((x,y))
            R,G,B = pre.getpixel((x,y))
            norm.putpixel((x,y),(old_R-R,old_B-B,old_G-G))
    #norm.show(title="Normalised")
    #cvImage=cv2.cvtColor(np.array(norm), cv2.COLOR_BGR2RGB)
    return pre, post, norm
#cv2.imwrite('normalised.png',cvImage)

if __name__ == "__main__":
    normalise_image("green")



'''post = PIL.Image.open("test4.tif")
norm = post.convert("RGB")
width, height = post.size
#rgb_val = norm.getpixel((1,1))
R0,G0,B0 = norm.getpixel((0,0))
print("size:",width,",",height)
print("Values:",R0,G0,B0)
#print(rgb_val)
for x in range(width):
    for y in range(height):
        R,G,B = norm.getpixel((x,y))
        new_R,new_G,new_B = (R-R0)*50,(B-B0)*50,(G-G0)*50 # Multiplying by 50 amplifies the difference in brightness
        #print(D,E,F)
        #R1,G1,B1 = norm.getpixel((x,y))
        #R1, G1, B1 = norm.getpixel((x,y))
        norm.putpixel((x,y),(new_R,new_G,new_B))
#norm.save('example'+str(3  )+'.png')
#post.show()
norm.show()'''
