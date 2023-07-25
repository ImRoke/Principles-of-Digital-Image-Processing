# Principles-of-Digital-Image-Processing
You are at the right place to start yearning the basic principles of the digital image processing are being explained through OpenCV and Python. 

## What actually a Digital Image?

A digital image is a 2D representation of visual objects or scenes that are stored in digital form, typically as a series of numerical values. These are made up of a grid of square or rectangular area of uniform tiny picture elements called pixels, each of which is assigned a color or grayscale based on the format it has been stored (like 8 bit, 16 bit etc). The resolution of an image is determined by the number of pixels in the grid. 

Before we delve into blurring, let's briefly discuss how images are represented in digital form. An image can be represented as a two-dimensional discrete function, where each pixel corresponds to a discrete point on the grid. We denote this function as **I(x, y)**, where **x** and **y** are the spatial coordinates.

The higher the resolution, the more pixels it has, and the more detail that can be displayed in the image. Digital images are widely used in many fields, including photography, design, medical imaging, astronomy, security, engineering, computer vision, autonomous vehicles and science, among others. 

So, here I'm displaying the pixel values on left side and the image on the right side for better understanding.

![alt text](https://github.com/ImRoke/Principles-of-Digital-Image-Processing/blob/main/DIP-Images/DIP2.png)

## Digital Image Processing (DIP)

DIP is a rapidly growing field and driven by the use of computer algorithms to enhance, restore and extract information from the images by using mathematical and computational techniques. Which includes linear algebra, calculus, probability theory, and machine learning. 

### Steps involved in DIP

The primary step will be the acquisition of image adn then analysis part comes into picture. Which includes the following steps:

  * Enhancement
    > Image will be enhanced by adjusting its brightness, contrast, or color balance and or by reducing noise or blurring.

  * Restoration
     > The degraded or distorted image can be brought back by removing artifacts, noise, and blur.

  * Segmentation
     > Here the image will be divided into particular regions or objects based on the user requirements such as color, shape or texture.

  * Compression
     > Image visual quality will be preserved by removing redundant or irrelevant informatoin while reducing the file size.
