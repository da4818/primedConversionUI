import os
import re
import skimage.io
from collections import Counter
'''
method - primed conversion (pr) or photoconversion (pc)
excitation - red channel (red_excitation) or green channel (green_excitation)

FUNCTIONS:
Generate file object for excitation&method, or neither (for opening previous files)
Find id of pr-green, pr-red, pc-green, pc-red files
generate file names for incoming images

'''

#NOTE - relative path doesn't seem to work on tkinter - will use absolute path for time being
root_path = "/Users/debbie/python"

class Files:
    def __init__(self, excitation=None, method=None):
        #self.root = __file__ #Path of files.py --> useful in finding relative directory of image
        self.curr_filename = None
        self.curr_filepath = None
        self.colour = None
        if excitation is not None and method is not None:
            self.excitation = excitation #Whether saving to red channel or green channel
            self.colour = self.excitation[:-11]
            self.method = method #Whether primed conversion (pr) or photo conversion (pc)
            self.raw_path = self.get_raw_path()
            self.analysis_path = self.get_analysis_path()
            self.curr_file_ID = self.get_file_ID()

        '''else:
            print("Load previous files")
            self.get_prev_files()'''

    def get_raw_path(self):
        if self.colour is not None:
            absolute_path = root_path + '/GroupProject/raw_images/'+str(self.colour)
        else:
            absolute_path = root_path + '/GroupProject/raw_images/'
        return absolute_path #ValueError currently doesn't check if method input is valid

    def get_analysis_path(self):
        absolute_path = root_path + '/GroupProject/analysis_images/'+str(self.colour)
        return absolute_path #ValueError currently doesn't check if method input is valid

    def get_file_ID(self):
        path = self.get_raw_path()
        path1 = self.get_analysis_path()
        files_list = []
        for root, directories, filenames in os.walk(path):
            for name in filenames:
                if self.method+str("_") in name: #looks for pr or pc in filename
                    files_list.append((path, name))
        for i in path, path1:
            for root, directories, filenames in os.walk(i):
                for name in filenames:
                    if self.method+str("_") in name:
                        files_list.append((i, name))
        n = find_max(files_list)
        if (n == None or n == 0):
            n = 0  #Shows number of existing files of the existing experiments
        return n
    #Finds existing normalised & masked files for a given experiment
    # - if they both exist, then the experiment has been completed its raw image will exist
    # We will generate the corresponding raw image file name to find
    def get_prev_files(self):
        path = root_path + '/GroupProject/analysis_images'
        raw_path = root_path + '/GroupProject/raw_images'
        files_list = []
        roots_list = []
        for root, directories, filenames in os.walk(path):
            for name in filenames:
                out = root.replace("analysis_images", "raw_images")
                files_list.append(name)
        if len(files_list) > 0:
            prev_files = compare_filenames(files_list)

            for i, attr in enumerate(prev_files):
                prev_files[i] = "post_"+str(attr)+".png"
                if "green" in prev_files[i]:
                    roots_list.append(raw_path+"/green")
                elif "red" in prev_files[i]:
                    roots_list.append(raw_path+"/red")
        else:
            print("No existing files")
            prev_files = 0
        return prev_files, roots_list #roots list hasnt been updated

    def get_raw_images(self, prev_list = None, roots_list=None):
        path = root_path + '/GroupProject/raw_images'
        raw_files_list = []
        methods = []
        if prev_list is not None and roots_list is not None:
            raw_files_list = list(zip(roots_list,prev_list))
            for i, name in enumerate(raw_files_list):
                raw_files_list[i] = os.path.join(*name)
                if 'pc' in raw_files_list[i]:
                    methods.append('Photo Conversion')
                elif 'pr' in raw_files_list[i]:
                    methods.append('Primed Conversion')
        else:
            for root, directories, filenames in os.walk(path):
                for name in filenames:
                    if self.colour in name and self.method in name:
                        raw_files_list.append(name)
                        if 'pc' in name:
                            methods.append('Photo Conversion')
                        elif 'pr' in name:
                            methods.append('Primed Conversion')
        res = re.findall(r'\d+', str(raw_files_list))
        numbers = list(map(int, res))
        return list(raw_files_list), numbers, methods

    def get_file_name(self, type):
        if type == "pre":
            self.curr_file_ID = self.curr_file_ID+1 #the pre image is the first photo in the analysis process and decides the ID number of subsequent files
            filename = "pre_"+str(self.method)+"_"+str(self.colour)+"_"+str(self.curr_file_ID)+".png"
        elif type == "post":
            filename = "post_"+str(self.method)+"_"+str(self.colour)+"_"+str(self.curr_file_ID)+".png"
        elif type == "norm":
            filename = "norm_"+str(self.method)+"_"+str(self.colour)+"_"+str(self.curr_file_ID)+".png"
        elif type == "masked":
            filename = "masked_"+str(self.method)+"_"+str(self.colour)+"_"+str(self.curr_file_ID)+".png"
        return filename

    def get_normalised_image(self):
        path = self.get_analysis_path()
        for root, directories, filenames in os.walk(path):
            for name in filenames:
                if 'norm' in name and str(self.curr_file_ID) in name:
                    norm_file = (os.path.join(root, name))
        return norm_file

    def export_files(self):
        path = self.get_analysis_path()
        filename = "/norm_"+str(self.method)+"_"+str(self.colour)+"_"+str(self.curr_file_ID)+".png"
        filename1 = "/masked_"+str(self.method)+"_"+str(self.colour)+"_"+str(self.curr_file_ID)+".png"
        norm = skimage.io.imread(path+filename)
        masked = skimage.io.imread(path+filename1)
        masked_path = path+filename1
        print(masked_path)
        return norm, masked, masked_path

def find_max(name): #Find the largest filename ID number
    numbers = re.findall(r'\d+', str(name)) #Finds all the numbers listed in each file name
    res = list(map(int, numbers)) #Transforms into a list of type int
    if len(res) == 0: #Error check: if the folder of images is empty, set ID as 0
        res = [0]
    return max(res)

def compare_filenames(list):
    attributes = []
    for names in list:
        temp = names.replace("_", " ")
        attr = re.findall(r'(\w+)', temp)
        method = attr[1]
        colour = attr[2]
        ID = attr[3]
        attributes.append([method, colour, ID])
    counter = Counter([tuple(i) for i in attributes])
    file_info=[]
    for j in counter.items():
        if j[1] == 2:
            s = str(j[0])
            s = s.replace("\'","")
            s = s.replace(",","")
            s = s.replace("(","")
            s = s.replace(")","")
            s = s.replace(" ","_")
            file_info.append(s)
    return file_info


'''if __name__ == "__main__":
    f = Files()
    prev_files, roots = f.get_prev_files()
    previous, IDs, methods = f.get_raw_images(prev_files, roots)
    print(previous, IDs, methods)'''

