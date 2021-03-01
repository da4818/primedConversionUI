import glob
import shutil
from PIL import Image
import os
from os import path
import re
import cv2
import numpy as np
from skimage import io
def open_files(state):
    if state == "red":
        prefilepath = '/Users/debbie/python/GroupProject/Images/Red/Red_Pre_Conversion/'
        postfilepath = '/Users/debbie/python/GroupProject/Images/Red/Red_Post_Conversion/'
    elif state == "green":
        prefilepath = '/Users/debbie/python/GroupProject/Images/Green/Green_Pre_Conversion/'
        postfilepath = '/Users/debbie/python/GroupProject/Images/Green/Green_Post_Conversion/'
    post_files_list=[]
    pre_files_list=[]
    for root, directories, files in os.walk(postfilepath):
        for name in files:
            post_files_list.append((root, name)) #os.path.join
    for root, directories, files in os.walk(prefilepath):
        for name in files:
            pre_files_list.append((root, name)) #os.path.join

    return pre_files_list, post_files_list

def find_max(name):
    numbers = re.findall(r'\d+', str(name))
    res = list(map(int, numbers))
    return max(res)

#This saves the image and returns it, ready for analysis
def save_image(pre, post):
    pre_root, name = zip(*pre)
    post_root, name1 = zip(*post)

    img = Image.new( mode = "RGB", size = (50, 50),color = (153, 153, 255))
    img1 = Image.new( mode = "RGB", size = (50, 50),color = (255, 153, 255)) #post will undergo normalisation
    pre_index = find_max(name)
    post_index = find_max(name1)
    index = max(pre_index, post_index) #in case files are deleted non-uniformly, the new set of images will use an ID that hasn't been used before

    post_filename = "post"+str(index+1)+".png" #This will create a file name of the largest number +1
    pre_filename = "pre"+str(index+1)+".png"

    img.save(str(pre_root[0])+str(pre_filename)) #the roots will be the same e.g. pre_root[0] == pre_root[1] == ...
    img1.save(str(post_root[0])+str(post_filename))

    pre_img = Image.open(os.path.join(pre_root[0],pre_filename))
    post_img = Image.open(os.path.join(post_root[0],post_filename))
    #pre_img.show()
    return pre_img, post_img






if __name__ == "__main__":
    #open_files("red")
    pre,post = open_files("green")
    save_image(pre,post)

    '''for root, directories, files in os.walk('/Users/debbie/python/GroupProject/Images/Green/'):
        for name in files:
            files_list.append(os.path.join(root, name))
    print(files_list)'''