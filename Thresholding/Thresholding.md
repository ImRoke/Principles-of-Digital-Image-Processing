# Thresholding Techniques

A common technique used to segment an image into regions of interest based on the pixel intensity values by converting a grayscale or color 
image into a binary image. Here the pixel values will be either black or white, depending on whether its intensity value is above or below a 
certain threshold value. Primarily used in object detection, image segmentation, and feature extraction. 


## Simple/Global Thresholding

Simplest and most commonlly used technique, involves selecting a threshold value that separates the pixels into two groups, foreground and background.
All the pixels above the threshold value are set to white, while all  the pixels below the threshold are set to black and vice versa. The choice of 
threshold value can be based on various methods, such as Otsu's binarization method or mean intensity value.


## Adaptive Thresholding

A global thresholding may not be suitable due to variations in illumination or contrast within the image because of different lighting conditions 
in different areas. So, this technique uses a local threshold value that varies depending on the surrounding pixel values. Useful when images with 
different lighting conditions are taking into consideration. 

## Otsu's Binarization

Otsu's method is a widely used technique for automatic thresholding and can be applied to a wide range of grayscale images. It is particularly useful for 
images with bimodal intensity distributions, where the foreground and background pixels have distinct intensity ranges. It is used to determine the threshold 
value automatically. The basic idea is to maximize the variance between the two classes of pixels in the binary image 
