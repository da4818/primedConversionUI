import PIL
import cv2
from PIL import Image
import numpy as np

# We will use this python script to perform the image analysis and display the results


#FUNCTIONALISED
photo = PIL.Image.open("after.png")
photo.show(title="New")
photo_rgb = photo.convert("RGB")
width, height = photo.size

og=PIL.Image.open("before.png")
og = og.convert("RGB")
og.show(title="Original")
print(og.size)
#show_color(R,G,B)
print("size:",width,",",height)
#print("Normalisation RGB value:",R,G,B)
#print(rgb_val)
for x in range(width):
    for y in range(height):
        old_R,old_G,old_B = photo_rgb.getpixel((x,y))
        R,G,B = og.getpixel((x,y))
        photo_rgb.putpixel((x,y),(old_R-R,old_B-B,old_G-G))
photo_rgb.show(title="Normalised")
cvImage=cv2.cvtColor(np.array(photo_rgb), cv2.COLOR_BGR2RGB)
cv2.imwrite('normalised.png',cvImage)


'''photo = PIL.Image.open("test4.tif")
photo_rgb = photo.convert("RGB")
width, height = photo.size
#rgb_val = photo_rgb.getpixel((1,1))
R0,G0,B0 = photo_rgb.getpixel((0,0))
print("size:",width,",",height)
print("Values:",R0,G0,B0)
#print(rgb_val)
for x in range(width):
    for y in range(height):
        R,G,B = photo_rgb.getpixel((x,y))
        new_R,new_G,new_B = (R-R0)*50,(B-B0)*50,(G-G0)*50 # Multiplying by 50 amplifies the difference in brightness
        #print(D,E,F)
        #R1,G1,B1 = photo_rgb.getpixel((x,y))
        #R1, G1, B1 = photo_rgb.getpixel((x,y))
        photo_rgb.putpixel((x,y),(new_R,new_G,new_B))
#photo_rgb.save('example'+str(3  )+'.png')
#photo.show()
photo_rgb.show()'''
