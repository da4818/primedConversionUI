import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("pre_pr_red1.png")
#img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
colour_mask = cv2.imread("pre_pr_red1.png")
width=img.shape[0]


mask = np.zeros(img.shape[:2], np.uint8)
mask[200:201, 100:400] = 255

pixel_brightnesses = img[100:400,220]
pixel_locations = np.arange(100,400)


masked_img = cv2.bitwise_and(img,img, mask = mask)
colour_mask[200:201, 100:400] = (255,255,255)
plt.subplot(221), plt.imshow(img)
plt.subplot(222), plt.imshow(colour_mask)
#plt.subplot(222), plt.imshow(mask,'gray')
plt.subplot(223), plt.imshow(masked_img)
plt.subplot(224), plt.plot(pixel_locations,pixel_brightnesses)
plt.xlim([0,width])




plt.show()


'''for x in range(10):
    print(img.getpixel((x+100, 50)))
    img.putpixel((x+100, 50), (255, 255, 255))
#grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
plt.hist(img.ravel(),256,[0,256]); plt.show()'''

#hist, bins = np.histogram(img.ravel(),256,[0,256])
#hist = cv2.calcHist([img],[0],None,[256],[0,256])


'''image = Image.open("pre_pr_red1.png")
im = image.convert('L')
width, height = image.size
#image = skimage.io.imread(filename, as_gray=True)
print(width, height)

for x in range(10):
    print(im.getpixel((x+100, 50)))
    image.putpixel((x+100, 50), (255, 255, 255))
image.show()'''
