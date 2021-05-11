import cv2
import numpy as np


def generate_brightness_profile(filename):
    img = cv2.imread(filename)
    width=img.shape[0]
    start_x=0
    end_x=width
    y=200
    colour_mask = cv2.imread(filename)
    colour_mask[y:y+1, start_x:end_x] = (255,255,255)
    mask = np.zeros(img.shape[:2], np.uint8)
    mask[y:y+1, start_x:end_x] = 255
    pixel_brightnesses = img[start_x:end_x,y]
    #pixel_locations = np.arange(start_x,end_x)
    return colour_mask, pixel_brightnesses