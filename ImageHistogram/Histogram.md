# Why do we need Histogram and Histogram Equalization techniques?

In the realm of digital image processing, understanding and improving image characteristics are vital for a wide range of applications. By analyzing the 
distribution of pixel intensities using histograms, we gain valuable insights into an image's properties. Here, we will explore the significance 
of histograms in providing valuable pixel intensity information, enabling us to identify under or over-exposed regions and assess the dynamic range of an image. 
We will delve into contrast enhancement techniques, such as histogram equalization, which skillfully redistributes intensity values to unveil hidden details and 
elevate the visual appeal of images. Additionally, we will explore brightness adjustment, a key process in adapting images to varying lighting conditions. In the 
domain of medical image processing, these techniques hold paramount importance, enhancing medical images and facilitating more accurate diagnosis and 
treatment planning. Furthermore, it provides a comprehensive understanding of these versatile image enhancement tools and their diverse applications, encompassing computer 
vision, remote sensing, and various other image-related disciplines.


## Histogram:

A histogram provides an overall idea about the intensity distribution of an image. It is a graphical representation of data that organizes pixel intensity values 
into a set of predefined bins. Each bin represents a range of pixel intensity values, and the height of the bin corresponds to the frequency or count of pixels 
falling within that intensity range.

Histograms are useful for understanding various characteristics of an image, such as contrast and brightness. Contrast, in particular, is a measure of the difference 
in brightness between light and dark areas in a scene. By examining the histogram of an image, one can gain intuition about its contrast, brightness, intensity 
distribution, and identify any over-exposed or under-exposed regions.

In the context of image processing, histograms are often calculated by counting the occurrences of pixel intensity values between 0 and 255 (for 8-bit images). 
These values are then plotted in 256 bins, each corresponding to a specific intensity value from 0 to 255.

## Histogram Equalization:

Histogram equalization is a technique used to improve the contrast in an image by stretching out the intensity range. The goal is to distribute the pixel intensity 
values more uniformly across the entire range of possible values (0 to 255 for 8-bit images), thereby enhancing the visual appearance of the image. The result of 
histogram equalization is an image with improved contrast, where previously under-populated areas are stretched to become more distinguishable. By performing 
histogram equalization, images with poor contrast can be enhanced to reveal more details and improve visual quality.

### The histogram equalization process involves the following steps:

* Obtain the histogram of the input image, representing the frequency of each pixel intensity value.
* Compute the cumulative distribution function (CDF) of the pixel values based on the histogram.
* Normalize the CDF values to a range of 0 to 255, representing the new intensity values.
* Map the original pixel intensity values of the input image to their corresponding normalized values.
* Obtain the equalized image, where the intensity values are spread more evenly across the entire range.


The transformation function for histogram equalization is given by:

```
g(i) = round((cdf(i) - cdf_min) * (L - 1) / (M * N - cdf_min))

where,
      g(i) is the transformed intensity value.
      cdf(i) is the cumulative distribution function of the original image.
      L is the number of intensity levels (256 for 8-bit images).
      M is the number of rows in the image.
      N is the number of columns in the image.
      cdf_min is the minimum non-zero cumulative distribution function value.
```

The cumulative distribution function (CDF) is calculated as the sum of the histogram values up to the current intensity value i. In other words, the CDF at
intensity value i is the sum of all histogram values from 0 to i and can be represented as follows:

```
cdf(i) = ∑ h(j), for j from 0 to i
```

**Note:** While histogram equalization can enhance images with low contrast, it may not always produce desired results, especially when there are extreme 
variations in pixel intensity values or when the image contains important localized features. In such cases, other advanced contrast enhancement techniques may 
be more appropriate.
