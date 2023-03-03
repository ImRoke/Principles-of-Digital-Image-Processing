# What are color spaces?

A color space is a specific way of representing colors in a digital image, which is defined by a mathematical model that maps colors as perceived by the human eye to
a set of numerical values that can be stored and processed by a computer. Following are the some of the most used color spaces in current time:

## RGB (Red, Green, Blue):

  * The most used color space and represents color as a combination of red, green, and blue values.
  * Used in computer displays, cameras, and digital devices.
  * Red - (255, 0, 0), Green - (0, 255, 0), Blue - (0, 0, 255), White - (255, 255, 255), Black - (0, 0, 0)
    
![alt text](https://github.com/ImRoke/Principles-of-Digital-Image-Processing-with-OpenCV-Python/blob/main/DIP-Images/Color%20Spaces.png)


## CMYK (Cyan, Magenta, Yellow, Key/Black):

  * Represents colors as a combination of Cyan, Magenta, Yellow, and Black values.
  * Used to create the four-color printing process.
  * Primarly used in printing.

## HSV (Hue, Saturation, Value):
 
 ### Hue:
 
  * The HSV color space plays a significant role in how humans perceive and distinguish colors. 
  * Hue is a color attribute that represents the pure color of an object or light source, as perceived by the human eye.
  * Hue represents color and can be calculated by knowing the color’s position on a color wheel.
  * Also represented as an angle around the color wheel. 
  ![alt text](https://learn.microsoft.com/en-us/windows/win32/wcs/images/hsvline.png)
 
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
