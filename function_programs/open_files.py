import glob
import shutil
from PIL import Image
import os
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
    return pre_files_list, post_files_list

def save_image(pre, post):
    root, name = zip(*post)
    root1, name1 = zip(*pre)
    img  = Image.new( mode = "RGB", size = (50, 50))
    newpost="post"+str(len(post)+1)+".png" #this works when no files are deleted - ensure no 'out of frame' numbering
    newpre = "pre"+str(len(pre)+1)+".png"
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