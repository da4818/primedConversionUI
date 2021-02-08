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
    - using blur and threshold methods might change for our images, we'll have to test and find best methods again
    - have to be careful with functions, gotta be able to work with more than 1 sample 


    Can do:
    - loads all images from a file as greyscale
    - graphs them through matplotlib
    - blurs images through gaussian filter
    - uses minimum threshold method to distinguish between inner and outer rectangle (returns single value)
    - makes binary arrays of images through applying minimum threshold value
    - masks outer rectangle from original image using binary array
    - gets median change in intensity of inner rectangle between pre and post conversion
    
    Need to do:
    - test out more filters for blur
    - look for different ways to get intensity (mean, cdf, idk)
    - take noise into account for median intensity values and difference
    - make blur, threshold and binary array into separate, dynamic functions
    - learn to normalize, Konstantinos told us to use 1 set of images as ref. to normalize second set
    
        
         
    
    Questions on analysis:
    - do we get single value from a ref image and normalize using that value or should we get multiple values representing
    an area of the image and normalize area with area
    - should we use same mask for all images? - doing that for now, to help in having same amount of pixels used in calculations
    - is using median good way to get intensity values for an area
    
'''


# path = 'Primed_Conversion_efficiency_Images_test/Test File/4/pr-mEosFP new_pr-mEosFP_new_post-pc_4_1_green.tif'


# graphing all images in array onto same figure.
def graph_images(images_array):
    plt.figure(figsize=(10, 10))  # big size to see all images in okay quality
    # plotting each image onto the figure, with possibility of title, axes, legend
    for i, img in enumerate(images_array):
        plt.subplot(2, 4, i + 1)
        plt.xticks([])
        plt.yticks([])
        plt.grid(False)
        plt.imshow(img, cmap='gray')
        plt.title("Image " + str(i), fontsize=20)
        plt.suptitle("Images", fontsize=70)
    plt.show()
    # plt.close()


def get_thresholds(images_array):
    # greyscaling the images as later functions accept only 2-D arrays
    gray_images = np.array([rgb2gray(img) for img in images_array])
    # graphing all images in array onto same figure
    graph_images(gray_images)
    # blurring the images through a gaussian filter to eliminates spikes,sigma changes how much it blurs
    # COULD USE DIFF TYPE HAVEN't TESTED THEM ALL YET
    blurred_gray_images = np.array([gaussian(img, sigma=2)
                                    for img in gray_images])
    # getting threshold value for each image using minimum method, as it works the cleanest in isolating the square
    # in the post-conversion images, compared to other threshold methods.
    # (can compare using 'try_all_threshold' function in skimage.filters)
    min_threshold = np.array([threshold_minimum(img)
                              for img in blurred_gray_images])
    return blurred_gray_images, min_threshold


def mask(images_array, binary_array):
    pass


def main():
    # loading up all image paths in a list using glob
    path = 'Primed_Conversion_efficiency_Images_test/Test File/*/*.tif'
    paths = glob.glob(path, recursive=True)
    # loading images as numpy arrays, all inside a numpy array
    images = np.array([io.imread(img, plugin='pil') for img in paths])

    blurred_gray_images, min_threshold = get_thresholds(images)

    # getting binary image delimiting rectangle by putting all values of rectangle-containing-image
    # either to True or False depending on comparison to threshold
    b_g_postpc_1 = blurred_gray_images[0] >= min_threshold[0]  # binary_green excitation_post photoconversion_1st pair

    # using binary array to mask all values external to rectangle
    for img in images:
        img[b_g_postpc_1] = 0  # values get set to black

    graph_images(images)

    '''
    Testing quantification methods with images in folder 4 (1st four images in image array)
    
    ! Not using rgb2gray for calculations as the greyscale doesn't equally transform green and red 
    (Y = 0.2125 R + 0.7154 G + 0.0721 B, from scikit image documentation)
    Converting to 0,1 range using img_to_float instead. (could also just keep in 0,255)
    '''
    # converting image values to float in 0,1 range with img_as_float
    img_floats = np.array([img_as_float(img) for img in images])
    # initializing lists for median/mean values
    green_medians = []
    green_means = []
    red_medians = []
    red_means = []
    means = []
    medians = []
    std_devs = []
    '''
    scipy.ndimage.median/mean function pretty useful bc it lets us choose areas to calculate in:
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
    '''
    for i, img in enumerate(img_floats):
        if i%2==0:
            green_medians.append(median(img[:,:,1], b_g_postpc_1, 0))
            green_means.append(mean(img[:,:,1], b_g_postpc_1, 0))
            medians.append(median(img[:,:,1], b_g_postpc_1, 0))
            means.append(mean(img[:,:,1], b_g_postpc_1, 0))
            std_devs.append(std(img[:,:,1], b_g_postpc_1, 0))
        else:
            red_medians.append(median(img[:,:,0], b_g_postpc_1, 0))
            red_means.append(mean(img[:,:,0], b_g_postpc_1, 0))
            medians.append(median(img[:,:,0], b_g_postpc_1, 0))
            means.append(mean(img[:,:,0], b_g_postpc_1, 0))
            std_devs.append(std(img[:,:,0], b_g_postpc_1, 0))

    #median values are close to identical to mean values, makes sense since proteins are evenly distributed in sample.
    # HAVEN'T TAKEN NOISE INTO ACCOUNT YET. could be done when we have images of plate, taking median of all values on
    # plate and substracting it from medians of sample areas. can also substract median absolute deviation

    # Normalizing 1st test - use mean of images in folder 4 and center pixels of folder 5 images around it
    # -> a start, vals seem better than non-normalized (see commented vals below)
    # 2nd test: - see if using std deviation makes values more understandable
    # -> red post-excitation vals have std_devs 10x larger than any other std_devs. makes mean post-conversion
    # red excitation intensity very small (~0.4) compared to green post and pre (2.5-2.8). red pre negative
    #3rd test: - try normalizing and shifting range to have all values positive
    # -> HAVEN'T TRIED YET
    normalized_means = []
    for i, img in enumerate(img_floats[4:]):
        # img = (img - means[i])/std_devs[i]
        img = (img - means[i])
        if i%2 ==0:
            normalized_means.append(mean(img[:,:,1], b_g_postpc_1, 0))
        else:
            normalized_means.append(mean(img[:,:,0], b_g_postpc_1, 0))

    # ratios of green_post/green_pre and green_post/red_post similar, good sign i think
    ratio_g_n = normalized_means[0]/normalized_means[2]  # = 0.8712845825803137
    ratio_post_r_n = normalized_means[0]/normalized_means[1]  # =0.789120575543297
    print("Ratio of change in green excitation post-conversion: " + str(ratio_g_n))
    print(" or a "+str(1-ratio_g_n)+" decrease in intensity")
    print("Ratio of intensity change between post-conversion green and red excitation: " + str(ratio_post_r_n))
    print(" or a "+str(1-ratio_post_r_n)+" difference in intensity")

    ratio_r_n = normalized_means[1]/normalized_means[3]  # = -15.353829343399187
    ratio_pre_n = normalized_means[3]/normalized_means[2]  # = -0.07191176575637018
    ratio_r_postn = normalized_means[1]/normalized_means[2]  # = 1.1041209792058053
    # values to compare normalized means to
    ratio_g = means[4]/means[6]  # = 0.8640487515575197
    ratio_r = means[5]/means[7]  # = 142.0985996824022
    ratio_pre = means[7]/means[6]  # = 0.013097348702334526
    ratio_post = means[5]/means[4]  # = 2.1539466457176744
    ratio_r_post = means[5]/means[6]  # = 1.8611149101538638



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
# b_g_postpc_2 = blurred_gray_images[4] >= min_threshold[4]
# b_r_postpc_1 = blurred_gray_images[1] <= min_threshold[1]
# b_r_postpc_2 = blurred_gray_images[5] <= min_threshold[5]
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



