from os import path
import numpy as np  # to load images in array type with lots of functions to help in analysis
import matplotlib.pyplot as plt  # used to visualize what's happening with the images

from skimage import io  # loading image
from skimage import img_as_float
from skimage.filters import gaussian, threshold_minimum  # functions to blur and create mask
from skimage.color import rgb2gray  # greyscale conversion, not sure of the greyscale bit-depth but probably modulable
from scipy.ndimage import mean, median  # useful to do median of specific areas of image selectively
from scipy.ndimage import standard_deviation as std
import glob  # glob used to extract all filepaths from desired folder

'''
    Notes:
    - Script needs numpy, matplotlib, skimage, glob, and PIL libraries.
    - PIL is only needed for a technicality right now, because the images are tiff images and there's an annoying bug 
    when using skimage to open a tiff file. (still technically using skimage to open the file but through the PIL plugin).
    - blur and threshold methods might change for our images, we'll have to test and find best methods again
    - have to be careful with functions, gotta be able to work with more than 1 sample 


    Can do:
    - loads all images from a filepath
    - identify if image is red/green excitation, pre/photo/primed conversion through file name (case sensitive!)
    - blurs images through gaussian filter
    - uses minimum threshold method to distinguish between inner and outer rectangle (returns single value)
    - makes binary arrays of images through applying minimum threshold value
    - masks outer rectangle from original image using binary array
    - calculate mean/median/std dev of inner rectangle area
    - calculates ratios of intensity change of inner rectangle between pre and post conversion
    - calculates normalized means of second folder of images, normalizing with first folder of images (NOT DONE)
    
    Need to do:
    - test out more filters for blur
    - look for different ways to get intensity (cdf, idk)
    - take noise into account for median/mean intensity values and difference
    - fins out if what I'm doing is good normalization, 
        Konstantinos told us to use 1 set of images as ref. to normalize second set
    - add quantification values to graph_image function
    - add text panel with intensity ratios to graph_image function 
    - 
         
    
    Questions on analysis:
    - do we get single value from a ref image and normalize using that value or should we get multiple values representing
    an area of the image and normalize area with area
    - should we use same mask for all images? - doing that for now, to help in having same amount of pixels used in calculations
    - is using median good way to get intensity values for an area
  
  
path = 'Primed_Conversion_efficiency_Images_test/Test File/4/pr-mEosFP new_pr-mEosFP_new_post-pc_4_1_green.tif'

'''

# empty class to act as a structure for image data
class ImageData:
    def __init__(self, paths, names):
        self.paths = paths
        self.names = names

class ImageAnalyze:
    def __init__(self, images_array, filenames):

        self.images = images_array
        self.filenames = filenames
        # Converting to 0,1 range using img_to_float for calculations (could also just keep in 0,255)
        self.images_float = np.array([img_as_float(img) for img in self.images])
        self.IData = []
        self.categorize()

    # categorizes each image by creating an ImageData object and populating it
    def categorize(self):
        for i, filename in enumerate(self.filenames):
            ID_temp = ImageData()
            ID_temp.array = self.images[i]
            ID_temp.filename = self.filenames[i]
            ID_temp.float_array = self.images_float[i]
            # checking what excitation colour the picture is.
            # IF STATEMENTS ARE CASE SENSITIVE, GOTTA BE CAREFUL WHEN NAMING FILES
            if 'green' in filename:
                ID_temp.channel = 'green'
            elif 'red' in filename:
                ID_temp.channel = 'red'
            else:
                # manual choice for which channel to calculate in.
                print("ERROR: Program cannot assign channel to image \'"+ID_temp.filename+"\'")
                while True:
                    k = input("Please enter channel manually (0 = red, 1 = green): ")
                    if k == '0':
                        ID_temp.channel = 'red'
                        break
                    elif k == '1':
                        ID_temp.channel = 'green'
                        break
                    else:
                        print("Please input 0 for a red excitation image, 1 for a green excitation image.")
            # checking if picture is preconversion, photoconverted or primed converted
            if 'pre' in filename:
                ID_temp.converted = False
            elif 'post' in filename:
                ID_temp.converted = True
            else:
                # manual choice for conversion information
                print("ERROR: Program cannot find out if image \'"+ID_temp.filename+"\' is converted or not.")
                while True:
                    k = input("Please enter 0 for pre-conversion, 1 for Photoconverted, "
                              "2 for Primed converted")
                    if k == '0':
                        ID_temp.converted = False
                        break
                    elif k == '1':
                        ID_temp.channel = True
                        # self.IData[i].primed = False
                        break
                    elif k == '2':
                        ID_temp.channel = True
                        # self.IData[i].primed = True
                        break
                    else:
                        print("Please input 0 for a pre-conversion image, "
                              "1 for a photoconversion image, 2 for a primed conversion image")
            self.IData.append(ID_temp)

    # grayscales then blurs images. Exists as its own function for ease of modification if we'll be hanging
    # filtering methods with our images
    def blur_images(self):
        # greyscaling the images as later functions accept only 2-D arrays
        # blurring the images through a gaussian filter to eliminates spikes,sigma changes how much it blurs
        # COULD USE DIFF TYPE HAVEN't TESTED THEM ALL YET
        self.images_grey = np.array([rgb2gray(img) for img in self.images])
        # adding gaussian filter onto gray images to separate inner and outer rectangle better, in order for threshold
        # masking to work better (sigma = 2 chosen by testing multiple values)
        self.images_blurred = np.array([gaussian(img, sigma=2) for img in self.images_grey])
        return self.images_blurred

    def mask(self):
        # getting threshold value for each image using minimum method, as it works the cleanest in isolating the
        # rectangle in the post-conversion images compared to other threshold methods (used 'try_all_threshold'
        # function to compare)
        self.threshold = np.array([threshold_minimum(img) for img in self.images_blurred])
        self.binary_array = self.images_blurred[0] >= self.threshold[0]

        # using binary array to mask all values external to rectangle
        for img in self.images:
            img[self.binary_array] = 0  # values get set to black
        return self.images, self.binary_array

    def quantify(self):
        """
        scipy.ndimage.median/mean/std_dev functions pretty useful bc it lets us choose areas to calculate in:
        -input = image(s) as arrays
        -labels = integer arrays that'll make the function take into account only specific areas of image (here binary array)
        -index = specify region labels. if no index, values where labels is nonzero is taken into account
        (if index = [0, 1] -> returns 2 medians/means: one over values where labels=0 and other over vals where label=1)

        If we make a binary image of where the samples are, we can then assign a value to each sample area, creating a label
        array with as many diff numbers as samples on the plate. (assign using ndimage.label)
        We can then use the label array as 'labels' in median/mean, and the index as np.unique(labels) that would output
        an array with 1 iteration of every different number in the label array.
        tl;dr: - useful when we'll be working with many samples

        (credit to the lab that made the picker screening platform, got the idea from their code)
        """
        # initializing lists for median/mean/standard deviation values
        self.medians = []
        self.means = []
        self.std_devs = []
        for i in range(len(self.IData)):
            if self.IData[i].channel == 'green':
                # median/mean/dev of values in the green channel (=1) that have a corresponding value of 0
                # on the pixel in the binary array of the same size of the image.
                self.IData[i].median = median(self.IData[i].float_array[:,:,1], self.binary_array, 0)
                self.IData[i].mean = mean(self.IData[i].float_array[:,:,1], self.binary_array, 0)
                self.IData[i].std_dev = std(self.IData[i].float_array[:,:,1], self.binary_array, 0)
            elif self.IData[i].channel == 'red':
                self.IData[i].median = median(self.IData[i].float_array[:,:,0], self.binary_array, 0)
                self.IData[i].mean = mean(self.IData[i].float_array[:,:,0], self.binary_array, 0)
                self.IData[i].std_dev = std(self.IData[i].float_array[:,:,0], self.binary_array, 0)
            # appending values to their general list in self
            self.medians.append(self.IData[i].median)
            self.means.append(self.IData[i].mean)
            self.std_devs.append(self.IData[i].std_dev)
        return self.means


# graphing all images in array onto same figure.
def graph_images(images_array, title=None, med_means=None, std_devs=None, ratios=None):
    plt.figure(figsize=(10, 10))  # big size to see all images in okay quality
    # plotting each image onto the figure, with possibility of title, axes, legend
    for i, img in enumerate(images_array):
        plt.subplot(2, 4, i + 1)
        plt.xticks([])
        plt.yticks([])
        plt.grid(False)
        plt.imshow(img, cmap='gray')
        plt.title("Image " + str(i), fontsize=20)
        if title:   plt.suptitle(title, fontsize=50)
        else:       plt.suptitle("Images", fontsize=70)
    plt.show()
    # plt.close()
#Function to
def get_files():
    filepath = '/Users/debbie/BioEng/year 3/Group project/Primed_Conversion_efficiency_Images_test/Test File/4/*.tif'
    imagepaths = glob.glob(filepath, recursive=True)
    filenames = [path.basename(path_string) for path_string in imagepaths]
    new_set = imagepaths #Need to create a new list of file paths that don't include the filename itself (as this is needed for showing an image on tkinter)
    i=0;
    for x in new_set:
        for y in filenames:
            if (x.find(y)>0):
                new_set[i] = x.replace(y, '')
                i=i+1
    imageinfo = ImageData(new_set, filenames)
    return imageinfo


def main():
    # loading up all image paths in a list using glob
    filepath = 'Primed_Conversion_efficiency_Images_test/Test File/*/*.tif'
    imagepaths = glob.glob(filepath, recursive=True)

    # isolate filename to categorize files
    filenames = [path.basename(path_string) for path_string in imagepaths]
    # loading images as numpy arrays, all inside a numpy array
    images = np.array([io.imread(img, plugin='pil') for img in imagepaths])

    # instantiating the ImageAnalyze class
    IA = ImageAnalyze(images,filenames)

    images_blurred = IA.blur_images()

    images_masked, binary_array = IA.mask()

    graph_images(images)
    graph_images(images_blurred, title='Gaussian blur, sigma=2')
    graph_images(images_masked, title='Images with masking')
    """
    Testing quantification methods :
    median values are close to identical to mean values, makes sense since proteins are evenly distributed in sample.
    # HAVEN'T TAKEN NOISE INTO ACCOUNT YET. could be done when we have images of plate, taking median of all values on
    # plate and substracting it from medians of sample areas. can also substract median absolute deviation

    # Normalizing 1st test - use mean of images in folder 4 and center pixels of folder 5 images around it
    # -> a start, vals seem better than non-normalized (see commented vals below)
    # 2nd test: - see if using std deviation makes values more understandable
    # -> red post-excitation vals have std_devs 10x larger than any other std_devs. makes mean post-conversion
    # red excitation intensity very small (~0.4) compared to green post and pre (2.5-2.8). red pre negative
    #3rd test: - try normalizing and shifting range to have all values positive
    # -> HAVEN'T TRIED YET
    """

    means = IA.quantify()
    normalized_means = []
    for i, img in enumerate(IA.images_float[4:]):
        # just doing one image minus the other gets same result as doing image minus mean
        img = (img - IA.images_float[i])
        # img = (img - means[i])/std_devs[i]
        # img = (img - means[i])
        if i%2 ==0:
            normalized_means.append(mean(img[:,:,1], binary_array, 0))
        else:
            normalized_means.append(mean(img[:,:,0], binary_array, 0))

    # ratios of green_post/green_pre and green_post/red_post similar, good sign i think
    ratio_g_n = normalized_means[0]/normalized_means[2]  # = 0.8712845825803137
    ratio_post_r_n = normalized_means[0]/normalized_means[1]  # =0.789120575543297
    print("Ratio of change in green excitation post-conversion: " + str(ratio_g_n))
    print(" or a "+str(1-ratio_g_n)+" decrease in intensity")
    print("Ratio of intensity change between green and red excitation, post-conversion: " + str(ratio_post_r_n))
    print(" or a "+str(1-ratio_post_r_n)+" difference in intensity")

    # means = IA.means
    ratio_r_n = normalized_means[1]/abs(normalized_means[3])  # = -15.353829343399187
    ratio_pre_n = normalized_means[2]/abs(normalized_means[3])  # = -0.07191176575637018
    ratio_r_postn = normalized_means[1]/normalized_means[2]  # = 1.1041209792058053
    # values to compare normalized means to
    ratio_g = means[4]/means[6]  # = 0.8640487515575197
    ratio_r = means[5]/means[7]  # = 142.0985996824022
    ratio_pre = means[7]/means[6]  # = 0.013097348702334526
    ratio_post = means[5]/means[4]  # = 2.1539466457176744
    ratio_r_post = means[5]/means[6]  # = 1.8611149101538638
    k = 1

if __name__ == "__main__":
    main()

# code purgatory, might need to bring some of this back at some point so I'd rather not delete yet
#
#
# g_1 = images[0][~b_g_postpc_1]
# g_2 = images[2][~b_g_postpc_1]
# r_1 = images[1][~b_r_postpc_1]
# r_2 = images[3][~b_r_postpc_1]
#
# b_g_postpc_2 = images_blurred[4] >= min_threshold[4]
# b_r_postpc_1 = images_blurred[1] <= min_threshold[1]
# b_r_postpc_2 = images_blurred[5] <= min_threshold[5]
#
#
# images[0][b_g_postpc_1] = 0
# # masking same area onto pre-conversion image for comparisons
# images[2][b_g_postpc_1] = 0
# # second green pair
# images[4][b_g_postpc_2] = 0
# images[6][b_g_postpc_2] = 0
# # red pairs
# images[1][b_r_postpc_1] = 0
# images[3][b_r_postpc_1] = 0
# images[5][b_r_postpc_2] = 0
# images[7][b_r_postpc_2] = 0
#
# g_float_1 = g_float_1*50
# g_float_2 = g_float_2*50
# r_float_1 = r_float_1*50
# r_float_2 = r_float_2*50
#
# converting to float in 0,1 range
#     g_grey_1 = rgb2gray(images[0])
#     g_grey_2 = rgb2gray(images[2])
#     r_grey_1 = rgb2gray(images[1])
#     r_grey_2 = rgb2gray(images[3])
#     # ratios between means for greyscale
#     ratio_red = r_mean_post/r_mean_pre  # mean intensity ratio in red excitation, pre and post-conversion
#     ratio_green = g_mean_post/g_mean_pre  # mean intensity ratio in green excitation, pre and post-conversion
#     ratio_pre = r_mean_pre/g_mean_pre
#     ratio_post = r_mean_post/g_mean_post
#     ratio_r_post = r_mean_post/g_mean_pre
# # same for greyscale
#     g_mean_post = np.mean(g_grey_1[np.nonzero(g_grey_1)])
#     g_mean_pre  = np.mean(g_grey_2[np.nonzero(g_grey_2)])
#     r_mean_post = np.mean(r_grey_1[np.nonzero(r_grey_1)])
#     r_mean_pre  = np.mean(r_grey_2[np.nonzero(r_grey_2)])

#
# def quantify(images_array, binary_array):
#     # Not using rgb2gray for calculations as the greyscale doesn't equally transform green and red
#     # (Y = 0.2125 R + 0.7154 G + 0.0721 B, from scikit image documentation)
#     # Converting to 0,1 range using img_to_float instead. (could also just keep in 0,255)
#     images_float = np.array([img_as_float(img) for img in images_array])
#     # initializing lists for median/mean values
#     green_medians = []
#     green_means = []
#     red_medians = []
#     red_means = []
#     means = []
#     medians = []
#     std_devs = []
#
#     for i, img in enumerate(images_float):
#         if i%2==0:
#             green_medians.append(median(img[:,:,1], binary_array, 0))
#             green_means.append(mean(img[:,:,1], binary_array, 0))
#             median_temp = median(img[:,:,1], binary_array, 0)
#             mean_temp = mean(img[:,:,1], binary_array, 0)
#             stddev_temp = median(img[:,:,1], binary_array, 0)
#         else:
#             red_medians.append(median(img[:,:,0], binary_array, 0))
#             red_means.append(mean(img[:,:,0], binary_array, 0))
#             median_temp = median(img[:,:,0], binary_array, 0)
#             mean_temp= mean(img[:,:,0], binary_array, 0)
#             stddev_temp = median(img[:,:,0], binary_array, 0)
#         medians.append(median_temp)
#         means.append(mean_temp)
#         std_devs.append(stddev_temp)
#     return (means, medians, std_devs)



