import cv2
import numpy as np
import matplotlib.pyplot as plt
import argparse

class CustomArithmeticBitwise:
    def __init__(self, img1_path, img2_path):
        self.img1 = cv2.imread(img1_path)
        self.img2 = cv2.imread(img2_path)

    def add_images(self):
        return cv2.add(self.img1, self.img2)

    def subtract_images(self):
        return cv2.subtract(self.img1, self.img2)

    def weighted_addition(self, alpha=0.5, beta=0.5, gamma=0):
        return cv2.addWeighted(self.img1, alpha, self.img2, beta, gamma)

    def multiply_images(self):
        return cv2.multiply(self.img1, self.img2)

    def bitwise_and(self):
        return cv2.bitwise_and(self.img1, self.img2)

    def bitwise_or(self):
        return cv2.bitwise_or(self.img1, self.img2)

    def bitwise_xor(self):
        return cv2.bitwise_xor(self.img1, self.img2)

    def bitwise_not(self):
        return cv2.bitwise_not(self.img1)

    def plot_results(self):
        titles = ["First Image", "Second Image", "Addition of images", "Subtraction of images", "Weighted addition of images",
                  "Multiplication of Images", "Bitwise AND of images", "Bitwise OR of images", "Bitwise XOR of images", "Bitwise NOT of image"]
        images = [self.img1, self.img2, self.add_images(), self.subtract_images(), self.weighted_addition(),
                  self.multiply_images(), self.bitwise_and(), self.bitwise_or(), self.bitwise_xor(), self.bitwise_not()]
        
        plt.figure(figsize=(30, 30))
        for i in range(len(titles)):
            plt.subplot(5, 2, i+1)
            plt.imshow(cv2.cvtColor(images[i], cv2.COLOR_BGR2RGB))
            plt.title(titles[i])
        plt.tight_layout()
        plt.savefig('arithmetic_bitwise_operations_OpenCV.png')
        plt.show()

def parse_arguments():
    parser = argparse.ArgumentParser(description='Custom Arithmetic and Bitwise Operations on Images')
    parser.add_argument('img1_path', type=str, help='Path to the first input image')
    parser.add_argument('img2_path', type=str, help='Path to the second input image')
    return parser.parse_args()

if __name__ == "__main__":
    args = parse_arguments()

    custom_arith_bitwise = CustomArithmeticBitwise(args.img1_path, args.img2_path)
    custom_arith_bitwise.plot_results()


# Usage

# python arithmetic_bitwise_operations_OpenCV.py image1.jpg image2.jpg

