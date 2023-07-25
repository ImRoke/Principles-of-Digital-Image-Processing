import cv2
import numpy as np
import argparse

class Blur:
    def __init__(self, image_path):
        self.image_path = image_path
        self.image = cv2.imread(image_path)
        self.image = cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB)

    @staticmethod
    def gauss_kernel(filter_size, sigma=1):
        filter_size = int(filter_size) // 2
        hgt, wdt = np.mgrid[-filter_size:filter_size+1, -filter_size:filter_size+1]
        gaus_const = 1 / (2.0 * np.pi * sigma**2)
        gauss = np.exp(-((hgt**2 + wdt**2) / (2.0*sigma**2))) * gaus_const
        return gauss

    def custom_average_blur(self, kernel_size):
        h, w, c = self.image.shape
        kernel = np.ones(kernel_size) / (kernel_size[0] * kernel_size[1])
        blurred_image = np.zeros_like(self.image)

        kh, kw = kernel_size
        for row in range(h - kh + 1):
            for col in range(w - kw + 1):
                for ch in range(c):
                    blurred_image[row, col, ch] = np.sum(self.image[row:row + kh, col:col + kw, ch] * kernel)

        return blurred_image

    def custom_gaussian_blur(self, kernel_size, sigma):
        h, w, c = self.image.shape
        kernel = self.gauss_kernel(kernel_size, sigma)
        blurred_image = np.zeros_like(self.image)

        kh, kw = kernel_size
        for row in range(h - kh + 1):
            for col in range(w - kw + 1):
                for ch in range(c):
                    blurred_image[row, col, ch] = np.sum(self.image[row:row + kh, col:col + kw, ch] * kernel)

        return blurred_image

    def custom_bilateral_filter(self, d, sigma_color, sigma_space):
        h, w, c = self.image.shape
        out = np.zeros_like(self.image)

        def spatial_filter(x, y):
            return np.exp(-(x ** 2 + y ** 2) / (2 * sigma_space ** 2))

        space_filter = np.zeros((d, d))
        center = d // 2
        for i in range(d):
            for j in range(d):
                x = i - center
                y = j - center
                space_filter[i, j] = spatial_filter(x, y)

        for i in range(h):
            for j in range(w):
                pixel = self.image[i, j]
                intensity_filter = np.zeros((d, d))
                for k in range(d):
                    for l in range(d):
                        x = i + k - center
                        y = j + l - center
                        if x < 0 or y < 0 or x >= h or y >= w:
                            intensity_filter[k, l] = 0
                        else:
                            intensity_filter[k, l] = np.exp(-np.sum((pixel - self.image[x, y]) ** 2) / (2 * sigma_color ** 2))
                filter = intensity_filter * space_filter
                total_weight = np.sum(filter)
                out[i, j] = np.sum(self.image * filter[..., np.newaxis], axis=(0, 1)) / total_weight

        return out

    def custom_median_blur(self, kernel_size):
        h, w, c = self.image.shape
        kernel = np.ones(kernel_size)
        blurred_image = np.zeros_like(self.image)

        kh, kw = kernel_size
        for row in range(h - kh + 1):
            for col in range(w - kw + 1):
                for ch in range(c):
                    blurred_image[row, col, ch] = np.median(self.image[row:row + kh, col:col + kw, ch] * kernel)

        return blurred_image

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Apply custom blur techniques to an image')
    parser.add_argument('image_path', type=str, help='Path to input image')
    parser.add_argument('--blur', choices=['average', 'gaussian', 'bilateral', 'median'], default='average',
                        help='Blur technique to apply (default: average)')
    parser.add_argument('--kernel_size', type=int, nargs=2, default=[5, 5], help='Kernel size for blur (default: 5 5)')
    parser.add_argument('--sigma', type=float, default=1, help='Sigma value for Gaussian blur (default: 1)')
    args = parser.parse_args()

    blur = Blur(args.image_path)

    if args.blur == 'average':
        blurred_image = blur.custom_average_blur(tuple(args.kernel_size))
    elif args.blur == 'gaussian':
        blurred_image = blur.custom_gaussian_blur(tuple(args.kernel_size), args.sigma)
    elif args.blur == 'bilateral':
        blurred_image = blur.custom_bilateral_filter(d=args.kernel_size[0], sigma_color=args.sigma, sigma_space=args.sigma)
    elif args.blur == 'median':
        blurred_image = blur.custom_median_blur(tuple(args.kernel_size))
    else:
        raise ValueError('Invalid blur technique.')

    cv2.imshow('Blurred Image', blurred_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# Usage 

python custom_blur.py gargantua.png --blur gaussian --kernel_size 9 9 --sigma 2.5
