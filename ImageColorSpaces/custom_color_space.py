import cv2
import numpy as np
import argparse
import matplotlib.pyplot as plt

class CustomColorSpace:
    def __init__(self, image_path):
        self.image_path = image_path
        self.img = cv2.imread(image_path)

    def convert_to_rgb(self):
        R = self.img[..., 2]
        G = self.img[..., 1]
        B = self.img[..., 0]
        return self._merge_channels(R, G, B)

    def convert_to_hsv(self):
        B, G, R = self.img[..., 0], self.img[..., 1], self.img[..., 2]
        V = self.img.max(axis=-1)
        S = (V - self.img.min(axis=-1)) / V.clip(min=1e-10)
        diff = V - self.img.min(axis=-1)
        R_diff = (V - R) / diff.clip(min=1e-10)
        G_diff = (V - G) / diff.clip(min=1e-10)
        B_diff = (V - B) / diff.clip(min=1e-10)
        H = 60 * (2 + B_diff - R_diff) + 360 * (V == R)
        H += 60 * (4 + R_diff - G_diff) * (V == G)
        H += 60 * (6 + G_diff - B_diff) * (V == B)
        H = H if H >= 0 else H + 360
        return self._merge_channels(H, S, V)

    def convert_to_yuv(self):
        R, G, B = self.img[..., 2], self.img[..., 1], self.img[..., 0]
        Y = 0.299 * R + 0.587 * G + 0.114 * B
        U = (B - Y) * 0.492
        V = (R - Y) * 0.877
        return self._merge_channels(Y, U, V)

    def convert_to_yuv420(self):
        yuv = self.convert_to_yuv()
        U = yuv[..., 1][::2, ::2]
        V = yuv[..., 2][::2, ::2]
        return self._merge_channels(yuv[..., 0], U, V)

    def convert_to_ycrcb(self):
        R, G, B = self.img[..., 2], self.img[..., 1], self.img[..., 0]
        Y = 0.299 * R + 0.587 * G + 0.114 * B
        Cr = (R - Y) * 0.713 + 128
        Cb = (B - Y) * 0.564 + 128
        return self._merge_channels(Y, Cr, Cb)

    def convert_to_gray(self):
        R, G, B = self.img[..., 2], self.img[..., 1], self.img[..., 0]
        gray = 0.299 * R + 0.587 * G + 0.114 * B
        return gray.astype(np.uint8)

    def _merge_channels(self, *channels):
        result = channels[0].copy()
        for i in range(len(channels)):
            result[..., i] = channels[i]
        return result

    def plot_image(self, img, title):
        plt.imshow(img)
        plt.title(title, fontsize=14)
        plt.axis('off')
        plt.show()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Convert image color space')
    parser.add_argument('image_path', type=str, help='Path to the input image')
    parser.add_argument('--colorspace', type=str, default='rgb', help='Color space to convert (rgb, hsv, yuv, yuv420, ycrcb, gray)')
    args = parser.parse_args()

    custom_cs = CustomColorSpace(args.image_path)

    if args.colorspace == 'rgb':
        converted_img = custom_cs.convert_to_rgb()
    elif args.colorspace == 'hsv':
        converted_img = custom_cs.convert_to_hsv()
    elif args.colorspace == 'yuv':
        converted_img = custom_cs.convert_to_yuv()
    elif args.colorspace == 'yuv420':
        converted_img = custom_cs.convert_to_yuv420()
    elif args.colorspace == 'ycrcb':
        converted_img = custom_cs.convert_to_ycrcb()
    elif args.colorspace == 'gray':
        converted_img = custom_cs.convert_to_gray()
    else:
        print(f"Unknown colorspace: {args.colorspace}")
        converted_img = None

    if converted_img is not None:
        custom_cs.plot_image(converted_img, f"{args.colorspace.upper()} color space")


# Usage

python custom_color_space.py image.png --colorspace hsv
