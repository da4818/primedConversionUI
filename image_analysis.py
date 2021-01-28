import PIL
from PIL import Image
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
#from networkx.drawing.tests.test_pylab import plt
#from skimage import data

# We will use this python script to perform the image analysis and display the results



def send_message():
    return 'Example text'

photo = PIL.Image.open("test4.tif")
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
photo_rgb.show()
def get_file(i):
    out = 'example'+str(i)+'.png'
    #photo_rgb.save(photo_rgb.save('example'+str(1)+'.png'))
    return out

#example3.png is the edited file "pr-mEosFP new_pr-mEosFP_new_before_4_ch00.tif