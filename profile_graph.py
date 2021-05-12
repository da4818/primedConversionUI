import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("pre_pr_red1.png")
#img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
colour_mask = cv2.imread("pre_pr_red1.png")
width=img.shape[0]


#automating profile variables
start_x=0
end_x=width
y=200
#creates array to determine area of image that is to be masked
mask = np.zeros(img.shape[:2], np.uint8)
#the chosen masking area is a 1px thick line from x=100 to x=400
mask[y:y+1, start_x:end_x] = 255
#creates matrix of brightness for chosen pixels (forms a 3 column matrix - the first 2 column are irrelevant)
pixel_brightnesses = img[y,start_x:end_x]
#creates vector of the pixel location selection (e.g., x coord 1,2,3....)
pixel_locations = np.arange(start_x,end_x)

#this masks off everything outside of the masking range (plot 3)
# -->sets everything else to black (since it's 1px thick it's hard to see)
masked_img = cv2.bitwise_and(img,img, mask = mask)
colour_mask[y:y+1, start_x:end_x] = (255,255,255)

#original image - not too sure why the image displays as blue
plt.subplot(221), plt.imshow(img)
#original image with profile section highlighted in white
plt.subplot(222), plt.imshow(colour_mask)
#masked image
'''plt.subplot(223), plt.imshow(masked_img)
#4th plot is the brightness profile'''
plt.subplot(224), plt.plot(pixel_brightnesses[:,2])
#as the columns 0 and 1 are irrelevant, we want to only take information for column 2
plt.xlim([0,width])

plt.show()


