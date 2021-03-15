import numpy as np
import skimage.color
import skimage.io
import skimage.viewer
from scipy.signal import find_peaks
import cv2
from function_programs.colour_conversion import hex_to_RGB
#This performs the main image analysis - masking and plotting
def get_thresholds():
    t_Values = np.linspace(0, 1.0, num=10) #Can modify thresholds to meaningful values
    colours = ('#000000', '#0000FF', '#1F38F0', '#72BCF5', '#96F7F4', '#95F4B3', '#A1F359', '#DFF860', '#F7FA63', '#FFFF00')
    return t_Values, colours

def export_images(filename):
    image = skimage.io.imread(filename)
    masked = masked_image(filename)
    return image, masked

def generate_histogram(filename):
    image = skimage.io.imread(filename, as_gray=True)
    histogram, bin_edges = np.histogram(image, bins=256, range=(0, 1))
    return histogram, bin_edges

def obtain_peaks(t, d, histogram, bin_edges):
    peaks, _ = find_peaks(histogram, threshold=t, distance=d)
    return bin_edges[peaks], histogram[peaks]

def masked_image(filename):
    t_Values, colours = get_thresholds()
    image = skimage.io.imread(filename, as_gray=True)
    gray = cv2.imread(filename)
    masks = [] #Mask to 'colour in' the parts of the image that meet the threshold criteria
    sigma = 2 #Blurring factor
    blur = skimage.color.rgb2gray(image) #Blur and grayscale before thresholding
    blur = skimage.filters.gaussian(blur, sigma=sigma)
    #Performs binary thresholding for each threshold value
    for t in t_Values:
        masks.append(blur > t)
    gray[masks[0]] = hex_to_RGB(colours[0])
    gray[masks[1]] = hex_to_RGB(colours[1])
    gray[masks[2]] = hex_to_RGB(colours[2])
    gray[masks[3]] = hex_to_RGB(colours[3])
    gray[masks[4]] = hex_to_RGB(colours[4])
    return gray
