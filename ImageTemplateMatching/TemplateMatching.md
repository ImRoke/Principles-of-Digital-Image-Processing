# The Necessity of Template Matching Techniques in Computer Vision

Template matching is a computer vision technique used to find instances of a known pattern or a template (a small image) within a larger image. The comparison is usually done by calculating a similarity score between the template and the image patch at each location. It involves sliding the template over the target image and comparing pixel values to determine the similarity between the template and the image regions. Different methods are employed to measure this similarity, leading to various template matching techniques. The location with the highest similarity score is the most likely location of the template in the image. It is a versatile technique that can be used to find a variety of patterns in images. Template matching can be used to detect faces in images, to register images of the same scene taken from different viewpoints and to match features in fingerprints are some of the examples.

Following are the techniques used to find the similarities of image and template

## Correlation:

The correlation coefficient between the image patch and the template is calculated as follows:



 $$ correlation = \frac{\sum_{x,y} (I_{x,y} \cdot T_{x,y})}{\sqrt{\sum_{x,y} (I_{x,y})^2} \cdot \sqrt{\sum_{x,y} (T_{x,y})^2}} $$

where:
  - I(x, y) is the intensity at pixel (x,y) in the image
  - T(x, y) is the intensity at pixel (x,y) in the template
  - ∑(x, y) is the sum over all pixels in the image

## Normalized correlation:

The normalized correlation coefficient between the image patch and the template is calculated as follows:



$  correlation_normalized = \frac{\sum_{x,y} (I_{x,y} \cdot T_{x,y}) - \mu_I \cdot \mu_T}{\sqrt{\sum_{x,y} (I_{x,y} - \mu_I)^2} \cdot \sqrt{\sum_{x,y} (T_{x,y} - \mu_T)^2}} $

where:
  - I(x, y) is the intensity at pixel (x,y) in the image
  - T(x, y) is the intensity at pixel (x,y) in the template
  - ∑(x, y) is the sum over all pixels in the image


## Cross-correlation:

The cross-correlation between the image patch and the template is calculated as follows:



 $ cross_correlation = \sum_{x,y} (I_{x,y} \cdot T_{x-y,y}) $

where:
  - I(x, y) is the intensity at pixel (x,y) in the image
  - T(x, y) is the intensity at pixel (x,y) in the template
  - ∑(x, y) is the sum over all pixels in the image


## Normalized cross-correlation:

The normalized cross-correlation between the image patch and the template is calculated as follows:



$ cross_correlation_normalized = \frac{\sum_{x,y} (I_{x,y} \cdot T_{x-y,y}) - \mu_I \cdot \mu_T}{\sqrt{\sum_{x,y} (I_{x,y} - \mu_I)^2} \cdot \sqrt{\sum_{x,y} (T_{x-y,y} - \mu_T)^2}} $

where:
  - I(x, y) is the intensity at pixel (x,y) in the image
  - T(x, y) is the intensity at pixel (x,y) in the template
  - ∑(x, y) is the sum over all pixels in the image



## Sum of squared differences:

The sum of the squared differences between the image patch and the template is calculated as follows:



 $ sum_of_squared_differences = \sum_{x,y} (I_{x,y} - T_{x,y})^2  $

where:
  - I(x, y) is the intensity at pixel (x,y) in the image
  - T(x, y) is the intensity at pixel (x,y) in the template
  - ∑(x, y) is the sum over all pixels in the image


## Normalized sum of squared differences:

The normalized sum of the squared differences between the image patch and the template is calculated as follows:



$ sum_of_squared_differences_normalized = \frac{\sum_{x,y} (I_{x,y} - T_{x,y})^2}{\sum_{x,y} (I_{x,y})^2} $

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
