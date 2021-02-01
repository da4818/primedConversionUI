# from PIL import Image
# array type with lots of functions to help in analysis
import numpy as np
# matplotlib used to visualize what's happening with the images
import matplotlib.pyplot as plt
# loading image:
from skimage import io
# from skimage import image_as_float
# functions to blur and create mask:
from skimage.filters import gaussian, threshold_minimum
# greyscale conversion, not sure of the greyscale bit-depth but probably modulable:
from skimage.color import rgb2gray
# useful to do median of specific areas of image selectively:
from scipy.ndimage import median
# glob used to extract all filepaths from desired folder:
import glob


# Loading using io.imread loads image as numpy array. CAN LOAD THROUGH PIL AND
# CONVERT TO np ARRAY IF WE WANT TO KEEP USING PIL FUNCTIONS FOR LOADED IMAGES

# path = 'Primed_Conversion_efficiency_Images_test/Test File/4/pr-mEosFP new_pr-mEosFP_new_post-pc_4_1_green.tif'


# graphing all images in array onto same figure. amount of images is dynamic
# but arranged with 4 columns
def graph_images(images_array):
    plt.figure(figsize=(20,20)) #big size to see all images in good quality
    # plotting each image onto the figure, with possibility of title, axes, legend
    for i, img in enumerate(images_array):
        plt.subplot(4,4,i+1)
        plt.xticks([])
        plt.yticks([])
        plt.grid(False)
        plt.imshow(img, cmap='gray')
        plt.title("Image "+str(i+1), fontsize=20)
        plt.suptitle("Images", fontsize=70)
    plt.show()






def main():
    # loading up all image paths in a list using glob
    path = 'Primed_Conversion_efficiency_Images_test/Test File/*/*.tif'
    paths = glob.glob(path, recursive=True)
    # loading images as numpy arrays, all inside a numpy array
    images = np.array([io.imread(img) for img in paths])
    # greyscaling the images as future functions accept only 2-D arrays
    gray_images = np.array([rgb2gray(img) for img in images])

    # graphing all images in array onto same figure
    graph_images(gray_images)
    # blurring the images through a gaussian filter to eliminates spikes,sigma changes how much it blurs
    # COULD USE DIFF TYPE HAVEN't TESTED THEM ALL YET
    blurred_gray_images = np.array([gaussian(img, sigma=2)
                                    for img in gray_images])
    # getting threshold value for each image using minimum method,
    # as it turns out the cleanest in isolating the square
    # in the post-conversion images, compared to other threshold methods
    min_threshold = np.array([threshold_minimum(img)
                              for img in blurred_gray_images])

    # getting binary image delimiting rectangle by putting
    # all values either to True or False
    # depending on comparison to threshold
    b_g_postpc_1 = blurred_gray_images[0] <= min_threshold[0]
    b_g_postpc_2 = blurred_gray_images[4] <= min_threshold[4]
    # same but red excitation
    b_r_postpc_1 = blurred_gray_images[1] >= min_threshold[1]
    b_r_postpc_2 = blurred_gray_images[5] >= min_threshold[5]


    # CURRENTLY EACH IMAGE PAIR HAS ITS OWN MASK OF DIFF SIZE/SHAPE
    # WILL NEED TO EITHER TAKE SMALLEST OR AN AVERAGE TO HAVE SAME ONE
    # FOR EACH IMAGE

    # setting all values external to rectangle as 0 (black) to isolate
    # desired area
    images[0][~b_g_postpc_1] = 0
    # masking same area onto pre-conversion image for comparisons
    images[2][~b_g_postpc_1] = 0

    images[4][~b_g_postpc_1] = 0
    images[6][~b_g_postpc_1] = 0


    images[1][~b_r_postpc_1] = 0
    images[3][~b_r_postpc_1] = 0

    images[5][~b_r_postpc_2] = 0
    images[7][~b_r_postpc_2] = 0

    graph_images(images)

    # 1st image from pair of green excitation images in folder 4
    # (naming them just to keep track when trying out comparisons)
    # changing them to greyscale to work on intensity a bit easier





    g_pair_4_1 = rgb2gray(images[0])
    g_pair_4_2 = rgb2gray(images[2])

    # scipy.ndimage.median function pretty useful bc it lets us input
    # image(s) as arrays, labels - integer arrays that'll make the
    # function take into account only specific areas of image
    # and index - specify region labels (not too sure on what it does yet)
    pair_4_1 = median(input=g_pair_4_1, labels=b_g_postpc_1, index=None)
    pair_4_2 = median(g_pair_4_2, b_g_postpc_1)

    g_pair_4_ratio = 1 - pair_4_1/pair_4_2
    print("Ratio of change in green exciation post-conversion: "+str(g_pair_4_ratio), end='')
    print(" decrease in intensity")

    # HAVEN'T TAKEN NOISE INTO ACCOUNT YET
    # median_noise = np.median(g_pair_4_1[np.nonzero(g_pair_4_1)])




if __name__ == "__main__":
    main()
