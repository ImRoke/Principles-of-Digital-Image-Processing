# What are color spaces?

A color space is a specific way of representing colors in a digital image, which is defined by a mathematical model that maps colors as perceived by the human eye to
a set of numerical values that can be stored and processed by a computer. Following are the some of the most used color spaces in current time:

## RGB (Red, Green, Blue):

  * RGB is more intuitive and closely related to the way that human vision perceives color.
  * The most used color space and represents color as a combination of red, green, and blue values.
  * Used in computer displays, cameras, and digital devices.
  * Red - (255, 0, 0), Green - (0, 255, 0), Blue - (0, 0, 255), White - (255, 255, 255), Black - (0, 0, 0)

R = BGR[..., 2]
G = BGR[..., 1]
B = BGR[..., 0]

RGB = (R, G, B)
    
![alt text](https://github.com/ImRoke/Principles-of-Digital-Image-Processing-with-OpenCV-Python/blob/main/DIP-Images/Color%20Spaces.png)

## GRAY Image:

The grayscale color space uses a single channel to represent an image, where each pixel value corresponds to its brightness. 

## CMYK (Cyan, Magenta, Yellow, Key/Black):

![alt text](https://learn.microsoft.com/en-us/windows/win32/wcs/images/cmyclrs1.png)

  * It is a substractive color model, which means colors are created by subtracting or absorbing certain wavelengths of light from white light.
  * Represents colors as a combination of Cyan, Magenta, Yellow, and Black values.
  * The colors are created by varying the amounts of ink or toner of each color - Cyan, Magenta, Yellow, and Black.
  * Cyan, Magenta, and Yellow are used to create a wide range of colors, but are not related to produce the deep, rich black color that is often desired.
  * Hence, it requires a separate black ink or toner is used, represented by the 'K' in CMYK, which stands for 'Key' because it is used as the key plate in the printing process.
  * Used to create the four-color printing process.
  * Primarly used in printing. However, because the color model in color inacuracies or variations between different printing methods or devices.

## HSV (Hue, Saturation, Value):

![alt text](https://learn.microsoft.com/en-us/windows/win32/wcs/images/hsvline.png)

 ### Hue:
 
  * The HSV color space plays a significant role in how humans perceive and distinguish colors. 
  * Hue is a color attribute that represents the pure color of an object or light source, as perceived by the human eye.
  * Hue represents color and can be calculated by knowing the color’s position on a color wheel.
  * Also represented as an angle around the color wheel. 
  
 
|  Color  |  Angle   |   
| --------|:--------:| 
| Red     | 0-60°    |
| Yellow  | 61-120°  | 
| Green   | 121-180° |
| Cyan    | 181-240° |
| Blue    | 241-300° |
| Magenta | 301-360° |

  
 ### Saturation:
 
  * Saturation refers to the intensity or purity of an image. As it increases, colors vary from unsaturated (shades of gray) to fully saturated (no white component).
  * Increasing saturation makes the image look more ambient and intense, while decreasing it can create a more muted or pastel effect.
  * These values are represented in percentages, with 100% saturation indicating the purest possible color, and 0% saturation indicating a completely desaturated color. Which is in the range [0 (gray), 1 (primary color)]. 
  * For example, this color space is often used by people who are selecting colors, such as paint or ink color, from a color wheel or palette.

### Value

  * Value refers to the brightness or lightness of an image.
  * Value often represented as percentage or a numerical value that indicates the brightness of a color, with 0% representing black and 100% representing white. 
  * Increasing the value of a color can make it appear lighter and brighter, while decreasing the value can make it appear darker and less intense. Which is in the range [0 (black), 1 (white)].
  * Used to create the four-color printing process and also used in graphic design, art and photography.


B, G, R = BGR[..., 0], BGR[..., 1], BGR[..., 2]

V = max(R, G, B)
S = (V - min(R, G, B)) / V if V != 0 else 0

diff = V - min(R, G, B)
R_diff = (V - R) / diff if diff != 0 else 0
G_diff = (V - G) / diff if diff != 0 else 0
B_diff = (V - B) / diff if diff != 0 else 0

H = 60 * (2 + B_diff - R_diff) if V == R else 60 * (4 + R_diff - G_diff) if V == G else 60 * (6 + G_diff - B_diff) if V == B else 0
H = H if H >= 0 else H + 360

HSV = (H, S, V) 

## YUV (Luma, Chrominance Blue, Chrominace Red):

  * The Y component represents the brightness of the image. Alone used to represent Black and White images or it provides the luminance information in color images. 
  * The U and V components represent the Chrominance or color information.
  * These U and V components are also known as the color difference signals because they represent the difference betweenn the image.
  * Mostly used in video compression formats, such as MPEG and H.264, because it allows for efficient compression of the color information by separating it from the luminance information. 


Y = 0.299 * R + 0.587 * G + 0.114 * B
U = (B - Y) * 0.492
V = (R - Y) * 0.877

YUV = (Y, U, V)

## YUV420 (YUVI420)

 * YUV420, also known as I420, is a widely used planar format in video compression.
 * It consists of three components: Y (luma), U (chrominance blue), and V (chrominance red).
 * The Y channel, responsible for brightness and visual content, is retained at full resolution, ensuring crucial image details.
 * In contrast, the U and V channels are subsampled, reducing data size while maintaining acceptable visual quality.
 * This color space is particularly advantageous for video compression due to the human visual system's sensitivity to changes in brightness (Y) rather than color (U and V).
 * By subsampling the chrominance components, video codecs achieve significant data compression, making it ideal for storage and transmission without perceptible loss in image quality.
 * It is essential to note that YUV420 primarily caters to video compression purposes and may not be commonly employed in general image processing tasks.
 * Its efficiency lies in efficiently representing video frames and reducing data, making it an excellent choice for video codecs.

First convert the BGR image to YUV using the YUV formulas from the above.

Then Subsample the U and V channels (every other pixel)
U = YUV[1][::2, ::2]
V = YUV[2][::2, ::2]

YUV420 = (Y, U, V)



Y = 0.299 * R + 0.587 * G + 0.114 * B
Cr = (R - Y) * 0.713 + 128
Cb = (B - Y) * 0.564 + 128

YCrCb = (Y, Cr, Cb)

