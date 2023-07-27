import cv2
import argparse
import matplotlib.pyplot as plt

class ImageRotateFlip:
    def __init__(self, image_path):
        self.image_path = image_path
        self.im = cv2.imread(self.image_path)
        self.im = cv2.cvtColor(self.im, cv2.COLOR_BGR2RGB)

    def rotate(self, angle):
        if angle == 90:
            rotated_image = cv2.rotate(self.im, cv2.ROTATE_90_CLOCKWISE)
        elif angle == 180:
            rotated_image = cv2.rotate(self.im, cv2.ROTATE_180)
        elif angle == 270:
            rotated_image = cv2.rotate(self.im, cv2.ROTATE_90_COUNTERCLOCKWISE)
        else:
            raise ValueError("Invalid rotation angle. Use 90, 180, or 270 degrees.")
        return rotated_image

    def flip(self, direction):
        if direction == 'horizontal':
            flipped_image = cv2.flip(self.im, 1)
        elif direction == 'vertical':
            flipped_image = cv2.flip(self.im, 0)
        else:
            raise ValueError("Invalid flip direction. Use 'horizontal' or 'vertical'.")
        return flipped_image


def plot_results(image_path, rotate_angle=None, flip_direction=None):
    
    transformer = ImageRotateFlip(image_path)

    input_image = plt.imread(image_path)

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


    fig, axs = plt.subplots(1, 2, figsize = (20, 10))
    # Plot the input image on the first subplot
    axs[0].imshow(input_image)
    axs[0].set_title("Input Image")
    axs[0].axis('off')
    
    # Plot the transformed image on the second subplot
    axs[1].imshow(transformed_image)
    axs[1].set_title(transformation_title)
    axs[1].axis('off')

    output_filename = f"transformed_{transformation_name}.png"
    plt.savefig(output_filename) 
    plt.show()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Perform rotate and flip using OpenCV")
    parser.add_argument("input_image", help="Path to the input image file")
    parser.add_argument("--rotate", type=int, choices=[90, 180, 270], help="Rotation angle (choose from 90, 180, or 270)")
    parser.add_argument("--flip", choices=['horizontal', 'vertical'], help="Flip direction ('horizontal' or 'vertical')")
    args = parser.parse_args()

    plot_results(args.input_image, args.rotate, args.flip)


# Usage

# python rotate_flip_OpenCV.py path_to_input_image.jpg --rotate 90
# python rotate_flip_OpenCV.py path_to_input_image.jpg --flip horizontal
