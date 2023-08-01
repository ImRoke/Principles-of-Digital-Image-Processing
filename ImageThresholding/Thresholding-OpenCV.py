import cv2
import argparse
import matplotlib.pyplot as plt

class ImageThresholding:
    def __init__(self, image_path, technique, block_size=11, c=2, adaptive=False):
        self.image_path = image_path
        self.technique = technique
        self.block_size = block_size
        self.c = c
        self.adaptive = adaptive

    def load_image(self):
        return cv2.imread(self.image_path, cv2.IMREAD_GRAYSCALE)

    def threshold_image(self, image):
        if self.technique == "THRESH_BINARY":
            _, thresholded = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

        elif self.technique == "THRESH_BINARY_INV":
            _, thresholded = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

        elif self.technique == "THRESH_TRUNC":
            _, thresholded = cv2.threshold(image, 127, 255, cv2.THRESH_TRUNC)

        elif self.technique == "THRESH_TOZERO":
            _, thresholded = cv2.threshold(image, 127, 255, cv2.THRESH_TOZERO)

        elif self.technique == "THRESH_TOZERO_INV":
            _, thresholded = cv2.threshold(image, 127, 255, cv2.THRESH_TOZERO_INV)

        elif self.technique == "AdaptiveMean":
            thresholded = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, \
                                               cv2.THRESH_BINARY, self.block_size, self.c)

        elif self.technique == "AdaptiveGaussian":
            thresholded = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, \
                                               cv2.THRESH_BINARY, self.block_size, self.c)

        else:
            raise ValueError("Invalid thresholding technique. Please select from the given options.")

        return thresholded

def plot_thresholding_results(image_path, technique, block_size=11, c=2, adaptive=False):
    thresholding_obj = ImageThresholding(image_path, technique, block_size, c, adaptive)
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
    
    plt.savefig('thresholded_OpenCV.png')
    plt.show()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Perform different image thresholding techniques using OpenCV")
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

# python Thresholding-OpenCV.py input_image_path thresholding_technique [--block_size BLOCK_SIZE] [--c C]
# replace the thresholding_technique with the technique you needed
