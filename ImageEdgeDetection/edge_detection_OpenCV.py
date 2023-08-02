import cv2
import numpy as np
import argparse
import matplotlib.pyplot as plt


class EdgeDetectionOpenCV:
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

    def canny_edge_detection(self, image):
        return cv2.Canny(cv2.GaussianBlur(image, (5, 5), 1), 100, 200)  # cv2.Canny(image, 100, 200) not preferred

    def laplacian_edge_detection(self, image):
        return cv2.Laplacian(image, cv2.CV_64F)

    def sobel_x_edge_detection(self, image):
        return cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=5)

    def sobel_y_edge_detection(self, image):
        return cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=5)

    def prewitt_x_edge_detection(self, image):
        kernel_prewitt_x = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]])
        return cv2.filter2D(image, cv2.CV_64F, kernel_prewitt_x)

    def prewitt_y_edge_detection(self, image):
        kernel_prewitt_y = np.array([[-1, -1, -1], [0, 0, 0], [1, 1, 1]])
        return cv2.filter2D(image, cv2.CV_64F, kernel_prewitt_y)

    def robert_x_edge_detection(self, image):
        kernel_robert_x = np.array([[1, 0], [0, -1]])
        return cv2.filter2D(image, cv2.CV_64F, kernel_robert_x)

    def robert_y_edge_detection(self, image):
        kernel_robert_y = np.array([[0, 1], [-1, 0]])
        return cv2.filter2D(image, cv2.CV_64F, kernel_robert_y)

    def perform_edge_detection(self, image):
        return self.available_techniques[self.technique_name](image)

def plot_and_save_edge_detection(image_path, technique_name):
    edge_detection = EdgeDetectionOpenCV(technique_name)

    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    edges = edge_detection.perform_edge_detection(image)

    result_image = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)
    cv2.addWeighted(result_image, 0.7, cv2.cvtColor(image, cv2.COLOR_GRAY2BGR), 0.3, 0, result_image)

    
    output_path = f'edge_detection_{technique_name}.png'
    cv2.imwrite(output_path, result_image)
    print(f"Edge detection result saved to {output_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Perform edge detection using different techniques")
    parser.add_argument("input_image", help="Path to the input image file")
    parser.add_argument("technique", choices=["canny", "laplacian", "sobel_x", "sobel_y", "prewitt_x", "prewitt_y", "robert_x", "robert_y"],
                        help="Edge detection technique to use")
    args = parser.parse_args()

    plot_and_save_edge_detection(args.input_image, args.technique)


# Usage

# python edge_detection_OpenCV.py path_to_input_image.jpg canny


