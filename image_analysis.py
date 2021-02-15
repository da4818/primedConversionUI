import numpy as np

import matplotlib.pyplot as plt
from skimage.io import imread
from PIL import Image
from skimage.exposure import rescale_intensity
from skimage.filters import threshold_triangle, try_all_threshold
from skimage.morphology import remove_small_objects, remove_small_holes, skeletonize, closing, selem
from skimage.measure import label, regionprops
from skimage.color import label2rgb
from scipy import ndimage

imagename='OldFiles/test4.tif'

sample = Image.open(imagename)
sample.show()
pix = sample.load()
width,height = sample.size
photo = sample.convert("RGB")
totals = [0.0, 0.0, 0.0]
for y in range(sample.size[1]):
    for x in range(sample.size[0]):
        color = pix[x,y]
        for c in range(3):
            totals[c] += color[c] ** 2.2
count = sample.size[0] * sample.size[1]
color = tuple(int(round((totals[c] / count) ** (1/2.2))) for c in range(3))
R,G,B = color
print(R,G,B)
for x in range(width):
    for y in range(height):
        photo.putpixel((x,y),(R,G,B))
photo.show()

images =
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


