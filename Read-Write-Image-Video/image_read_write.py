import cv2

def read_image(image_path):
    # Reading an image
    im = cv2.imread(image_path)

    if im is None:
        print(f"Error: Unable to read the image at '{image_path}'")
        return

    # Getting image properties
    height, width, channels = im.shape

    print(f"Image Path: {image_path}")
    print(f"Height of the Image: {height}")
    print(f"Width of the Image: {width}")
    print(f"No of Channels: {channels}")
    print(f"Dimensions of the Image: {height}x{width}x{channels}")

    # Showing the image
    cv2.imshow('Image', im)

    # Image will be shown for infinity time
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    image_path = 'goku3.jpeg'
    read_image(image_path)
