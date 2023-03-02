
import cv2

# Reading an image by giving the exact file name
# You can also read stored image in system by giving the address like 'C:/Users/username/...'
im = cv2.imread('goku3.jpeg')

# Using '.shape' method, we will get to know the height, width and channels of the image
h, w, ch = im.shape
dims = im.shape

print(f"Height of the Image: {h}")
print(f"Width of the Image: {w}")
print(f"No of Channels : {ch}")
print(f"Dimensions of the Image: {dims}")

# Showing the image from the default commands of opencv
cv2.imshow('GOKU-Supersaiyan-3', im)

# Image will be shown for infinity time
cv2.waitKey(0)
