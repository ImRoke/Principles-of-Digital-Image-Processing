import cv2
import matplotlib.pyplot as plt

# pip install opencv-python matplotlib


class ImageBlur:
    """
    Applies various blur methods to an input image and plots the results.
    """
    
    def __init__(self, image_path):
        """
        Initializes an instance of the ImageBlur class.
        
        Parameters:
            image_path (str): The path of the input image.
        """
        self.image_path = image_path
        self.im = cv2.imread(self.image_path)
        self.im = cv2.cvtColor(self.im, cv2.COLOR_BGR2RGB)
    
    
    def blur_methods(self):
        """
        Applies various blur methods to the input image and plots the results.
        
        Parameters:
            None
            
        Returns:
            None
        """
        # Applying blur or average blur to image
        blr = cv2.blur(self.im, (15, 15))

        # Applying gaussian blur to image
        gaus_blr = cv2.GaussianBlur(self.im, (15, 15), 0)

        # Applying median blur to image
        mdn_blr = cv2.medianBlur(self.im, 15)

        # Applying bilateral blur to image
        blt_blr = cv2.bilateralFilter(self.im, 20, 175, 175)

        # Plotting all the default methods results for comparision
        titles = ["Average Blur", "Gaussian Blur", "Median Blur", "Bilateral Blur"]
        images = [avg_blr, gaus_blr, mdn_blr, bilat_blr]
        
        plt.figure(figsize=(25,15))
        for i in range(4):
            plt.subplot(2, 2, i+1)
            plt.imshow(images[i])
            plt.title(titles[i], fontsize=20)
        plt.tight_layout()
        plt.show()
        
        
    def main(self):
        """
        The main method of the ImageBlur class that applies blur methods to the input image
        and plots the results.
        
        Parameters:
            None
            
        Returns:
            None
        """
        self.blur_methods()


        
if __name__ == "__main__":
    image_path = 'goku3.jpeg'
    ib = ImageBlur(image_path)
    ib.main()

