import numpy as np
import cv2
import skimage.color
import skimage.io
import skimage.viewer
from scipy.signal import find_peaks
import matplotlib.pyplot as plt
from function_programs.colour_conversion import hex_to_RGB

'''
Program that outputs a grayscale histogram of the image - an indicator for its brightness
Similar to those thermal camera, except it's for brightness
'''


# read the image as grayscale from the outset
file="tiles.png"
image = skimage.io.imread(file, as_gray=True)
original = cv2.imread(file)
gray = cv2.imread(file)
title=str(file)

#create a histogram of the greyscale image
histogram, bin_edges = np.histogram(image, bins=256, range=(0, 1))

#we can set a threshold of greyscale based on a standard greyscale value of a protein of known fluorescence
t_Values=np.linspace(0,1.0, num=5)
#this is a set of colour hex values as a high contrast visual representation of brightness
colours = ('#0000ff','#bb00ff','#ff00ff','#00ffff','#ffff00')


plt.figure()
#Finding the peaks will give us the numerical value of brightness, which can be used against a calibration curve later on to give fluorescence
peaks, _ = find_peaks(histogram,threshold=25, distance=20)#Plot the peaks onto the histogram (the threshold and distance value will need to be adjusted - this can be done on tkinter if needed)
plt.plot(bin_edges[0:-1], histogram)#Draw the histogram figure with corresponding peaks
plt.plot(bin_edges[peaks],histogram[peaks],"x")
for t,c in zip(t_Values,colours): #Draw threshold lines in their corresponding colours as will appear on the analysed in
    plt.axvline(x=t,color=c, label='line at x = {}'.format(t),)
plt.legend()
plt.title(title)
plt.xlabel("greyscale value")
plt.ylabel("pixels")
plt.xlim([0.0, 1.0])
plt.title(title)
plt.show()

masks = [] #We want to create a mask for each threshold value to allow us to 'colour in' the parts of the image that meet the threshold criteria
sigma=2 #blurring factor
blur = skimage.color.rgb2gray(image)# blur and grayscale before thresholding
blur = skimage.filters.gaussian(blur, sigma=sigma)
#perform binary thresholding for each threshold value
for t in t_Values:
    masks.append(blur > t)

gray[masks[0]] = hex_to_RGB(colours[0])
gray[masks[1]] = hex_to_RGB(colours[1])
gray[masks[2]] = hex_to_RGB(colours[2])
gray[masks[3]] = hex_to_RGB(colours[3])
gray[masks[4]] = hex_to_RGB(colours[4])
'''cv2.imshow('Original image', original)
cv2.imshow('Masked image', gray)
cv2.imwrite('masking.png',gray)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.waitKey(1)'''
plt.figure()
plt.subplot(1,1,1),plt.imshow(gray)
plt.xticks([])
plt.yticks([])
plt.grid(False)
plt.title('Brightness of image using colour masking')
plt.show()



