import os
import re
'''
FILES CLASS FUNCTIONALITY
- returns path of existing raw images (taken with camera) --> will be used in windows.py when loading previous data
- generates a new (unique) ID number for all filenames in the current session --> finds the largest existing ID number and increments it by 1
- creates filenames using the ID number for pre, post, normalised and masked images: 
e.g., post_pr_green4.png - 4th raw image of green excitation after undergoing primed conversion
- various variables are saved --> this is useful in camera.py
'''
#NOTE - relative path doesn't seem to work on tkinter - will use absolute path for time being
class files:
    def __init__(self, excitation, method):
        self.excitation = excitation #Whether saving to red channel or green channel
        self.method = method #Whether primed conversion (pr) or photo conversion (pc)
        self.root = __file__ #Path of files.py --> useful in finding relative directory of image
        self.fileID = 0
        self.curr_path = ""
        self.names = self.generate_file_ID()

    def get_raw_images(self):
        path = "raw_images"
        relative_path = os.path.relpath(path, self.root)
        raw_files_list = []
        for root, directories, filenames in os.walk(relative_path):
            for name in filenames:
                raw_files_list.append(os.path.join(root, name))
        '''for root, directories, filenames in os.walk(path, relative_path):
            for name in filenames:
                if 'pre' in name:
                    raw_files_list.append((path, name))'''
        return raw_files_list

    def get_raw_path(self):
        colour = self.excitation[:-11] #removes '_excitation' from the string
        relative_path = '/Users/debbie/python/GroupProject/raw_images/'+str(colour)
        return relative_path #ValueError currently doesn't check if method input is valid

    def get_analysis_path(self):
        colour = self.excitation[:-11]
        relative_path = '/Users/debbie/python/GroupProject/analysis_images/'+str(colour)
        return relative_path #ValueError currently doesn't check if method input is valid

    def generate_file_ID(self):
        path = self.get_raw_path()
        path1 = self.get_analysis_path()

        files_list = []
        for root, directories, filenames in os.walk(path):
            for name in filenames:
                files_list.append((root, name))
        for i in path, path1:
            for root, directories, filenames in os.walk(i):
                for name in filenames:
                    files_list.append((i, name))
        n = find_max(files_list)
        self.fileID = n+1 #Create ID number that is increment of most recent fileID number
        names = self.get_file_names()
        return names

    def get_file_names(self):
        pre_filename = "pre_"+str(self.method)+"_"+str(self.excitation)+str(self.fileID)+".png"
        post_filename = "post_"+str(self.method)+"_"+str(self.excitation)+str(self.fileID)+".png"
        normalised_filename = "norm_"+str(self.method)+"_"+str(self.excitation)+str(self.fileID)+".png"
        masked_filename = "masked_"+str(self.method)+"_"+str(self.excitation)+str(self.fileID)+".png"
        return pre_filename, post_filename, normalised_filename, masked_filename

def find_max(name): #Find the largest filename ID number
    numbers = re.findall(r'\d+', str(name)) #Finds all the names listed in each file name
    res = list(map(int, numbers)) #Transforms into a list of type int
    if len(res) == 0: #Error check: if the folder of images is empty, set ID as 0
        res = [0]
    return max(res)

if __name__ == "__main__":
    f = files("green_excitation", "pc")
    print(f.fileID)
    print(f.get_raw_images())

'''if __name__ == "__main__":
    f = files("green_excitation", "pc")
    print(f.fileID)
    print(f.get_raw_images())'''
