import cv2
from collections import Counter

#Analyses image to find shapes, then finds centre of each shape
'''
I will use this to generate a brightness profile of each row -
By finding the middle of each circle there will be a common value for the y coordinate, which can be used for the profile
'''
def find_centres(filename):
    img = cv2.imread(filename, 0)
    out = img.copy()

    contours, hierarchy = cv2.findContours(out, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)
    #cv2.CHAIN_APPROX_TC89_L1
    #print(len(contours))
    centres = []
    for i in range(len(contours)):
        moments = cv2.moments(contours[i])
        centres.append((int(moments['m10']/moments['m00']), int(moments['m01']/moments['m00'])))
        cv2.circle(img, centres[-1], 3, (0, 0, 0), -1)
    #print(centres)
    coords = list(zip(*centres))
    y_coords = []
    c = Counter(coords[1])
    for i in c.items():
        if i[1]>1:
            y_coords.append(i[0])
   # print(y_coords)
    #cv2.imshow('image', img)
    #cv2.waitKey(0)
    return y_coords

'''if __name__ == "__main__":
    find_centres()'''





