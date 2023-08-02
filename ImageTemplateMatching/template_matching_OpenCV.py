import cv2
import numpy as np
import matplotlib.pyplot as plt
import argparse

class TemplateMatchingOpenCV:
    def __init__(self, method_name):
        self.method_name = method_name

        self.available_methods = {
            "cv2.TM_CCOEFF": cv2.TM_CCOEFF,
            "cv2.TM_CCOEFF_NORMED": cv2.TM_CCOEFF_NORMED,
            "cv2.TM_CCORR": cv2.TM_CCORR,
            "cv2.TM_CCORR_NORMED": cv2.TM_CCORR_NORMED,
            "cv2.TM_SQDIFF": cv2.TM_SQDIFF,
            "cv2.TM_SQDIFF_NORMED": cv2.TM_SQDIFF_NORMED
        }

        if method_name not in self.available_methods:
            raise ValueError("Invalid template matching method name. Please choose from the available methods.")

    def perform_template_matching(self, image, template):
        if len(image.shape) == 3:
            image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        if len(template.shape) == 3:
            template = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)

        method = self.available_methods[self.method_name]

        result = cv2.matchTemplate(image, template, method)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

        if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
            top_left = min_loc
            match_val = min_val
        else:
            top_left = max_loc
            match_val = max_val

        h, w = template.shape
        bottom_right = (top_left[0] + w, top_left[1] + h)

        return top_left, bottom_right, match_val

def plot_template_matching_results(image_path, template_path, method_name):
    template_matching = TemplateMatchingOpenCV(method_name)

    image = cv2.imread(image_path)
    template = cv2.imread(template_path)

    top_left, bottom_right, match_val = template_matching.perform_template_matching(image, template)

    
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

    plt.savefig('template_matching_OpenCV.png') 
    plt.show()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Perform template matching using different techniques")
    parser.add_argument("input_image", help="Path to the input image file")
    parser.add_argument("template_image", help="Path to the template image file")
    parser.add_argument("technique", choices=["cv2.TM_CCOEFF", "cv2.TM_CCOEFF_NORMED",
                                              "cv2.TM_CCORR", "cv2.TM_CCORR_NORMED",
                                              "cv2.TM_SQDIFF", "cv2.TM_SQDIFF_NORMED"],
                        help="Template matching technique to use")
    args = parser.parse_args()

    plot_template_matching_results(args.input_image, args.template_image, args.technique)



# Usage

# python template_matching_OpenCV.py path_to_input_image.jpg path_to_template_image.jpg cv2.TM_CCOEFF_NORMED

