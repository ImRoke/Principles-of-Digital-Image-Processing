import cv2
import numpy as np
import matplotlib.pyplot as plt
import argparse

class CustomBlur:
    def __init__(self, image_path):
        self.image_path = image_path
        self.image = cv2.imread(image_path)

    def show_image(self, title="Image"):
        plt.imshow(cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB))
        plt.title(title)
        plt.axis('off')
        plt.show()

    def apply_blur(self, blur_type, **kwargs):
        if blur_type == 'median':
            self.custom_median_blur(**kwargs)
        elif blur_type == 'gaussian':
            self.custom_gaussian_blur(**kwargs)
        elif blur_type == 'average':
            self.custom_average_blur(**kwargs)
        elif blur_type == 'bilateral':
            self.custom_bilateral_blur(**kwargs)

    def custom_median_blur(self, kernel_size=3):
        
        pad = kernel_size // 2
        height, width, channels = self.image.shape
        result = np.zeros_like(self.image)

        for i in range(pad, height - pad):
            for j in range(pad, width - pad):
                for k in range(channels):
                    window = self.image[i - pad : i + pad + 1, j - pad : j + pad + 1, k]
                    result[i, j, k] = np.median(window)

        self.image = result

    def custom_gaussian_blur(self, kernel_size=(5, 5), sigma=(1.0, 1.0)):
        
        pad_x = kernel_size[0] // 2
        pad_y = kernel_size[1] // 2
        height, width, channels = self.image.shape
        result = np.zeros_like(self.image)

        for i in range(pad_x, height - pad_x):
            for j in range(pad_y, width - pad_y):
                for k in range(channels):
                    window = self.image[i - pad_x : i + pad_x + 1, j - pad_y : j + pad_y + 1, k]
                    kernel_x = np.exp(-np.linspace(-pad_x, pad_x, kernel_size[0])**2 / (2 * sigma[0]**2))
                    kernel_y = np.exp(-np.linspace(-pad_y, pad_y, kernel_size[1])**2 / (2 * sigma[1]**2))
                    kernel = np.outer(kernel_x, kernel_y)
                    result[i, j, k] = np.sum(window * kernel) / np.sum(kernel)

        self.image = result

    def custom_average_blur(self, kernel_size=(5, 5)):
       
        pad_x = kernel_size[0] // 2
        pad_y = kernel_size[1] // 2
        height, width, channels = self.image.shape
        result = np.zeros_like(self.image)

        for i in range(pad_x, height - pad_x):
            for j in range(pad_y, width - pad_y):
                for k in range(channels):
                    window = self.image[i - pad_x : i + pad_x + 1, j - pad_y : j + pad_y + 1, k]
                    result[i, j, k] = np.mean(window)

        self.image = result

    def custom_bilateral_blur(self, d=9, sigmaColor=75, sigmaSpace=75):
        
        pad = d // 2
        height, width, channels = self.image.shape
        result = np.zeros_like(self.image)

        for i in range(height):
            for j in range(width):
                for k in range(channels):
                    w = 0
                    val = 0

                    for p in range(max(0, i - pad), min(height, i + pad + 1)):
                        for q in range(max(0, j - pad), min(width, j + pad + 1)):
                            dist_color = np.linalg.norm(self.image[p, q] - self.image[i, j])
                            dist_space = np.linalg.norm([p - i, q - j])
                            weight = np.exp(-dist_color**2 / (2 * sigmaColor**2) - dist_space**2 / (2 * sigmaSpace**2))
                            val += self.image[p, q, k] * weight
                            w += weight

                    result[i, j, k] = val / w

        self.image = result

def parse_arguments():
    parser = argparse.ArgumentParser(description='Custom Image Blurring')
    parser.add_argument('image_path', type=str, help='Path to the input image')
    parser.add_argument('--blur', choices=['median', 'gaussian', 'average', 'bilateral'], default='median',
                        help='Blur technique to apply (median, gaussian, average, bilateral)')
    parser.add_argument('--median', type=int, default=3, help='Kernel size for median blur')
    parser.add_argument('--gaussian', nargs=2, type=float, default=[5, 1.0],
                        help='Kernel size and sigma for Gaussian blur')
    parser.add_argument('--average', nargs=2, type=int, default=[5, 5], help='Kernel size for average blur')
    parser.add_argument('--bilateral', nargs=3, type=int, default=[9, 75, 75],
                        help='d, sigmaColor, and sigmaSpace for bilateral blur')
    return parser.parse_args()

if __name__ == "__main__":
    args = parse_arguments()

    custom_blur = CustomBlur(args.image_path)
    custom_blur.show_image("Original Image")

    # Apply the selected blur technique
    blur_args = {
        'median': {'kernel_size': args.median},
        'gaussian': {'kernel_size': tuple(map(int, args.gaussian)), 'sigma': tuple(map(float, args.gaussian))},
        'average': {'kernel_size': tuple(map(int, args.average))},
        'bilateral': {'d': args.bilateral[0], 'sigmaColor': args.bilateral[1], 'sigmaSpace': args.bilateral[2]}
    }
    custom_blur.apply_blur(args.blur, **blur_args[args.blur])

    # Show the blurred image
    custom_blur.show_image("Blurred Image")

    # Save the blurred image to a file (change 'blurred_image.jpg' to the desired filename)
    cv2.imwrite('blurred_image.jpg', custom_blur.image)


# Usage

# python custom_blur.py image.jpeg --blur gaussian --gaussian 5 1
# python custom_blur.py image.jpeg --blur median --median 5
