import cv2
import matplotlib.pyplot as plt
import argparse

class custom_colorspace:
    def __init__(self, image_path):
        self.image_path = image_path
        self.img = cv2.imread(image_path)

    def convert_colorspace(self, colorspace):
        if colorspace == 'rgb':
            return cv2.cvtColor(self.img, cv2.COLOR_BGR2RGB)
        elif colorspace == 'hsv':
            return cv2.cvtColor(self.img, cv2.COLOR_BGR2HSV)
        elif colorspace == 'yuv':
            return cv2.cvtColor(self.img, cv2.COLOR_BGR2YUV)
        elif colorspace == 'yuv420':
            return cv2.cvtColor(self.img, cv2.COLOR_BGR2YUV_I420)
        elif colorspace == 'gray':
            return cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)
        elif colorspace == 'ycrcb':
            return cv2.cvtColor(self.img, cv2.COLOR_BGR2YCrCb)
        else:
            print(f"Unknown colorspace: {colorspace}")
            return None

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Convert image color space')
    parser.add_argument('image_path', type=str, help='Path to the input image')
    parser.add_argument('--colorspace', type=str, default='rgb', help='Color space to convert (rgb, hsv, yuv, yuv420, gray, ycrcb)')
    args = parser.parse_args()

    custom_cs = custom_colorspace(args.image_path)
    converted_img = custom_cs.convert_colorspace(args.colorspace)

    if converted_img is not None:
        plt.imshow(converted_img)
        plt.title(args.colorspace, fontsize=40)
        plt.show()



# Usage

python color-spaces-OpenCV.py image.png --colorspace hsv
