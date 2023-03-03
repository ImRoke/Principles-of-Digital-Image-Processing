import cv2
import numpy as np
import matplotlib.pyplot as plt

def gauss_kernel(filter_size, sigma=1):
    # required filter size 
    filter_size = int(filter_size) // 2

    # creating a blob with that filter size
    hgt, wdt = np.mgrid[-filter_size:filter_size+1, -filter_size:filter_size+1]

    # Using the Gaussian formula for computation
    gaus_const = 1 / (2.0 * np.pi * sigma**2)

    gauss = np.exp(-((hgt**2 + wdt**2) / (2.0*sigma**2))) * gaus_const

    return gauss

def custom_gaussian_blur(image, kernel_size, sigma):
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    h, w, c = image.shape

    kernel = gauss_kernel(kernel_size, sigma)
    kh, kw = kernel.shape

#     blurred_image = image.copy()
#     blurred_image[:, :, :] = 0

    # Initialize the blurred image
    blurred_image = np.zeros_like(image)

    for row in range(h-kh+1):
        for col in range(w-kw+1):
            for ch in range(c):
                blurred_image[row, col, ch] = np.sum(image[row:row + kh, col:col + kw, ch] * kernel)

    return blurred_image

if __name__ == '__main__':
    # Load input image
    image = cv2.imread('gargantua.png')

    # Apply custom Gaussian blur
    blurred_image = custom_gaussian_blur(image, kernel_size=5, sigma=1)

    # Display original and blurred images
    fig, ax = plt.subplots(1, 2, figsize=(10, 5))
    ax[0].imshow(image)
    ax[0].set_title('Original')
    ax[1].imshow(blurred_image)
    ax[1].set_title('Gaussian Blur')
    plt.show()
    
    
    # Parse the command line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('image_path', type=str, help='path to the input image')
    parser.add_argument('kernel_size', type=int, nargs=2, help='kernel size for the custom gaussian blur')
    parser.add_argument('sigma', type=int, nargs=1, help='sigma value for the gaussian')
    args = parser.parse_args()

    # Apply the custom gaussian blur to the input image
    blurred_image = custom_gaussian_blur(args.image_path, tuple(args.kernel_size), tuple(args.sigma))

    # Show the blurred image
    cv2.imshow('Custom Gaussian Blur', blurred_image)
    cv2.waitKey(0)

    
   
# This will apply a custom gaussian blur with a kernel size of 5x5 to the image  
python custom_gaussian_blur.py goku3.jpeg 5 5 1
