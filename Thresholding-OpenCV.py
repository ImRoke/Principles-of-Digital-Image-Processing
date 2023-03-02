#!/usr/bin/env python
# coding: utf-8

# Required modules
import cv2
import numpy as np
from matplotlib import pyplot as plt


# To know the available thresholding (THRESH) methods in OpenCV
# tmp = [i for i in dir(cv2) if i.startswith('THRESH')]
# print(f"No of available templates are: {len(tmp)}")
# print(tmp)


# To read only a specified channel from the image, one can use 
# 0 - grayscale, 1 - color, -1 - unchanged in imread method
im = cv2.imread('goku3.jpeg', 0)

# Binary threshold method
ret, bthresh = cv2.threshold(im , 69, 255, cv2.THRESH_BINARY)

# Binary inverse threshold method
ret, bithresh = cv2.threshold(im, 69, 255, cv2.THRESH_BINARY_INV)

# Truncation threshold method
ret, tthresh = cv2.threshold(im, 69, 255, cv2.THRESH_TRUNC)

# Threshold to zero method
ret, zthresh = cv2.threshold(im, 69, 255, cv2.THRESH_TOZERO)

# Threshold to zero inverse method
ret, zithresh = cv2.threshold(im , 69, 255, cv2.THRESH_TOZERO_INV)

# Plotting 
names = ['Original','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
imgs = [img, bthresh, bithresh, tthresh, zthresh, zithresh]

plt.figure(figsize=(25,10))

for i in range(6):
    plt.subplot(2,3,i+1)
    plt.imshow(imgs[i],'gray')
    plt.title(names[i], fontsize = 20)
    plt.xticks([])
    plt.yticks([])
plt.show()


# Adaptive thresholding methods


# Adaptive Mean Thresholding
amthresh = cv.adaptiveThreshold(im, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 13, 2)

# Adaptive Gaussian Thresholding
agthresh = cv.adaptiveThreshold(im, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 13, 2)

# Plotting 
titles = ['Original', 'Adaptive Mean Threshold', 'Adaptive Gaussian Threshold']
images = [im, amthresh, agthresh]

plt.figure(figsize = (25,15))
for i in range(3):
    plt.subplot(1,3,i+1)
    plt.imshow(images[i],'gray')
    plt.title(titles[i], fontsize = 20)
    plt.xticks([]),plt.yticks([])
plt.show()
