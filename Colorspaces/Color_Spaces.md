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
 
  * The HSV color space plays a significant role in how humans perceive and distinguish colors. 
  * Hue is a color attribute that represents the pure color of an object or light source, as perceived by the human eye.
  * Hue represents color and can be calculated by knowing the color’s position on a color wheel, which is in the range of [0, 1]. Both 0 and 1 indicates red color.
  * Also represented as an angle around the color wheel, with Red at 0°, Green at 120°, and Blue at 240°. Other colors fall between these points, with Yellow at 60°, Cyan at 180°, and Magenta at 300°. 
  *
  * Saturation (S), which is the amount of hue or departure from neutral. S is in the range [0, 1]. As S increases, colors vary from unsaturated (shades of gray) to fully saturated (no white component).
  * For example, this color space is often used by people who are selecting colors, such as paint or ink color, from a color wheel or palette.

Attribute Description H .  V Value, which is the maximum value among the red, green, and blue components of a specific color. V is in the range [0, 1]. As V increases, the corresponding colors become increasingly brighter.
  * Used to create the four-color printing process.
  * Primarly used in printing.
