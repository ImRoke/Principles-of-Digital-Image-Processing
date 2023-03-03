# importing required modules
import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

# reading and showing the image
img1 = cv.imread('gargantua.png')
img1 = cv.cvtColor(img1, cv.COLOR_BGR2RGB)
plt.imshow(img1)

# applying blur or average blur to image
img_blr = cv.blur(img1,(5,5))
#plt.imshow(img_blr)
#plt.title("Average Blurred Image")

# applying gaussian blur to image
img_gaus_blr = cv.GaussianBlur(img1,(5,5),0)
#plt.imshow(img_gaus_blr)
#plt.title("Gaussian Blurred Image")

