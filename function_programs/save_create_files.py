
from PIL import Image
from function_programs.image_normalisation import *
import os
import re



def save_analysis_images(state,type):
    if state == "red":
        prefilepath = '/Users/debbie/python/GroupProject/raw_images/red/'
        postfilepath = prefilepath
        normalisedfilepath = '/Users/debbie/python/GroupProject/analysis_images/red_normalised/'
    elif state == "green":
        prefilepath = '/Users/debbie/python/GroupProject/raw_images/green/'
        postfilepath = prefilepath
        normalisedfilepath = '/Users/debbie/python/GroupProject/analysis_images/green_normalised/'

    post_files_list = []
    pre_files_list = []
    normalised_files_list = []
    for root, directories, files in os.walk(postfilepath):
        for name in files:
            post_files_list.append((postfilepath, name)) #os.path.join
    for root, directories, files in os.walk(prefilepath):
        for name in files:
            pre_files_list.append((root, name)) #os.path.join
    for root, directories, files in os.walk(normalisedfilepath):
        for name in files:
            normalised_files_list.append((normalisedfilepath, name)) #os.path.join
    if len(normalised_files_list) == 0:
        normalised_files_list.append((normalisedfilepath, ""))
    imagepaths, imagenames = get_image_info(pre_files_list, post_files_list, normalised_files_list, state, type)
    return imagepaths, imagenames


def find_max(name):
    numbers = re.findall(r'\d+', str(name))
    res = list(map(int, numbers))
    if len(res) == 0:
        res = [0]
    return max(res)

#This saves the image and returns it, ready for analysis
def get_image_info(pre, post, norm, state, type):
    pre_root, name = zip(*pre)

    if len(post) == 0:
        post_index = 0
        post_root = pre_root
    elif len(post) > 0:
        post_root, name1 = zip(*post)
        post_index = find_max(name1)
    if len(norm) == 0:
        norm_index = 0;
        #norm_root =
    elif len(norm) > 0:
        norm_root, name2 = zip(*norm)
        norm_index = find_max(name2)

    #img = Image.new(mode = "RGB", size = (50, 50),color = (153, 153, 255))
    #img1 = Image.new(mode = "RGB", size = (50, 50),color = (255, 153, 255)) #post will undergo normalisation
    img, img1, img2 = normalise_image(state)
    pre_index = find_max(name)

    index = max(pre_index, post_index, norm_index) #in case files are deleted non-uniformly, the new set of analysis_images will use an ID that hasn't been used before

    if type == "pc": #for photoconversion
        post_filename = "postpc"+str(index+1)+".png" #This will create a file name of the largest number +1
        pre_filename = "prepc"+str(index+1)+".png"
        norm_filename = "normpc"+str(index+1)+".png"
    if type == "pr": #for primed conversion
        post_filename = "postpr"+str(index+1)+".png" #This will create a file name of the largest number +1
        pre_filename = "prepr"+str(index+1)+".png"
        norm_filename = "normpr"+str(index+1)+".png"

    img.save(str(pre_root[0])+str(pre_filename)) #the roots will be the same e.g. pre_root[0] == pre_root[1] == ...
    img1.save(str(post_root[0])+str(post_filename))
    img2.save(str(norm_root[0])+str(norm_filename))

    pre_img = os.path.join(pre_root[0], pre_filename)
    #post_img = os.path.join(post_root[0], post_filename)
    norm_img = os.path.join(norm_root[0],norm_filename)

    '''pre_img = Image.open(os.path.join(pre_root[0],pre_filename))
    post_img = Image.open(os.path.join(post_root[0],post_filename))
    #pre_img.show()'''
    paths = [pre_img, norm_img]
    names = [pre_filename, norm_filename]
    return paths, names


'''if __name__ == "__main__":
    #open_files("red")
    pre,post = save_analysis_images("green")'''

