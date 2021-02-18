import numpy as np
import skimage.color
import skimage.io
import skimage.viewer
import cv2
from function_programs.colour_conversion import hex_to_BGR, hex_to_RGB
def export_images(filename):
    image = skimage.io.imread(filename)
    masked = masked_image(filename)
    return image, masked

def histogram(filename):
    image = skimage.io.imread(filename, as_gray=True)
    histogram, bin_edges = np.histogram(image, bins=256, range=(0, 1))
    return histogram,bin_edges

def masked_image(filename):
    t_Values=np.linspace(0,1.0, num=5)
    colours = ('#0000ff','#bb00ff','#ff00ff','#00ffff','#ffff00')
    image = skimage.io.imread(filename, as_gray=True)
    gray = cv2.imread(filename)
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
    gray[masks[3]] = hex_to_RGB(colours[2])
    gray[masks[4]] = hex_to_RGB(colours[4])
    return gray