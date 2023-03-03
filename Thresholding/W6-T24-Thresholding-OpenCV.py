#!/usr/bin/env python
# coding: utf-8

# In[1]:


# importing the required modules
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


# In[2]:


# getting to know the available thresh methods in opencv
temp = [i for i in dir(cv) if i.startswith('THRESH')]
print("No of available templates are: {}".format(len(temp)))
print(temp)


# In[3]:


# reading a single channel image
img = cv.imread('goku.png',0)

# default binary threshold method
ret,bin_thresh = cv.threshold(img,63,255,cv.THRESH_BINARY)

# default binary inverse threshold method
ret,bin_ithresh = cv.threshold(img,63,255,cv.THRESH_BINARY_INV)

# default truncation threshold method
ret,trunc_thresh = cv.threshold(img,63,255,cv.THRESH_TRUNC)

# default threshold to zero method
ret,zero_thresh = cv.threshold(img,63,255,cv.THRESH_TOZERO)

# default threshold to zero inverse method
ret,zero_ithresh = cv.threshold(img,63,255,cv.THRESH_TOZERO_INV)

# plotting them for comparision
titles = ['Original Image','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
images = [img, bin_thresh, bin_ithresh, trunc_thresh, zero_thresh, zero_ithresh]

plt.figure(figsize=(25,10))

for i in range(6):
    plt.subplot(2,3,i+1)
    plt.imshow(images[i],'gray')
    plt.title(titles[i], fontsize = 20)
    plt.xticks([])
    plt.yticks([])
plt.show()


# In[4]:


# default adaptive threshold methods

amthresh1 = cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY,11,2)
agthresh2 = cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY,11,2)

# plotting the results
titles = ['Original Image', 'Adaptive Mean Thresholding', 'Adaptive Gaussian Thresholding']
images = [img, amthresh1, agthresh2]

plt.figure(figsize = (25,15))
for i in range(3):
    plt.subplot(1,3,i+1)
    plt.imshow(images[i],'gray')
    plt.title(titles[i], fontsize = 20)
    plt.xticks([]),plt.yticks([])
plt.show()


# In[ ]:


thresh = input('Enter an integer between 0 and 255 for Thresholding\n')


# **Binary Threshold**
# 
# **dst(x,y) = maxval if src(x,y) > thresh**
# 
# **dst(x,y) = 0       otherwise**

# In[ ]:


# Implementation of Custom Binary Threshold 

# 63 is used as a thershold for entire calculation

gray_img = cv.imread('goku.png', 0)

# iterating through the image dimensions
for i in range(gray_img.shape[0]):
    for j in range(gray_img.shape[1]):
        
        # comparing the pixel values to threshold
        # and then making them as bright pixel 
        # if not, then to a dark pixel
        if(gray_img[i,j] > 63):
            gray_img[i,j] = 255
        else:
            gray_img[i,j] = 0
    

# plotting the results in a grid
fig, axs = plt.subplots(2,2, figsize = (30,30))

plt.subplot(1,2,1)
plt.title('Default Binary Method', fontsize = 20)
plt.imshow(bin_thresh, 'gray')

plt.subplot(1,2,2)
plt.title('Custom Binary Threshold', fontsize = 20)
plt.imshow(gray_img, 'gray')


# **Binary Inverse**
# 
# **dst(x,y) = 0 if src(x,y) > thresh**
# 
# **dst(x,y) = maxval       otherwise**

# In[ ]:


# Implementation of custom Binary Inverse threshold

gray_img1 = cv.imread('goku.png', 0)

# iterating through the image dimensions
for i in range(gray_img1.shape[0]):
    for j in range(gray_img1.shape[1]):
        
        # comparing the pixel values to threshold
        # and then making them as dark pixel 
        # if not, then to a bright pixel
        if(gray_img1[i,j] > 63):
            gray_img1[i,j] = 0
        else:
            gray_img1[i,j] = 255

            
# plotting the results in a grid
fig, axs = plt.subplots(2,2, figsize = (30,30))

plt.subplot(1,2,1)
plt.title('Default Binary Inverse Method', fontsize = 20)
plt.imshow(bin_ithresh, 'gray')

plt.subplot(1,2,2)
plt.title('Custom Binary Inverse', fontsize = 20)
plt.imshow(gray_img1, 'gray')


# **Truncation**
# 
# **dst(x,y) = thresh if src(x,y) > thresh**
# 
# **dst(x,y) = src(x,y) otherwise**

# In[ ]:


# Implementation of Custom Truncation method

gray_img2 = cv.imread('goku.png', 0)

h, w = gray_img2.shape[0], gray_img2.shape[1]

# iterating through the image dimensions
for i in range(h):
    for j in range(w):
        
        # comparing the pixel values to threshold
        # and then making them equals to the threshold 
        # if not, then to a same original pixel value
        if(gray_img2[i,j] > 63):
            gray_img2[i,j] = 63
        else:
            gray_img2[i,j] = gray_img2[i,j]
    

# plotting the results in a grid
fig, axs = plt.subplots(2,2, figsize = (30,30))

plt.subplot(1,2,1)
plt.title('Default Truncation Method', fontsize = 20)
plt.imshow(trunc_thresh, 'gray')

plt.subplot(1,2,2)
plt.title('Custom Truncation', fontsize = 20)
plt.imshow(gray_img2, 'gray')


# **Threshold To Zero**
# 
# **dst(x,y) = src(x,y) if src(x,y) > thresh**
# 
# **dst(x,y) = 0 otherwise**

# In[ ]:


# Implementation of Custom Threshold To Zero

gray_img3 = cv.imread('goku.png', 0)

h, w = gray_img3.shape[0], gray_img3.shape[1]

# iterating through the image dimensions
for i in range(h):
    for j in range(w):
        
        # comparing the pixel values to threshold
        # and then making them equals to the same original pixel value 
        # if not, then to a dark pixel value
        if(gray_img3[i,j] > 63):
            gray_img3[i,j] = gray_img3[i,j]
        else:
            gray_img3[i,j] = 0
    


# plotting the results in a grid
fig, axs = plt.subplots(2,2, figsize = (30,30))

plt.subplot(1,2,1)
plt.title('Default TOZERO Method', fontsize = 20)
plt.imshow(zero_thresh, 'gray')

plt.subplot(1,2,2)
plt.title('TOZERO from Scratch', fontsize = 20)
plt.imshow(gray_img3, 'gray')


# **Threshold To Zero Inverse**
# 
# **dst(x,y) = 0 if src(x,y) > thresh**
# 
# **dst(x,y) = src(x,y) otherwise**

# In[ ]:


# Implementation of Threshold To Zero Inverse from scratch

gray_img4 = cv.imread('goku.png', 0)

h, w = gray_img4.shape[0], gray_img4.shape[1]

# iterating through the dimensions of image
for i in range(h):
    for j in range(w):
        
        # comparing the pixel values to threshold
        # and then making them equals to a dark pixel value 
        # if not, then to the same original pixel value
        if(gray_img4[i,j] > 63):
            gray_img4[i,j] = 0
        else:
            gray_img4[i,j] = gray_img4[i,j]
    

# plotting the results in a grid
fig, axs = plt.subplots(2,2, figsize = (30,30))

plt.subplot(1,2,1)
plt.title('Default TOZERO_INV Method', fontsize = 20)
plt.imshow(zero_ithresh, 'gray')

plt.subplot(1,2,2)
plt.title('Custom TOZERO_INV ', fontsize = 20)
plt.imshow(gray_img4, 'gray')


# **ADAPTIVE_THRESH_MEAN_C** 
# 
# **the threshold value T(x,y) is a mean of the blockSize×blockSize neighborhood of (x,y) minus C**

# In[43]:


# Implementation of ADAPTIVE_THRESH_MEAN_C from scratch

gray_img5 = cv.imread('goku.png', 0)
#gray_img5 = cv.cvtColor(gray_img5, cv.COLOR_BGR2GRAY)

h, w = gray_img5.shape[0], gray_img5.shape[1]

avg_kernel = np.ones((11,11), np.uint8)/121
kh, kw = avg_kernel.shape

dark_img5 = gray_img5.copy()
dark_img5[:, :] = 0

for col in range(w-kw+1):
#for row in range(h-kh+1):
    for row in range(h-kh+1):
    #for col in range(w-kw+1):
        
        dark_img5 = np.mean(np.sum(np.sum(gray_img5[row:row + kh, col:col + kw] * avg_kernel)))

        
        if(gray_img5[row, col] > ((dark_img5 - 2))):
            gray_img5[row, col] = 255
        else:
            gray_img5[row, col] = 0
    
    
#plt.imshow(cv.cvtColor(gray_img5, cv.COLOR_BGR2RGB))
#plt.show()

# plotting the results in a grid
fig, axs = plt.subplots(2,2, figsize = (30,30))

plt.subplot(1,2,1)
plt.title('Default ADAPTIVE_THRESH_MEAN_C Method', fontsize = 20)
plt.imshow(amthresh1, 'gray')

plt.subplot(1,2,2)
plt.title('ADAPTIVE_THRESH_MEAN_C from Scratch', fontsize = 20)
plt.imshow(gray_img5, 'gray')


# **ADAPTIVE_THRESH_GAUSSIAN_C**
# 
# **the threshold value T(x,y) is a weighted sum (cross-correlation with a Gaussian window) of the blockSize×blockSize neighborhood of (x,y) minus C**
# 
# **The default sigma (standard deviation) is used for the specified blockSize**

# In[31]:


# Implementation of ADAPTIVE_THRESH_GAUSSIAN_C from scratch


def gaus_kernel(filter_size, sigma):
    
    # required filter size 
    filter_size = int(filter_size) // 2
    
    # creating a blob with that filter size
    hgt, wdt = np.mgrid[-filter_size:filter_size+1, -filter_size:filter_size+1]
    
    # Using the Gaussian formula for computation
    gaus_const = 1 / (2.0 * np.pi * sigma**2)
    
    gauss =  np.exp(-((hgt**2 + wdt**2) / (2.0*sigma**2))) * gaus_const
    
    return gauss


# In[33]:


gray_img6 = cv.imread('goku.png',0)
#gray_img6 = cv.cvtColor(gray_img6, cv.COLOR_BGR2GRAY)

h, w = gray_img6.shape[0], gray_img6.shape[1]

kernel = gaus_kernel(11, 2)
kh, kw = kernel.shape

dark_img6 = gray_img6.copy()
dark_img6[:, :] = 0

for row in range(h-kh+1):
    for col in range(w-kw+1):
        
        dark_img6[row, col] = np.average(np.sum(np.sum(gray_img6[row:row + kh, col:col + kw] * kernel)))
        
        if(gray_img6[row, col] > (dark_img6[row, col] - 2)):
            gray_img6[row, col] = 255
        else:
            gray_img6[row, col] = 0 


# In[34]:


# plotting the results in a grid
fig, axs = plt.subplots(2,2, figsize = (30,30))

plt.subplot(1,2,1)
plt.title('Default ADAPTIVE_THRESH_GAUSSIAN_C Method', fontsize = 20)
plt.imshow(agthresh2, 'gray')

plt.subplot(1,2,2)
plt.title('ADAPTIVE_THRESH_GAUSSIAN_C from Scratch', fontsize = 20)
plt.imshow(gray_img6, 'gray')


# In[35]:




