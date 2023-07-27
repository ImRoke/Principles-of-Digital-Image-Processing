# Why do we need Image Manipulation Techniques?
Image processing is a captivating field that empowers us to manipulate images in diverse ways, from basic operations like addition to more intricate blending and 
bitwise manipulations. The fundamental image manipulation techniques namely image addition, image blending, and bitwise operations are mostly used in image 
processing and computer vision. Understanding these techniques expands our capabilities in image manipulation, opening doors to a myriad of creative possibilities 
and practical applications in various fields. 



## Image Addition
Image addition involves the merging of two images of the same size by adding their corresponding pixel values to create a new image. This operation can only be 
performed on images with the same dimensions, as it involves pairing up the pixel values at each location (x, y) in both images and computing their sum to 
determine the corresponding pixel value in the resulting image. Image addition finds numerous applications, such as image superimposing, creating image masks, 
and merging images with transparency. One crucial consideration when performing image addition is to ensure that the resulting pixel values remain within the 
valid range (e.g., 0 to 255 for 8-bit images) to prevent overflow or underflow issues.

Mathematically, given two images A and B, with pixel values A(x, y) and B(x, y) at location (x, y), the result image C will have pixel value as below:
```
C(x, y) = A(x, y) + B(x, y).
```



## Image Subtraction

Image subtraction involves subtracting the corresponding pixel values of two images to create a new image. Like image addition, this operation is also performed on 
images with the same dimensions. At each location (x, y), the pixel value of the resulting image is obtained by subtracting the pixel value of image B from the 
corresponding pixel value of image A. Image subtraction can be useful for tasks like identifying differences between two images, creating difference masks, or 
removing background elements from images. One crucial consideration when performing image subtraction is to ensure that the resulting pixel values remain within the 
valid range (e.g., 0 to 255 for 8-bit images) to prevent overflow or underflow issues.

Mathematically, given two images A and B, with pixel values A(x, y) and B(x, y) at location (x, y), the result image D will have pixel value as below:
```
D(x, y) = A(x, y) - B(x, y).
```



## Image Multiplication

Image multiplication, also known as element-wise multiplication, involves multiplying the corresponding pixel values of two images to create a new image. As with 
image addition and subtraction, image multiplication is performed on images with the same dimensions. At each location (x, y), the pixel value of the resulting 
image is obtained by multiplying the pixel value of image A with the corresponding pixel value of image B. One crucial consideration when performing image 
multiplicaion is to ensure that the resulting pixel values remain within the valid range (e.g., 0 to 255 for 8-bit images) to prevent overflow or underflow issues.
Image multiplication can be useful for various applications, such as creating image masks, emphasizing certain features, and adjusting the contrast of images.

Mathematically, given two images A and B, with pixel values A(x, y) and B(x, y) at location (x, y), the result image M will have pixel value as below:
```
M(x, y) = A(x, y) * B(x, y).
```

**NOTE:** Additionally, depending on the application, pixel values can be further normalized or adjusted necessarily to achieve the desired results.



## Image Blending
Image blending is an advanced technique that aims to seamlessly combine two images by applying blending weights to each pixel before adding them together. These 
blending weights, commonly represented by the alpha value, control the contribution of each image to the final result. Image blending finds applications in creating 
fade-in/fade-out effects, cross-dissolve transitions, and image overlays with adjustable transparency, enabling artists and developers to craft visually captivating 
compositions.

Mathematically, given two images A and B with pixel values A(x, y) and B(x, y) at location (x, y), and the blending weight alpha, the result image C will have 
pixel value as follows:
```
C(x, y) = (1 - α) * A(x, y) + α * B(x, y).

D(x, y) = α * image1 + β * image2 + γ

where,
  changing α leads to smooth transition and manipulating the β including α gives us a blending effect.
  γ = 0
```
The alpha value ranges from 0 to 1, determining the degree of influence each image has on the final blend. Values between 0 and 1 will produce a smooth combination 
of the two images, allowing for visually appealing transitions and effects.



## Bitwise Operations
Bitwise operations are low-level manipulations that operate on individual bits of pixel values in images. In these operations, pixel values are treated as binary 
numbers, and computations are performed bit by bit. These are commonly employed in image processing for tasks like masking, extracting specific regions, and 
manipulating individual bits in pixel values. Bitwise operations are particularly useful for manipulating binary masks, extracting regions of interest, and 
performing intricate pixel-level manipulations.

The primary bitwise operations are as follows:

  * Bitwise AND:
      > This operation operates on two input images and produces an output image in which each bit is set to 1 only if both corresponding bits in the input 
images are 1. Otherwise, the output bit is set to 0.

  * Bitwise OR:
      > This operation operates on two input images and results in an output image where each bit is set to 1 if either of the corresponding bits in the input
images is 1. If both bits are 0, the output bit will also be 0.

  * Bitwise XOR (Exclusive OR):
      > This operation operates on two input images and generates an output image in which each bit is set to 1 only if the corresponding bits in the input images
differ (one bit is 1, and the other is 0). If both bits are the same (both 0 or both 1), the output bit will be set to 0.

  * Bitwise NOT:
      > This operation is performed on a single input image and inverts each bit of the pixel values, changing 0s to 1s and 1s to 0s. In other words, it produces the bitwise
negation of the input image.


