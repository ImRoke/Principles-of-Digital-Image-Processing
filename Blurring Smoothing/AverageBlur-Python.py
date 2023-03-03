import cv2
import numpy as np
import argparse

def custom_average_blur(image_path, kernel_size):
    # Read the image
    image = cv2.imread(image_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Define the kernel
    kernel = np.ones(kernel_size) / (kernel_size[0] * kernel_size[1])

    # Get the dimensions of the image
    h, w, c = image.shape

    # Initialize the blurred image
    blurred_image = np.zeros_like(image)

    # Apply the custom average blur using nested for-loops
    kh, kw = kernel_size
    for row in range(h - kh + 1):
        for col in range(w - kw + 1):
            for ch in range(c):
                blurred_image[row, col, ch] = np.sum(image[row:row + kh, col:col + kw, ch] * kernel)

    return blurred_image


if __name__ == '__main__':
    # Parse the command line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('image_path', type=str, help='path to the input image')
    parser.add_argument('kernel_size', type=int, nargs=2, help='kernel size for the custom average blur')
    args = parser.parse_args()

    # Apply the custom average blur to the input image
    blurred_image = custom_average_blur(args.image_path, tuple(args.kernel_size))

    # Show the blurred image
    cv2.imshow('Custom Average Blur', blurred_image)
    cv2.waitKey(0)

    
   
# This will apply a custom average blur with a kernel size of 5x5 to the image  
python custom_average_blur.py goku3.jpeg 5 5
   
