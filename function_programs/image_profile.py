import cv2
import os
import numpy as np
import matplotlib.pyplot as plt
from function_programs.find_centres import *
def generate_brightness_profile(filename):
    img = cv2.imread(filename)
    #Convert image to HSV values
    hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    width = img.shape[0]
    #We want to create a line profile across the width of the image, so we choose our start and end point
    start_x = 0
    end_x = width
    #Create height to create brightness profile
    #y = y_coords #Will possibly create a user defined height by finding cursor location
    colour_mask = cv2.imread(filename)
    y_coords = find_centres(filename)
    pixel_brightnesses=[]
    new_y =[]
    new_y.append(y_coords[0])
    new_y.append(y_coords[2])
    for y in list(new_y):
        colour_mask[y:y+1, start_x:end_x] = (255, 255, 255)
        pixel_info = hsv_img[y, start_x:end_x] #returns a 3 column vector containing Hue, Saturation and Value (brightness)
        pixel_brightnesses.append(pixel_info[:, 2])

    mask = np.zeros(img.shape[:2], np.uint8)
    mask[y:y+1, start_x:end_x] = 255
    return colour_mask, pixel_brightnesses, new_y



def plot_profile(filename):
    img = cv2.imread(filename)
    #Convert image to HSV values
    hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    width = img.shape[0]
    #We want to create a line profile across the width of the image, so we choose our start and end point
    start_x = 0
    end_x = width
    #Create height to create brightness profile
    #y = y_coords #Will possibly create a user defined height by finding cursor location
    colour_mask = cv2.imread(filename)
    y = 75
    pixel_brightnesses=[]
    colour_mask[y:y+1, start_x:end_x] = (255, 255, 255)
    pixel_info = hsv_img[y, start_x:end_x] #returns a 3 column vector containing Hue, Saturation and Value (brightness)
    pixel_brightnesses.append(pixel_info[:, 2])

    mask = np.zeros(img.shape[:2], np.uint8)
    mask[y:y+1, start_x:end_x] = 255
    return colour_mask, pixel_brightnesses
'''if __name__ == "__main__":
    #y_coords = find_centres('sample.png')
    #print(y_coords)
    colour_mask, pixel_brightness = plot_profile('sample_image.png')
    pic = cv2.imread("profile1.png")
    cv2.imshow("Plot Profile", pic)
    cv2.waitKey(0)
    
    cv2.destroyAllWindows()

    fig, axs = plt.subplots(2)
    axs[0].imshow(colour_mask)
    axs[0].set_title("Sample Image")
    axs[0].get_xaxis().set_visible(False)
    for p in pixel_brightness:
        axs[1].plot(p)
    axs[1].set_title("Plot Profile")
    axs[1].set_xlabel('Pixel location')
    axs[1].set_ylabel('Brightness')
    plt.show()'''




