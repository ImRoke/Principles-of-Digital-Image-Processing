import cv2
import numpy as np
import argparse
import matplotlib.pyplot as plt


class CustomImageRotateFlip:
    def __init__(self, image_path):
        self.image_path = image_path
        self.im = cv2.imread(self.image_path)

    def rotate(self, angle):
        if angle == 90:
            rotated_image = self.rotate_90()
        elif angle == 180:
            rotated_image = self.rotate_180()
        elif angle == 270:
            rotated_image = self.rotate_270()
        else:
            raise ValueError("Invalid rotation angle. Use 90, 180, or 270 degrees.")
        return rotated_image

    def rotate_90(self):
        height, width, channels = self.im.shape
        rotated_image = np.zeros((width, height, channels), dtype=self.im.dtype)
        for i in range(width):
            for j in range(height):
                rotated_image[i, j] = self.im[j, width - 1 - i]
        return rotated_image

    def rotate_180(self):
        height, width, channels = self.im.shape
        rotated_image = np.zeros_like(self.im)
        for i in range(height):
            for j in range(width):
                rotated_image[i, j] = self.im[height - 1 - i, width - 1 - j]
        return rotated_image

    def rotate_270(self):
        height, width, channels = self.im.shape
        rotated_image = np.zeros((width, height, channels), dtype=self.im.dtype)
        for i in range(width):
            for j in range(height):
                rotated_image[i, j] = self.im[height - 1 - j, i]
        return rotated_image

    def flip(self, direction):
        if direction == 'horizontal':
            flipped_image = self.flip_horizontal()
        elif direction == 'vertical':
            flipped_image = self.flip_vertical()
        else:
            raise ValueError("Invalid flip direction. Use 'horizontal' or 'vertical'.")
        return flipped_image

    def flip_horizontal(self):
        height, width, channels = self.im.shape
        flipped_image = np.zeros_like(self.im)
        for i in range(height):
            for j in range(width):
                flipped_image[i, j] = self.im[i, width - 1 - j]
        return flipped_image

    def flip_vertical(self):
        height, width, channels = self.im.shape
        flipped_image = np.zeros_like(self.im)
        for i in range(height):
            for j in range(width):
                flipped_image[i, j] = self.im[height - 1 - i, j]
        return flipped_image


def plot_results(image_path, rotate_angle=None, flip_direction=None):
    transformer = CustomImageRotateFlip(image_path)

    # input_image = plt.imread(image_path)
    input_image = cv2.cvtColor(cv2.imread(image_path), cv2.COLOR_BGR2RGB)

    transformed_image = None
    transformation_name = ""
    transformation_title = ""

    if rotate_angle:
        transformed_image = transformer.rotate(rotate_angle)
        transformation_name = f"rotated_{rotate_angle}"
        transformation_title = f"Rotated {rotate_angle} Degrees"
    elif flip_direction:
        transformed_image = transformer.flip(flip_direction)
        transformation_name = f"flipped_{flip_direction}"
        transformation_title = f"Flipped {flip_direction.capitalize()}"
    else:
        print("No transformation selected. Please specify either --rotate or --flip.")
        return

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

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Perform rotate and flip from scratch")
    parser.add_argument("input_image", help="Path to the input image file")
    parser.add_argument("--rotate", type=int, choices=[90, 180, 270], help="Rotation angle (choose from 90, 180, or 270)")
    parser.add_argument("--flip", choices=['horizontal', 'vertical'], help="Flip direction ('horizontal' or 'vertical')")
    args = parser.parse_args()

    plot_results(args.input_image, args.rotate, args.flip)


# Usage

# python custom_rotate_flip.py path_to_input_image.jpg --rotate 90
# python custom_rotate_flip.py path_to_input_image.jpg --flip horizontal
