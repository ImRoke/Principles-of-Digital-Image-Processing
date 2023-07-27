import cv2
import numpy as np
import matplotlib.pyplot as plt
import argparse

class CustomArithmeticBitwiseOperations:
    def __init__(self, img1_path, img2_path):
        self.img1 = cv2.imread(img1_path)
        self.img2 = cv2.imread(img2_path)

    def add_images(self):
        return self._perform_element_wise_operation(self._add)

    def subtract_images(self):
        return self._perform_element_wise_operation(self._subtract)

    def weighted_addition(self, alpha=0.5, beta=0.5, gamma=0):
        return self._perform_element_wise_operation(self._weighted_addition, alpha, beta, gamma)

    def multiply_images(self):
        return self._perform_element_wise_operation(self._multiply)

    def bitwise_and(self):
        return self._perform_bitwise_operation(self._bitwise_and)

    def bitwise_or(self):
        return self._perform_bitwise_operation(self._bitwise_or)

    def bitwise_xor(self):
        return self._perform_bitwise_operation(self._bitwise_xor)

    def bitwise_not(self):
        return self._perform_bitwise_operation(self._bitwise_not)

    def _add(self, x, y):
        return x + y

    def _subtract(self, x, y):
        return x - y

    def _weighted_addition(self, x, y, alpha, beta, gamma):
        return alpha * x + beta * y + gamma

    def _multiply(self, x, y):
        return x * y

    def _bitwise_and(self, x, y):
        return x & y

    def _bitwise_or(self, x, y):
        return x | y

    def _bitwise_xor(self, x, y):
        return x ^ y

    def _bitwise_not(self, x, y):
        return ~x

    def _perform_element_wise_operation(self, operation_func, *args):
        result = np.zeros_like(self.img1)
        for i in range(self.img1.shape[0]):
            for j in range(self.img1.shape[1]):
                for k in range(self.img1.shape[2]):
                    result[i, j, k] = operation_func(self.img1[i, j, k], self.img2[i, j, k], *args)
        return np.clip(result, 0, 255).astype(np.uint8)

    def _perform_bitwise_operation(self, operation_func):
        result = np.zeros_like(self.img1)
        for i in range(self.img1.shape[0]):
            for j in range(self.img1.shape[1]):
                for k in range(self.img1.shape[2]):
                    result[i, j, k] = operation_func(self.img1[i, j, k], self.img2[i, j, k])
        return result

    def perform_operation(self, operation):
        if operation == 'add':
            return self.add_images()
        elif operation == 'subtract':
            return self.subtract_images()
        elif operation == 'weighted':
            return self.weighted_addition()
        elif operation == 'multiply':
            return self.multiply_images()
        elif operation == 'and':
            return self.bitwise_and()
        elif operation == 'or':
            return self.bitwise_or()
        elif operation == 'xor':
            return self.bitwise_xor()
        elif operation == 'not':
            return self.bitwise_not()
        else:
            raise ValueError(f"Invalid operation: {operation}")
          

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
    parser.add_argument('--operation', choices=['add', 'subtract', 'weighted', 'multiply', 'and', 'or', 'xor', 'not'], 
                        default='add', help='Operation to perform on the images')
    return parser.parse_args()

if __name__ == "__main__":
    args = parse_arguments()

    custom_arith_bitwise = CustomArithmeticBitwiseOperations(args.img1_path, args.img2_path)
    result_image = custom_arith_bitwise.perform_operation(args.operation)

    plt.imshow(cv2.cvtColor(result_image, cv2.COLOR_BGR2RGB))
    plt.title(f"{args.operation.capitalize()} of Images")
    plt.show()



# Usage

# python custom_arithmetic_bitwise_operations.py path_to_image1.jpg path_to_image2.jpg --operation add
