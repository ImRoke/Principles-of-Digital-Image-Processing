import matplotlib.pyplot as plt
import argparse

class CustomHistHisteq:
    def __init__(self, image_path):
        self.image_path = image_path
        self.im = plt.imread(self.image_path)

    def convert_to_gray(self):
        if len(self.im.shape) == 3:
            self.im = self.im.mean(axis=2)

    def compute_histogram(self):
        histogram = [0] * 256
        for row in self.im:
            for pixel_value in row:
                histogram[int(pixel_value)] += 1
        return histogram

    def equalize_histogram(self):
        self.convert_to_gray()
        histogram = self.compute_histogram()
        total_pixels = self.im.shape[0] * self.im.shape[1]
        equalized_image = self.im.copy()
        cumulative_sum = 0

        for i in range(len(histogram)):
            cumulative_sum += histogram[i]
            equalized_value = int(255 * cumulative_sum / total_pixels)
            equalized_image[self.im == i] = equalized_value

        return equalized_image, self.compute_histogram()

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

    hist_eq = CustomHistHisteq(args.input_image)

    if args.technique == 'histogram':
        histogram = hist_eq.compute_histogram()
        plot_histogram(histogram, [0] * len(histogram))
        plot_results(hist_eq.im, hist_eq.im, hist_eq.im)
    elif args.technique == 'histequalize':
        equalized_image, equalized_histogram = hist_eq.equalize_histogram()
        plot_histogram(hist_eq.compute_histogram(), equalized_histogram)
        plot_results(hist_eq.im, hist_eq.im, equalized_image)


# Usage

# python custom_hist_histeq.py path_to_input_image.jpg --technique histogram
# python custom_hist_histeq.py path_to_input_image.jpg --technique histequalize



# Reference Purpose

# class HistogramEqualizer:
#     def __init__(self, image_path):
#         self.image_path = image_path
#         self.im = self.read_image()

#     def read_image(self):
#         with open(self.image_path, "rb") as f:
#             header = f.read(18)
#             width = int.from_bytes(header[12:14], "little")
#             height = int.from_bytes(header[14:16], "little")
#             data = f.read(width * height)

#         return list(data)

#     def convert_to_gray(self):
#         gray_im = []
#         for pixel in self.im:
#             gray_value = sum(pixel[:3]) // 3
#             gray_im.append(gray_value)
#         self.im = gray_im

#     def compute_histogram(self):
#         histogram = [0] * 256
#         for pixel_value in self.im:
#             histogram[pixel_value] += 1
#         return histogram

#     def equalize_histogram(self):
#         self.convert_to_gray()
#         histogram = self.compute_histogram()
#         total_pixels = len(self.im)
#         equalized_image = []
#         cumulative_sum = 0

#         for pixel_value, frequency in enumerate(histogram):
#             cumulative_sum += frequency
#             equalized_value = int(255 * cumulative_sum / total_pixels)
#             equalized_image.extend([equalized_value] * frequency)

#         return equalized_image, self.compute_histogram()
