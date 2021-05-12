import cv2
import numpy as np
import os
def generate_brightness_profile(filename):
    img = cv2.imread(filename)
    width = img.shape[0]
    start_x = 0
    end_x = width
    y = 100 #make y variable - possibly find cursor location
    colour_mask = cv2.imread(filename)
    colour_mask[y:y+1, start_x:end_x] = (255,255,255)
    mask = np.zeros(img.shape[:2], np.uint8)
    mask[y:y+1, start_x:end_x] = 255
    pixel_brightnesses = img[y, start_x:end_x]
    pixel_locations = np.arange(start_x, end_x)
    return colour_mask, pixel_brightnesses