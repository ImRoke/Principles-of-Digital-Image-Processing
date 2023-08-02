import cv2
import numpy as np
import matplotlib.pyplot as plt
import argparse

class CustomEdgeDetection:
  """
    This class implements edge detection algorithms from scratch.

    Args:
        technique_name (str): The name of the edge detection technique to use.
    """
  
    def __init__(self, technique_name):
        self.technique_name = technique_name

        self.available_techniques = {
            "canny": self.canny_edge_detection,
            "laplacian": self.laplacian_edge_detection,
            "sobel_x": self.sobel_x_edge_detection,
            "sobel_y": self.sobel_y_edge_detection,
            "prewitt_x": self.prewitt_x_edge_detection,
            "prewitt_y": self.prewitt_y_edge_detection,
            "robert_x": self.robert_x_edge_detection,
            "robert_y": self.robert_y_edge_detection
        }

        if technique_name not in self.available_techniques:
            raise ValueError("Invalid edge detection technique name. Please choose from the available techniques.")

    def apply_kernel(self, image, kernel):
      """
        Applies a kernel to an image.

        Args:
            image (np.ndarray): The image to apply the kernel to.
            kernel (np.ndarray): The kernel to apply.

        Returns:
            np.ndarray: The result of applying the kernel to the image.
        """
      
        rows, cols = image.shape
        kernel_size = len(kernel)
        pad = kernel_size // 2

        padded_image = np.pad(image, pad, mode='edge')
        result = np.zeros((rows, cols), dtype=np.float32)

        for i in range(pad, rows + pad):
            for j in range(pad, cols + pad):
                result[i - pad, j - pad] = np.sum(padded_image[i - pad:i + pad + 1, j - pad:j + pad + 1] * kernel)

        return result

    def canny_edge_detection(self, image):
      """
        Performs Canny edge detection on an image.

        Args:
            image (np.ndarray): The image to perform Canny edge detection on.

        Returns:
            np.ndarray: The result of Canny edge detection on the image.
        """
      
        sobel_x = self.sobel_x_edge_detection(image)
        sobel_y = self.sobel_y_edge_detection(image)
        gradient_magnitude = np.sqrt(sobel_x ** 2 + sobel_y ** 2)
        gradient_direction = np.arctan2(sobel_y, sobel_x)

        non_max_suppressed = self.non_max_suppression(gradient_magnitude, gradient_direction)
        threshold_low, threshold_high = 50, 150
        edge_image = self.hysteresis_thresholding(non_max_suppressed, threshold_low, threshold_high)

        return edge_image

    def sobel_x_edge_detection(self, image):
      """
        Performs Sobel edge detection in the x-direction on an image.

        Args:
            image (np.ndarray): The image to perform Sobel edge detection on.

        Returns:
            np.ndarray: The result of Sobel edge detection in the x-direction on the image.
        """

        sobel_x_kernel = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
        return self.apply_kernel(image, sobel_x_kernel)

    def sobel_y_edge_detection(self, image):
      """
        Performs Sobel edge detection in the y-direction on an image.

        Args:
            image (np.ndarray): The image to perform Sobel edge detection on.

        Returns:
            np.ndarray: The result of Sobel edge detection in the y-direction on the image.
        """
      
        sobel_y_kernel = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])
        return self.apply_kernel(image, sobel_y_kernel)

    def laplacian_edge_detection(self, image):
      """
        Performs Laplacian edge detection on an image.

        Args:
            image (np.ndarray): The image to perform Laplacian edge detection on.

        Returns:
            np.ndarray: The result of Laplacian edge detection on the image.
        """
      
        laplacian_kernel = np.array([[0, 1, 0], [1, -4, 1], [0, 1, 0]])
        return self.apply_kernel(image, laplacian_kernel)

    def prewitt_x_edge_detection(self, image):
      """
        Performs Prewitt edge detection in the x-direction on an image.

        Args:
            image (np.ndarray): The image to perform Prewitt edge detection on.

        Returns:
            np.ndarray: The result of Prewitt edge detection in the x-direction on the image.
        """

        prewitt_x_kernel = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]])
        return self.apply_kernel(image, prewitt_x_kernel)

    def prewitt_y_edge_detection(self, image):
      """
        Performs Prewitt edge detection in the y-direction on an image.

        Args:
            image (np.ndarray): The image to perform Prewitt edge detection on.

        Returns:
            np.ndarray: The result of Prewitt edge detection in the y-direction on the image.
        """

        prewitt_y_kernel = np.array([[-1, -1, -1], [0, 0, 0], [1, 1, 1]])
        return self.apply_kernel(image, prewitt_y_kernel)

    def robert_x_edge_detection(self, image):
      """
        Performs Roberts edge detection in the x-direction on an image.

        Args:
            image (np.ndarray): The image to perform Roberts edge detection on.

        Returns:
            np.ndarray: The result of Roberts edge detection in the x-direction on the image.
        """

        robert_x_kernel = np.array([[1, 0], [0, -1]])
        return self.apply_kernel(image, robert_x_kernel)

    def robert_y_edge_detection(self, image):
      """
        Performs Roberts edge detection in the y-direction on an image.

        Args:
            image (np.ndarray): The image to perform Roberts edge detection on.

        Returns:
            np.ndarray: The result of Roberts edge detection in the y-direction on the image.
        """

        robert_y_kernel = np.array([[0, 1], [-1, 0]])
        return self.apply_kernel(image, robert_y_kernel)

    def non_max_suppression(self, gradient_magnitude, gradient_direction):
      """
        Performs non-maximum suppression on an image.

        Args:
            image (np.ndarray): The image to perform non-maximum suppression on.
            gradient_direction (np.ndarray): The gradient direction of the image.

        Returns:
            np.ndarray: The result of non-maximum suppression on the image.
        """
      
        rows, cols = gradient_magnitude.shape
        suppressed = np.zeros((rows, cols), dtype=np.float32)

        for i in range(1, rows - 1):
            for j in range(1, cols - 1):
                angle = gradient_direction[i, j] * 180.0 / np.pi

                if (0 <= angle < 22.5) or (157.5 <= angle <= 180):
                    q = gradient_magnitude[i, j+1]
                    r = gradient_magnitude[i, j-1]
                elif (22.5 <= angle < 67.5):
                    q = gradient_magnitude[i+1, j-1]
                    r = gradient_magnitude[i-1, j+1]
                elif (67.5 <= angle < 112.5):
                    q = gradient_magnitude[i+1, j]
                    r = gradient_magnitude[i-1, j]
                else:
                    q = gradient_magnitude[i-1, j-1]
                    r = gradient_magnitude[i+1, j+1]

                if gradient_magnitude[i, j] >= q and gradient_magnitude[i, j] >= r:
                    suppressed[i, j] = gradient_magnitude[i, j]

        return suppressed

    def hysteresis_thresholding(self, image, low_threshold, high_threshold):
      """
        Performs hysteresis thresholding on an image.

        Args:
            image (np.ndarray): The image to perform hysteresis thresholding on.
            threshold_low (int): The low threshold value.
            threshold_high (int): The high threshold value.

        Returns:
            np.ndarray: The result of hysteresis thresholding on the image.
        """
      
        strong_edges = (image > high_threshold)
        weak_edges = (image >= low_threshold) & (image <= high_threshold)

        connected = self.weak_edge_connected(strong_edges, weak_edges)
        image_final = np.zeros_like(image)
        image_final[strong_edges] = 255
        image_final[connected] = 255

        return image_final

    def weak_edge_connected(self, strong_edges, weak_edges):
      """
        Finds connected weak edges in an image.

        Args:
            strong_edges (np.ndarray): The image of strong edges.
            weak_edges (np.ndarray): The image of weak edges.

        Returns:
            np.ndarray: The image of connected weak edges.
        """
      
        rows, cols = strong_edges.shape
        connected = np.zeros_like(strong_edges)

        for i in range(1, rows - 1):
            for j in range(1, cols - 1):
                if weak_edges[i, j] and np.any(strong_edges[i - 1:i + 2, j - 1:j + 2]):
                    connected[i, j] = 1

        return connected

    def plot_and_save_edge_detection(self, image_path):
        image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
        edges = self.available_techniques[self.technique_name](image)

        result_image = cv2.cvtColor(edges.astype(np.uint8), cv2.COLOR_GRAY2BGR)
        cv2.addWeighted(result_image, 0.7, cv2.cvtColor(image, cv2.COLOR_GRAY2BGR), 0.3, 0, result_image)

        # Save the result
        output_path = f'edge_detection_{self.technique_name}.png'
        cv2.imwrite(output_path, result_image)
        print(f"Edge detection result saved to {output_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Perform edge detection from scratch using different techniques")
    parser.add_argument("input_image", help="Path to the input image file")
    parser.add_argument("technique", choices=["canny", "laplacian", "sobel_x", "sobel_y", "prewitt_x", "prewitt_y", "robert_x", "robert_y"],
                        help="Edge detection technique to use")
    args = parser.parse_args()

    edge_detection = CustomEdgeDetection(args.technique)
    edge_detection.plot_and_save_edge_detection(args.input_image)



# Usage

# python custom_edge_detection.py path_to_input_image.jpg canny
