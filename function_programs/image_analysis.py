from math import floor
import numpy as np
import skimage.color
import skimage.io
import skimage.viewer
import skimage.filters
from scipy.signal import find_peaks
from scipy import ndimage
import cv2
from function_programs.colour_conversion import hex_to_RGB
#This performs the main image analysis - masking and plotting
def get_thresholds():
    t_Values = np.linspace(0, 1.0, num=10) #Can modify thresholds to meaningful values
    colours = ('#000000', '#01003F', '#0000ff', '#bb00ff', '#7B0003', '#ff00ff', '#45C3C0', '#00ffff', '#FFDC42', '#ffff00')
    return t_Values, colours

def export_images(filename):
    image = skimage.io.imread(filename)
    masked, _ = masked_image(filename)
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
    gray = cv2.imread(filename, cv2.IMREAD_GRAYSCALE) # better greyscale than skimage rgb2gray
                                                      # -> mapping doesn't lower red values relative to green valeus
    image = cv2.imread(filename)
    masks = [] #Mask to 'colour in' the parts of the image that meet the threshold criteria
    sigma = 2 #Blurring factor
    blur = skimage.filters.gaussian(gray, sigma=sigma)
    #Performs binary thresholding for each threshold value
    for t in t_Values:
        masks.append(blur > t)
    image[masks[0]] = hex_to_RGB(colours[0])
    image[masks[1]] = hex_to_RGB(colours[1])
    image[masks[2]] = hex_to_RGB(colours[2])
    image[masks[3]] = hex_to_RGB(colours[3])
    image[masks[4]] = hex_to_RGB(colours[4])

    return image, masks

# credit to Griesbecklab for the method of labelling, localizing and calculating median of samples through numpy.
# https://github.com/GriesbeckLab/Picker-Analysis/
def quantify(filename):
    _, masks = masked_image(filename)
    # Using binary mask from threshold = 0 which works with test images -> threshold will change when we get data
    labelled, sample_count = ndimage.label(masks[0]) # assigns unique int to each area of 1s it encounters = each sample
    if sample_count>=1:
        # gets center of each sample - same arrangement as median/mean/std_dev with input, label and index parameters
        sample_locations = ndimage.measurements.center_of_mass(masks[0], labelled, np.arange(1,sample_count+1))
        # flooring coordinates to have specific pixel locations
        sample_locations = [(floor(x),floor(y)) for x,y in sample_locations]
        '''
        # Could use greyscale to calculate since theoretically all pixel values are from red or green emission with filters.
        image = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
        medians = ndimage.median(image, labelled, np.unique(labelled[1:]))
        means = ndimage.mean(image, labelled, np.unique(labelled[1:]))
        std_devs = ndimage.standard_deviation(image, labelled, np.unique(labelled[1:]))
        '''
        # If camera outputs data with solely or mainly red/green values for pixel values -> don't greyscale, use img[:,:,X]
        # But check if image is in BGR or RGB format. with test images: BGR
        image = cv2.imread(filename)
        # P1/P2 are names of some test images
        if 'red' in filename or 'P2' in filename:
            medians = ndimage.median(image[:,:,2], labelled, np.unique(labelled[1:]))
            means = ndimage.mean(image[:,:,2], labelled, np.unique(labelled[1:]))
            std_devs = ndimage.standard_deviation(image[:,:,2], labelled, np.unique(labelled[1:]))
        elif 'green' in filename or 'P1' in filename:
            medians = ndimage.median(image[:,:,1], labelled, np.unique(labelled[1:]))
            means = ndimage.mean(image[:,:,1], labelled, np.unique(labelled[1:]))
            std_devs = ndimage.standard_deviation(image[:,:,1], labelled, np.unique(labelled[1:]))
        else:
            image2 = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
            medians = ndimage.median(image2, labelled, np.unique(labelled[1:]))
            means = ndimage.mean(image2, labelled, np.unique(labelled[1:]))
            std_devs = ndimage.standard_deviation(image2, labelled, np.unique(labelled[1:]))
        samples = []
        for i in range(sample_count):
            sample_dict = {
                'Sample #':i+1,
                'location':sample_locations[i],
                'median':medians[i+1],
                'mean':means[i+1],
                'std_dev':std_devs[i+1]
            }
            samples.append(sample_dict)
    else:
        samples = ""
    return samples


if __name__ == '__main__':
    masked_image("C:/VscodeProjects/imgnalysis/Primed_Conversion_efficiency_Images_test/P1.png")
