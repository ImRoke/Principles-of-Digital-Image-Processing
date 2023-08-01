import cv2
import numpy as np
import argparse
import matplotlib.pyplot as plt


class CustomImageRotator:
    def __init__(self, image_path):
        self.image_path = image_path
        self.im = cv2.imread(self.image_path)

    def rotate(self, angle):
        angle = angle % 360  # Ensure angle is between 0 and 359 degrees
        rotated_image = self.rotate_image(self.im, angle)
        return rotated_image

    def rotate_image(self, image, angle):
        angle_rad = angle * np.pi / 180.0
        height, width = image.shape[:2]
        center_x, center_y = width / 2, height / 2

        # Calculate the new image size after rotation and ensure integers
        new_width = int(abs(width * np.cos(angle_rad)) + abs(height * np.sin(angle_rad)))
        new_height = int(abs(width * np.sin(angle_rad)) + abs(height * np.cos(angle_rad)))

        # Create an empty image to store the rotated image
        rotated_image = np.zeros((new_height, new_width, 3), dtype=np.uint8)

        # Calculate the offset to center the rotated image
        offset_x = (new_width - width) // 2
        offset_y = (new_height - height) // 2

        for y in range(height):
            for x in range(width):
                new_x = int((x - center_x) * np.cos(angle_rad) - (y - center_y) * np.sin(angle_rad)) + center_x
                new_y = int((x - center_x) * np.sin(angle_rad) + (y - center_y) * np.cos(angle_rad)) + center_y
                if 0 <= new_x < new_width and 0 <= new_y < new_height:
                    rotated_image[new_y + offset_y, new_x + offset_x] = image[y, x]

        return rotated_image

def plot_results(image_path, rotate_angle=None):
    transformer = CustomImageRotator(image_path)

    input_image = cv2.cvtColor(cv2.imread(image_path), cv2.COLOR_BGR2RGB)

    if rotate_angle:
        transformed_image = transformer.rotate(rotate_angle)
        transformation_name = f"rotated_{rotate_angle}"
        transformation_title = f"Rotated {rotate_angle} Degrees"

        fig, axs = plt.subplots(1, 2, figsize=(20, 10))
        
        axs[0].imshow(input_image)
        axs[0].set_title("Input Image")
        axs[0].axis('off')
        
        axs[1].imshow(transformed_image)
        axs[1].set_title(transformation_title)
        axs[1].axis('off')

        output_filename = f"transformed_{transformation_name}.png"
        plt.savefig(output_filename) 
        plt.show()
    else:
        print("No rotation angle specified. Please specify the --rotate argument with an angle (e.g., --rotate 90).")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Perform rotate from scratch")
    parser.add_argument("input_image", help="Path to the input image file")
    parser.add_argument("--rotate", type=int, help="Rotation angle (in degrees)")
    args = parser.parse_args()

    plot_results(args.input_image, args.rotate)


# Usage

# python rotate_from_scratch.py path_to_input_image.jpg --rotate 23
