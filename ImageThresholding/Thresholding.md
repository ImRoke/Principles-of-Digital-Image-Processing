# What is the need of Thresholding Techniques in DIP?

Image thresholding is a widely employed technique in digital image processing for segmenting an image into regions of interest based on pixel intensity values. It involves converting a grayscale or color image into a binary image, where pixels are either black or white, depending on whether their intensity value is above or below a specified threshold value. This powerful method finds extensive applications in object detection, image segmentation, and feature extraction tasks. By setting an appropriate threshold, specific objects or regions can be isolated from the background, aiding in the extraction of relevant information and facilitating further analysis. The simplicity and effectiveness of image thresholding make it a fundamental tool in various computer vision and image processing applications.


## Simple/Global Thresholding

Simplest and most commonlly used technique, involves selecting a threshold value that separates the pixels into two groups, foreground and background.
All the pixels above the threshold value are set to white, while all  the pixels below the threshold are set to black and vice versa. The choice of 
threshold value can be based on various methods, such as Otsu's binarization method or mean intensity value.

The binarized image B(x, y) is defined as follows:

The **Binary Threshold** of an image can be calculated using the below mentioned equations:

```
B(x, y) = { Max Value, if I(x, y) > T(x, y)
          { 0,         otherwise
```

The **Binary Inverse Threshold** of an image can be calculated using the below mentioned equations:

```
B(x, y) = { 0,          if I(x, y) > T(x, y)
          { Max Value,  otherwise

```

The **Truncated Threshold** of an image can be calculated using the below mentioned equations:

```
B(x, y) = { Threshold, if I(x, y) > Threshold
          { I(x, y),   otherwise
```

The **Truncated To Zero Threshold** of an image can be calculated using the below mentioned equations:

```
B(x, y) = { I(x, y), if I(x, y) > Threshold
          { 0,       otherwise

```

The **Truncated To Zero Inverse Threshold** of an image can be calculated using the below mentioned equations:

```
B(x, y) = { 0,         if I(x, y) > Threshold
          { I(x, y),   otherwise

```

## Adaptive Thresholding

A global thresholding may not be suitable due to variations in illumination or contrast within the image because of different lighting conditions 
in different areas. So, this technique uses a local threshold value that varies depending on the surrounding pixel values. Useful when images with 
different lighting conditions are taking into consideration. 

For adaptive thresholding, a window or neighborhood of size (w x w) is defined around each pixel (x, y). The threshold value T(x, y) for each pixel (x, y) is computed based on the pixel values within its local neighborhood. The binarized image B(x, y) is then obtained as:

```
B(x, y) = 0      if I(x, y) < T(x, y)
B(x, y) = 255    if I(x, y) ≥ T(x, y)
```

Mean Adaptive Threshold can be calculated as follows:

```
T(x, y) = mean(src(x - block_size/2 : x + block_size/2, y - block_size/2 : y + block_size/2)) - C

C is subtracted from the weighted sum to adjust the threshold level.

For Binary Threshold,

B(x, y) = { Max Value, if T(x, y) > 0
          { 0,         otherwise

For Binary Inverse Threshold,

B(x, y) = { 0,           if T(x, y) > 0
          { Max Value,   otherwise
```

Gaussian Adaptive Threshold can be calculated as follows:

```
T(x, y) = weighted_sum(src(x - block_size/2 : x + block_size/2, y - block_size/2 : y + block_size/2), Gaussian_window) - C

C is subtracted from the weighted sum to adjust the threshold level.

For Binary Threshold,

B(x, y) = { Max Value, if T(x, y) > 0
          { 0,         otherwise

For Binary  Inverse Threshold,

B(x, y) = { 0,           if T(x, y) > 0
          { Max Value,   otherwise
```

## Otsu's Binarization

Otsu's method is a widely used technique for automatic thresholding and can be applied to a wide range of grayscale images. It is particularly useful for 
images with bimodal intensity distributions, where the foreground and background pixels have distinct intensity ranges. It is used to determine the threshold 
value automatically. The basic idea is to maximize the variance between the two classes of pixels in the binary image.

Otsu's method involves computing the histogram of the image and calculating the probabilities of each intensity level. Then, the cumulative probabilities and mean intensity values are calculated to determine the optimal threshold value k. Otsu's method aims to find the optimal value of k that minimizes the weighted sum of within-class variance. 

Otsu's binarization involves several mathematical formulas to determine the optimal threshold value for automatic image thresholding. Here are the key mathematical equations used in Otsu's method:

### To Calculate Probability of Each Intensity Level:

The probability p(i) of each intensity level i (0 ≤ i ≤ 255) is calculated as the number of pixels with intensity i divided by the total number of pixels in the image:

```
p(i) = n(i) / N

Where,
      n(i) is the number of pixels with intensity i.
      N is the total number of pixels in the image.
```

### To Calculate Cumulative Probability:

The cumulative probability P(i) of each intensity level up to i is obtained by summing the probabilities from intensity 0 to i:

```
P(i) = ∑ p(j), for j from 0 to i
```

### To Calculate Mean Intensity Value:

The mean intensity value μ is calculated as the weighted sum of probabilities multiplied by their corresponding intensity values:

```
μ = ∑ (i * p(i)), for i from 0 to 255
```

### To Calculate Total Mean:

The total mean mT is the mean intensity value of the entire image and is equal to the weighted sum of probabilities for all intensity levels:

```
mT = ∑ (i * p(i)), for i from 0 to 255
```

### To Calculate Between-Class Variance:

The between-class variance σB^2 at each intensity level i is calculated as the square of the difference between the cumulative probability P(i) and 1 (total probability) multiplied by the cumulative probability P(i):

```
σB^2(i) = (P(i) * (1 - P(i)))^2 / P(i)
```

### To Calculate Optimal Threshold Value:

The optimal threshold value k is the one that maximizes the between-class variance σB^2(i) over all possible intensity levels:

```
k = argmax(σB^2(i)), for i from 0 to 255
```

Finally the binarized image B(x, y) is given by:

```
B(x, y) = 0      if I(x, y) < k
B(x, y) = 255    if I(x, y) ≥ k

```
