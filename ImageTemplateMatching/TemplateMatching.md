# The Necessity of Template Matching Techniques in Computer Vision

Template matching is a computer vision technique used to find instances of a known pattern or a template (a small image) within a larger image. The comparison is usually done by calculating a similarity score between the template and the image patch at each location. It involves sliding the template over the target image and comparing pixel values to determine the similarity between the template and the image regions. Different methods are employed to measure this similarity, leading to various template matching techniques. The location with the highest similarity score is the most likely location of the template in the image. It is a versatile technique that can be used to find a variety of patterns in images. Template matching can be used to detect faces in images, to register images of the same scene taken from different viewpoints and to match features in fingerprints are some of the examples.

Following are the techniques used to find the similarities of image and template

## Correlation:

Correlation stands as one of the most frequently employed methods in template matching. It gauges the correlation coefficient between an image patch and a template, serving as a measure of their likeness. A higher correlation coefficient signifies greater similarity between the two images, while a lower value indicates dissimilarity.

The correlation coefficient between the image patch and the template is calculated as follows:


 $correlation = \frac{\sum_{x,y} (I_{x,y} \cdot T_{x,y})}{\sqrt{\sum_{x,y} (I_{x,y})^2} \cdot \sqrt{\sum_{x,y} (T_{x,y})^2}}$
 
where:
  - I(x, y) is the intensity at pixel (x,y) in the image
  - T(x, y) is the intensity at pixel (x,y) in the template
  - ∑(x, y) is the sum over all pixels in the image

## Normalized correlation:

Normalized correlation is a modified version of the correlation technique that normalizes the correlation coefficient using the standard deviations of both the image patch and the template. This adjustment enhances the resilience of the correlation coefficient against variations in illumination and contrast.

The normalized correlation coefficient between the image patch and the template is calculated as follows:


$correlation_normalized = \frac{\sum_{x,y} (I_{x,y} \cdot T_{x,y}) - \mu_I \cdot \mu_T}{\sqrt{\sum_{x,y} (I_{x,y} - \mu_I)^2} \cdot \sqrt{\sum_{x,y} (T_{x,y} - \mu_T)^2}}$

where:
  - I(x, y) is the intensity at pixel (x,y) in the image
  - T(x, y) is the intensity at pixel (x,y) in the template
  - ∑(x, y) is the sum over all pixels in the image


## Cross-correlation:

Another prevalent technique in template matching is cross-correlation. By computing the cross-correlation between an image patch and a template, this method quantifies how well the two images align. A higher cross-correlation value suggests good alignment, whereas a lower value implies misalignment.

The cross-correlation between the image patch and the template is calculated as follows:



 $cross_correlation = \sum_{x,y} (I_{x,y} \cdot T_{x-y,y})$

where:
  - I(x, y) is the intensity at pixel (x,y) in the image
  - T(x, y) is the intensity at pixel (x,y) in the template
  - ∑(x, y) is the sum over all pixels in the image


## Normalized cross-correlation:

Normalized cross-correlation is a variant of the cross-correlation approach that normalizes the cross-correlation by considering the standard deviations of the image patch and the template. This normalization step bolsters the cross-correlation coefficient's robustness when faced with alterations in illumination and contrast.

The normalized cross-correlation between the image patch and the template is calculated as follows:


$cross_correlation_normalized = \frac{\sum_{x,y} (I_{x,y} \cdot T_{x-y,y}) - \mu_I \cdot \mu_T}{\sqrt{\sum_{x,y} (I_{x,y} - \mu_I)^2} \cdot \sqrt{\sum_{x,y} (T_{x-y,y} - \mu_T)^2}}$

where:
  - I(x, y) is the intensity at pixel (x,y) in the image
  - T(x, y) is the intensity at pixel (x,y) in the template
  - ∑(x, y) is the sum over all pixels in the image



## Sum of squared differences:

A simpler method is the sum of squared differences, which involves calculating the cumulative sum of the squared disparities between an image patch and a template. This summation reflects the dissimilarity between the images. A higher sum of squared differences indicates greater dissimilarity, while a lower sum signifies higher similarity.

The sum of the squared differences between the image patch and the template is calculated as follows:



 $sum_of_squared_differences = \sum_{x,y} (I_{x,y} - T_{x,y})^2$

where:
  - I(x, y) is the intensity at pixel (x,y) in the image
  - T(x, y) is the intensity at pixel (x,y) in the template
  - ∑(x, y) is the sum over all pixels in the image


## Normalized sum of squared differences:

Normalized sum of squared differences is an adapted version of the sum of squared differences method that normalizes the cumulative sum by considering the squared intensities of the image patch. This normalization process makes the sum of squared differences coefficient more resistant to changes in illumination and contrast.

The normalized sum of the squared differences between the image patch and the template is calculated as follows:



$sum_of_squared_differences_normalized = \frac{\sum_{x,y} (I_{x,y} - T_{x,y})^2}{\sum_{x,y} (I_{x,y})^2}$

where:
  - I(x, y) is the intensity at pixel (x,y) in the image
  - T(x, y) is the intensity at pixel (x,y) in the template
  - ∑(x, y) is the sum over all pixels in the image

## Applications

* Object detection
* Image registration
* Feature matching
* Tracking
* Image alignment
* Pattern recognition
