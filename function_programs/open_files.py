import glob
import shutil
from PIL import Image
import os
import re
from os import path
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

    root, name = zip(*post_files_list)
    numbers = re.findall(r'\d+', str(name))
    res = list(map(int, numbers))
    print (max(res))
    return pre_files_list, post_files_list

def find_max(name):
    numbers = re.findall(r'\d+', str(name))
    res = list(map(int, numbers))
    return max(res)


def save_image(pre, post):
    root, name = zip(*pre)
    root1, name1 = zip(*post)

    img = Image.new( mode = "RGB", size = (50, 50))
    preindex = find_max(name)
    postindex = find_max(name1)
    index = max(preindex, postindex) #in case files are deleted non-uniformly, the new set of images will use an ID that hasn't been used before

    newpost="post"+str(index+1)+".png" #This will create a file name of the largest number +1
    newpre = "pre"+str(index+1)+".png"
    print(newpost)
    #img.save(str(root[0])+str(newpost))
    img.save(str(root1[0])+str(newpre))




if __name__ == "__main__":
    #open_files("red")
    open_files("green")

    '''for root, directories, files in os.walk('/Users/debbie/python/GroupProject/Images/Green/'):
        for name in files:
            files_list.append(os.path.join(root, name))
    print(files_list)'''