# What is Edge Detection in Image Processing and Why do we use?

Edge detection is a technique used in image processing to determine the boundaries (edges) of objects or areas inside an image. Edges are one of the most important aspects of photographs. Edge detection allows users to examine picture features for substantial changes in grey level. It decreases the quantity of data in a picture while preserving its structural features. An edge is a large local shift in picture intensity that is frequently linked with a discontinuity in either the image intensity or the first derivative (gradient). 

These image intensity discontinuities can be either due to step discontinuities or line discontinuity. Step discontinuities occur when the picture intensity quickly shifts from one value on one side of the discontinuity to a different value on the opposite side of the discontinuity. Line discontinuities occur when the visual intensity quickly changes but returns to its initial value after a short distance. However, step and line borders are uncommon in real-world photographs. Sharp discontinuities in actual signals are uncommon due to low-frequency components or smoothing introduced by most sensing equipment. Step edges become ramp edges, and line edges become roof edges if intensity changes occur over a limited distance rather than instantaneously. Edge detection is a powerful tool for image processing. It can be used for a variety of tasks, such as object detection, image segmentation, and feature extraction etc.


There are two main types of edge detection algorithms such as gradient-based and Gaussian-based.

## Gradient-based Edge detection:

This algorithm computes the first derivative of the image and look for points where the derivative is large. This type of algorithm is relatively simple to implement, but it can be sensitive to noise.

### The Sobel operator:

A simple and efficient gradient-based edge detection algorithm. It uses two 3x3 kernels to compute the vertical and horizontal derivatives of the image. The magnitude of the gradient is then used to determine the edges. The Sobel operator is a 3x3 kernel that is used to compute the horizontal and vertical derivatives of an image.

```math
\quad\text{SobelX = }
\begin{bmatrix}
{-1} & 0 & {1} \\
{-2} & 0 & {2} \\
{-1} & 0 & {1}
\end{bmatrix}
,
\quad\text{SobelY = }
\begin{bmatrix}
{-1} & {-2} & {-1} \\
0 & 0 & 0 \\
{1} & {2} & {1}
\end{bmatrix}
```

### The Prewitt operator:

A similar to the Sobel operator, but it uses different kernels. The Prewitt operator is slightly less sensitive to noise than the Sobel operator, but it is also slightly less accurate. The Prewitt operator is similar to the Sobel operator, but it uses different kernels.

```math
\quad\text{PrewittX = }
\begin{bmatrix}
{-1} & 0 & {1} \\
{-1} & 0 & {1} \\
{-1} & 0 & {1}
\end{bmatrix}
,
\quad\text{PrewittY = }
\begin{bmatrix}
{-1} & {-1} & {-1} \\
0 & 0 & 0 \\
{1} & {1} & {1}
\end{bmatrix}
```

### The Robert Operator:

The Robert operators are a pair of 2x2 kernels that are used to detect edges in both the horizontal and vertical directions. The Robert X kernel is used to detect horizontal edges, while the Robert Y kernel is used to detect vertical edges.

```math
\quad\text{RobertX = }
\begin{bmatrix}
1 & 0 \\
0 & {-1}
\end{bmatrix}
,
\quad\text{RobertY = }
\begin{bmatrix}
0 & 1 \\
{-1} & 0   
\end{bmatrix}
```

The values of the kernels are multiplied by the corresponding pixel values in the image, and the results are summed. The sum of the products is then used to determine the magnitude of the gradient at that point. The magnitude of the gradient is a measure of the intensity of the edge at that point. The higher the magnitude of the gradient, the stronger the edge.

## Gaussian-based Edge detection

This algorithm first smooths the image with a Gaussian filter to reduce noise. Then, they compute the second derivative of the smoothed image and look for points where the second derivative is zero. This type of algorithm is more robust to noise than gradient-based algorithms, but it is also more computationally expensive.

### The Laplacian Operator:

The Laplacian operator is a 3x3 kernel that is used to detect edges. It is a second-order derivative operator, which means that it is sensitive to both the magnitude and direction of the gradient.

```math
\quad\text{Laplacian Operator = }
\begin{bmatrix}
0 & 1 & 0 \\
1 & -4 & 1 \\
0 & 1 & 0
\end{bmatrix}
```

### The Canny edge detector:

A more sophisticated edge detection algorithm that uses a combination of gradient-based and Gaussian-based techniques. The Canny edge detector is more robust to noise than the Sobel or Prewitt operators, and it also produces more accurate results because of noise resilience. While it offers numerous benefits, understanding its limitations is essential when applying it to different scenarios. Which possesses proper parameter tuning and can be resource sensitive to computational demands. This method comprises several stages, each contributing to its robustness and accuracy:

1. **Gaussian blurring**:
To reduce noise influence, the initial step involves smoothing the image with a Gaussian filter.

```math
\quad\text{Gaussian kernel }
\begin{equation}
G(x, y) = \frac{1}{2 \pi \sigma^2} \exp \left( -\frac{(x^2 + y^2)}{2 \sigma^2} \right)
\end{equation}
```

2. **Gradient calculation**:
Derivatives are computed along both horizontal and vertical directions to determine the image's gradient.

```math
\begin{align*}
Gx(x, y) &= -(G(x - 1, y) - 2 \cdot G(x, y) + G(x + 1, y)) \\ \\
Gy(x, y) &= -(G(x, y - 1) - 2 \cdot G(x, y) + G(x, y + 1)) \\ \\

magnitude(x, y) &= \sqrt{Gx(x, y)^2 + Gy(x, y)^2} \\ \\
direction(x, y) &= \tan^{-1} \left( \frac{Gy(x, y)}{Gx(x, y)} \right)
\end{align*}
```

3. **Non-maximum suppression**: This step eliminates unwanted edges by comparing pixel gradient magnitudes with those of neighboring pixels. If a pixel's gradient magnitude isn't the highest among its neighbors, it's suppressed.
```
if mag(x, y) > high_threshold:
    nms = True
elif mag(x, y) > low_threshold:
    nms = True if (mag(x - 1, y) <= mag(x, y) and
                    mag(x + 1, y) <= mag(x, y) and
                    mag(x, y - 1) <= mag(x, y) and
                    mag(x, y + 1) <= mag(x, y)) else False
else:
    nms = False
```
4. **Hysteresis thresholding**: Weak edges are connected to strong ones through hysteresis thresholding. By setting high and low thresholds, strong edges are those surpassing the high threshold, while weak edges fall between the two thresholds. Weak edges are retained only if they connect to strong edges.
```
if nms:
    edges.append((x, y))
```

## Applications:

* It can be used to identify objects in an image.
* It can be used to segment an image into different regions.
* It can be used to extract features from an image.
* It can be used to improve the quality of an image.
