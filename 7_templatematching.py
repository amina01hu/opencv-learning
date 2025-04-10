import numpy as np
import cv2

#load both template image and base image

img = cv2.resize(cv2.imread('assets/soccer_practice.jpg', 0), (0, 0), fx=0.5, fy=0.5) #loading them in grayscale so it works with the algo
template = cv2.resize(cv2.imread('assets/shoe.PNG', 0), (0,0), fx=0.5, fy=0.5)
h, w = template.shape

methods = [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR,
            cv2.TM_CCORR_NORMED, cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]

# try with all methods and see what method matches the best

for method in methods:
    img2 = img.copy()
    
    result = cv2.matchTemplate(img2, template, method) # performing a convulusion, sliding over each area in the image to find the closest match
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        location = min_loc #based on the method min is the best location
    else:
        location = max_loc #based on the method max is the best location
    
    bottom_right = (location[0] + w, location[1] + h)
    cv2.rectangle(img2, location, bottom_right, 255, 5)
    cv2.imshow('Match', img2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()