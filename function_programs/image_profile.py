import cv2
import numpy as np
def generate_brightness_profile(filename):
    img = cv2.imread(filename)
    #Convert image to HSV values
    hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    width = img.shape[0]
    #We want to create a line profile across the width of the image, so we choose our start and end point
    start_x = 0
    end_x = width
    #Create height to create brightness profile
    y = 200 #Will possibly create a user defined height by finding cursor location
    colour_mask = cv2.imread(filename)
    colour_mask[y:y+1, start_x:end_x] = (255, 255, 255)
    mask = np.zeros(img.shape[:2], np.uint8)
    mask[y:y+1, start_x:end_x] = 255
    pixel_info = hsv_img[y, start_x:end_x] #returns a 3 column vector contains Hue, Saturation and (brightness) Value
    pixel_brightnesses = pixel_info[:, 2]
    return colour_mask, pixel_brightnesses
