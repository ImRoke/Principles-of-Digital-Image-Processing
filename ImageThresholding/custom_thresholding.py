import numpy as np
import argparse
import matplotlib.pyplot as plt

class CustomImageThresholding:
    def __init__(self, image_path, technique, block_size=11, c=2, adaptive=False):
        self.image_path = image_path
        self.technique = technique
        self.block_size = block_size
        self.c = c
        self.adaptive = adaptive

    def load_image(self):
        return plt.imread(self.image_path, cmap="gray")

    def threshold_image(self, image):
        if self.technique == "THRESH_BINARY":
            thresholded = self.threshold_binary(image)

        elif self.technique == "THRESH_BINARY_INV":
            thresholded = self.threshold_binary_inv(image)

        elif self.technique == "THRESH_TRUNC":
            thresholded = self.threshold_trunc(image)

        elif self.technique == "THRESH_TOZERO":
            thresholded = self.threshold_tozero(image)

        elif self.technique == "THRESH_TOZERO_INV":
            thresholded = self.threshold_tozero_inv(image)

        elif self.technique == "AdaptiveMean":
            thresholded = self.adaptive_mean_threshold(image)

        elif self.technique == "AdaptiveGaussian":
            thresholded = self.adaptive_gaussian_threshold(image)

        else:
            raise ValueError("Invalid thresholding technique. Please select from the given options.")

        return thresholded

    def threshold_binary(self, image):
        threshold = self.otsu_threshold(image)
        return (image > threshold) * 255

    def threshold_binary_inv(self, image):
        threshold = self.otsu_threshold(image)
        return (image <= threshold) * 255

    def threshold_trunc(self, image):
        thresholded = np.copy(image)
        thresholded[image > 127] = 127
        return thresholded

    def threshold_tozero(self, image):
        thresholded = np.copy(image)
        thresholded[image <= 127] = 0
        return thresholded

    def threshold_tozero_inv(self, image):
        thresholded = np.copy(image)
        thresholded[image > 127] = 0
        return thresholded

    def otsu_threshold(self, image):
        hist, _ = np.histogram(image.flatten(), bins=256, range=[0, 256])
        total_pixels = image.size
        sum_total = np.sum(np.arange(256) * hist)
        sum_back = 0
        w_back = 0
        w_fore = 0
        variance_max = 0
        threshold = 0

        for t in range(256):
            w_back += hist[t]
            if w_back == 0:
                continue

            w_fore = total_pixels - w_back
            if w_fore == 0:
                break

            sum_back += t * hist[t]
            mean_back = sum_back / w_back
            mean_fore = (sum_total - sum_back) / w_fore

            variance_between = w_back * w_fore * (mean_back - mean_fore) ** 2
            if variance_between > variance_max:
                variance_max = variance_between
                threshold = t

        return threshold

    def adaptive_mean_threshold(self, image):
        thresholded = np.zeros_like(image)
        h, w = image.shape

        for y in range(0, h, self.block_size):
            for x in range(0, w, self.block_size):
                block = image[y:y+self.block_size, x:x+self.block_size]
                threshold = np.mean(block) - self.c
                thresholded[y:y+self.block_size, x:x+self.block_size] = (block > threshold) * 255

        return thresholded



    def adaptive_gaussian_threshold(self, image):                                                              # def adaptive_gaussian_threshold(self, image):
        thresholded = np.zeros_like(image)                                                                     # thresholded = np.zeros_like(image)
        h, w = image.shape                                                                                     # h, w = image.shape
                                                                                                               # for y in range(0, h, self.block_size):
        # Generate the Gaussian kernel                                                                         # for x in range(0, w, self.block_size):
        gaussian_kernel = self._generate_gaussian_kernel()                                                     # block = image[y:y+self.block_size, x:x+self.block_size]
                                                                                                               # block = image[y:y+self.block_size, x:x+self.block_size]
        for y in range(0, h, self.block_size):                                                                 # block_mean = np.mean(block)                                                
            for x in range(0, w, self.block_size):                                                             # block_std = np.std(block)
                block = image[y:y+self.block_size, x:x+self.block_size]                                        # threshold = block_mean + self.c * block_std
                threshold = np.sum(block * gaussian_kernel) - self.c                                           # thresholded[y:y+self.block_size, x:x+self.block_size] = (block > threshold) * 255
                thresholded[y:y+self.block_size, x:x+self.block_size] = (block > threshold) * 255              # return thresholded
                                                                                                               
        return thresholded                                                                                     
                                                                                                              
    def _generate_gaussian_kernel(self):
        # Generate a 2D Gaussian kernel based on block_size and sigma                                          
        x, y = np.meshgrid(np.arange(-self.block_size // 2 + 1, self.block_size // 2 + 1),
                           np.arange(-self.block_size // 2 + 1, self.block_size // 2 + 1))
        gaussian_kernel = np.exp(-(x**2 + y**2) / (2 * (self.block_size // 5)**2))
        return gaussian_kernel / np.sum(gaussian_kernel)


def plot_thresholding_results(image_path, technique, block_size=11, c=2, adaptive=False):
    thresholding_obj = CustomImageThresholding(image_path, technique, block_size, c, adaptive)
    original_image = thresholding_obj.load_image()
    thresholded_image = thresholding_obj.threshold_image(original_image)

    # Plot the images
    plt.figure(figsize=(12, 6))
    plt.subplot(1, 2, 1)
    plt.imshow(original_image, cmap="gray")
    plt.title("Original Image")
    plt.axis("off")

    plt.subplot(1, 2, 2)
    plt.imshow(thresholded_image, cmap="gray")
    plt.title(f"Thresholded Image - {technique}")
    plt.axis("off")

    plt.savefig('custom_thresholding.png') 
    plt.show()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Perform different image thresholding techniques from scratch")
    parser.add_argument("input_image", help="Path to the input image file")
    parser.add_argument("technique", choices=["THRESH_BINARY", "THRESH_BINARY_INV", "THRESH_TRUNC",
                                              "THRESH_TOZERO", "THRESH_TOZERO_INV", "AdaptiveMean",
                                              "AdaptiveGaussian"],
                        help="Thresholding technique to use")
    parser.add_argument("--block_size", type=int, default=11, help="Block size for adaptive thresholding")
    parser.add_argument("--c", type=int, default=2, help="Constant C for adaptive thresholding")
    args = parser.parse_args()

    plot_thresholding_results(args.input_image, args.technique, args.block_size, args.c)


# Usage

# python custom_thresholding.py input_image.png THRESH_BINARY --threshold 128

# python custom_thresholding.py input_image.png AdaptiveMean --block_size 15 --c 5
