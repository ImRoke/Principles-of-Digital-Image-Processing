import cv2
import numpy as np
import argparse
import matplotlib.pyplot as plt

class CustomTemplateMatching:
    """
    Template matching class that implements different template matching techniques.
    """

    def __init__(self, method_name):
        """
        Constructor for the TemplateMatching class.

        Args:
            method_name: The name of the template matching technique to use.
        """
        self.method_name = method_name

    def calculate_score(self, image_patch, template):
        """
        Calculates the score for a given image patch and template.

        Args:
            image_patch: The image patch.
            template: The template.

        Returns:
            The score for the image patch and template.
        """
        if self.method_name == "cv2.TM_CCOEFF":
            """
            The correlation coefficient between the image patch and the template.
            """
            return np.sum(image_patch * template)
        elif self.method_name == "cv2.TM_CCOEFF_NORMED":
            """
            The normalized correlation coefficient between the image patch and the template.

            This is a measure of how similar the two images are, normalized by the standard deviation of the images.
            """
            mean_image = np.mean(image_patch)
            mean_template = np.mean(template)
            corr = np.sum((image_patch - mean_image) * (template - mean_template))
            norm = np.sqrt(np.sum(np.square(image_patch - mean_image)) * np.sum(np.square(template - mean_template)))
            return corr / norm
        elif self.method_name == "cv2.TM_CCORR":
            """
            The cross-correlation between the image patch and the template.
            """
            return np.sum(image_patch * template)
        elif self.method_name == "cv2.TM_CCORR_NORMED":
            """
            The normalized cross-correlation between the image patch and the template.

            This is a measure of how similar the two images are, normalized by the standard deviation of the images.
            """
            corr = np.sum(image_patch * template)
            norm = np.sqrt(np.sum(np.square(image_patch)) * np.sum(np.square(template)))
            return corr / norm
        elif self.method_name == "cv2.TM_SQDIFF":
            """
            The sum of the squared differences between the image patch and the template.

            This is a measure of how different the two images are.
            """
            return np.sum(np.square(image_patch - template))
        elif self.method_name == "cv2.TM_SQDIFF_NORMED":
            """
            The normalized sum of the squared differences between the image patch and the template.

            This is a measure of how different the two images are, normalized by the standard deviation of the images.
            """
            return np.sum(np.square(image_patch - template)) / (np.prod(image_patch.shape))
        else:
            raise ValueError("Invalid template matching method name.")

    def perform_template_matching(self, image, template):
        """
        Performs template matching on the given image and template.

        Args:
            image: The image.
            template: The template.

        Returns:
            The result of the template matching.
        """
        if len(image.shape) == 3:
            image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        if len(template.shape) == 3:
            template = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)

        template_height, template_width = template.shape
        image_height, image_width = image.shape

        result_height = image_height - template_height + 1
        result_width = image_width - template_width + 1
        result = np.zeros((result_height, result_width))

        for y in range(result_height):
            for x in range(result_width):
                image_patch = image[y:y + template_height, x:x + template_width]
                result[y, x] = self.calculate_score(image_patch, template)

        return result


def plot_template_matching_results(image_path, template_path, method_name):
    """
    Plots the results of template matching.

    Args:
        image_path: The path to the image file.
        template_path: The path to the template file.
        method_name: The name of the template matching technique to use.
    """
    template_matching = CustomTemplateMatching(method_name)

    image = cv2.imread(image_path)
    template = cv2.imread(template_path)

    result = template_matching.perform_template_matching(image, template)

    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    top_left = max_loc
    h, w = template.shape[:2]
    bottom_right = (top_left[0] + w, top_left[1] + h)

    # Draw rectangle around the matched area
    result_image = image.copy()
    cv2.rectangle(result_image, top_left, bottom_right, (0, 255, 0), 2)

    # Plot the images
    plt.figure(figsize=(12, 6))
    plt.subplot(1, 2, 1)
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title("Original Image")
    plt.axis("off")

    plt.subplot(1, 2, 2)
    plt.imshow(cv2.cvtColor(result_image, cv2.COLOR_BGR2RGB))
    plt.title(f"Template Matching Result - {method_name}")
    plt.axis("off")

    plt.savefig('custom_template_matching.png')
    plt.show()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Perform template matching from scratch using different techniques")
    parser.add_argument("input_image", help="Path to the input image file")
    parser.add_argument("template_image", help="Path to the template image file")
    parser.add_argument("technique", choices=["cv2.TM_CCOEFF", "cv2.TM_CCOEFF_NORMED", "cv2.TM_CCORR",
                                               "cv2.TM_CCORR_NORMED", "cv2.TM_SQDIFF", "cv2.TM_SQDIFF_NORMED"],
                        help="Template matching technique to use")
    args = parser.parse_args()

    plot_template_matching_results(args.input_image, args.template_image, args.technique)



# Usage

# python custom_template_matching.py path_to_input_image.jpg path_to_template_image.jpg cv2_TM_CCOEFF
