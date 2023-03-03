import cv2
import numpy as np
import argparse

def custom_bilateral_filter(img, d, sigma_color, sigma_space):
    h, w, c = img.shape
    out = np.zeros_like(img)

    
    # Define spatial Gaussian filter function
    def spatial_filter(x, y):
        return np.exp(-(x ** 2 + y ** 2) / (2 * sigma_space ** 2))
    
    # Calculate the spatial Gaussian filter
    space_filter = np.zeros((d, d))
    center = d // 2
    for i in range(d):
        for j in range(d):
            x = i - center
            y = j - center
            space_filter[i, j] =  spatial_filter(x, y)   # np.exp(-(x ** 2 + y ** 2) / (2 * sigma_space ** 2))

    # Apply the filter to each pixel in the image
    for i in range(h):
        for j in range(w):
            pixel = img[i, j]
            intensity_filter = np.zeros((d, d))
            for k in range(d):
                for l in range(d):
                    x = i + k - center
                    y = j + l - center
                    if x < 0 or y < 0 or x >= h or y >= w:
                        intensity_filter[k, l] = 0
                    else:
                        intensity_filter[k, l] = np.exp(-np.sum((pixel - img[x, y]) ** 2) / (2 * sigma_color ** 2))
            filter = intensity_filter * space_filter
            total_weight = np.sum(filter)
            out[i, j] = np.sum(img * filter[..., np.newaxis], axis=(0, 1)) / total_weight

    return out

def main():
    parser = argparse.ArgumentParser(description='Apply custom bilateral filter to an image')
    parser.add_argument('image_path', type=str, help='Path to input image')
    parser.add_argument('-d', '--diameter', type=int, default=9, help='Diameter of each pixel neighborhood (default: 9)')
    parser.add_argument('-sc', '--sigma_color', type=float, default=75, help='Value of sigma for color space (default: 75)')
    parser.add_argument('-ss', '--sigma_space', type=float, default=75, help='Value of sigma for spatial space (default: 75)')
    parser.add_argument('-o', '--output', type=str, default='output.png', help='Output file name (default: output.png)')

    args = parser.parse_args()

    # Load the image
    img = cv2.imread(args.image_path)

    # Apply the custom bilateral filter
    out = custom_bilateral_filter(img, args.diameter, args.sigma_color, args.sigma_space)

    # Save the output image
    cv2.imwrite(args.output, out)

    print(f"Filtered image saved as {args.output}")

if __name__ == '__main__':
    main()
