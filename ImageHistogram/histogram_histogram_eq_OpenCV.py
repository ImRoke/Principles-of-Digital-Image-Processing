import cv2
import numpy as np
import matplotlib.pyplot as plt
import argparse

class CustomHistogramOpenCV:
    def __init__(self, image_path):
        self.image_path = image_path
        self.im = cv2.imread(self.image_path, cv2.IMREAD_GRAYSCALE)

    def compute_histogram(self):
        histogram = cv2.calcHist([self.im], [0], None, [256], [0, 256])
        return histogram.flatten()

    def equalize_histogram(self):
        equalized_image = cv2.equalizeHist(self.im)
        return equalized_image, cv2.calcHist([equalized_image], [0], None, [256], [0, 256]).flatten()

def plot_histogram(histogram, equalized_histogram):
    plt.figure(figsize=(12, 6))

    plt.subplot(1, 2, 1)
    plt.plot(histogram, color='black')
    plt.xlim([0, 256])
    plt.xlabel('Pixel Value')
    plt.ylabel('Frequency')
    plt.title('Histogram')
    plt.grid(True)

    plt.subplot(1, 2, 2)
    plt.plot(equalized_histogram, color='black')
    plt.xlim([0, 256])
    plt.xlabel('Pixel Value')
    plt.ylabel('Frequency')
    plt.title('Equalized Histogram')
    plt.grid(True)

    plt.tight_layout()
    plt.show()

def plot_results(input_image, gray_image, equalized_image):
    plt.figure(figsize=(18, 6))

    plt.subplot(1, 3, 1)
    plt.imshow(input_image, cmap='gray')
    plt.title('Original Image')
    plt.axis('off')

    plt.subplot(1, 3, 2)
    plt.imshow(gray_image, cmap='gray')
    plt.title('Gray Image')
    plt.axis('off')

    plt.subplot(1, 3, 3)
    plt.imshow(equalized_image, cmap='gray')
    plt.title('Equalized Image')
    plt.axis('off')

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Perform histogram equalization")
    parser.add_argument("input_image", help="Path to the input image file")
    parser.add_argument("--technique", choices=['histogram', 'histequalize'], default='histequalize', help="Histogram equalization technique ('histogram' or 'histequalize')")
    args = parser.parse_args()

    hist_eq = CustomHistogramOpenCV(args.input_image)

    if args.technique == 'histogram':
        histogram = hist_eq.compute_histogram()
        plot_histogram(histogram, np.zeros_like(histogram))
        plot_results(cv2.cvtColor(hist_eq.im, cv2.COLOR_GRAY2RGB), hist_eq.im, hist_eq.im)
    elif args.technique == 'histequalize':
        equalized_image, equalized_histogram = hist_eq.equalize_histogram()
        plot_histogram(hist_eq.compute_histogram(), equalized_histogram)
        plot_results(cv2.cvtColor(hist_eq.im, cv2.COLOR_GRAY2RGB), hist_eq.im, cv2.cvtColor(equalized_image, cv2.COLOR_GRAY2RGB))



# Usage

# python histogram_histogram_eq_OpenCV.py path_to_input_image.jpg --technique histogram
# python histogram_histogram_eq_OpenCV.py path_to_input_image.jpg --technique histequalize

