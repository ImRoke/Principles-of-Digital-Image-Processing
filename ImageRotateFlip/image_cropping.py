import cv2
import argparse

def crop_image(image_path, x, y, width, height):
    
    image = cv2.imread(image_path)

    cropped_image = image[y:y+height, x:x+width]

    cv2.imshow("Original Image", image)
    cv2.imshow("Cropped Image", cropped_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Crop an image using slicing technique")
    parser.add_argument("image_path", help="Path to the input image file")
    parser.add_argument("--x", type=int, default=0, help="Starting x-coordinate of the crop")
    parser.add_argument("--y", type=int, default=0, help="Starting y-coordinate of the crop")
    parser.add_argument("--width", type=int, default=100, help="Width of the crop")
    parser.add_argument("--height", type=int, default=100, help="Height of the crop")
    args = parser.parse_args()

    crop_image(args.image_path, args.x, args.y, args.width, args.height)


# Usage

# python image_cropping.py path_to_image.jpg --x 100 --y 50 --width 300 --height 200
