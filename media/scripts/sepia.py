import cv2
import numpy as np
def convert(img):
    img_sepia = np.array(img, dtype=np.float64) # converting to float to prevent loss
    # img_sepia = cv2.transform(img_sepia, np.matrix([[0.272, 0.534, 0.131],
    #                                 [0.349, 0.686, 0.168],
    #                                 [0.393, 0.769, 0.189]])) # multipying image with special sepia matrix
    img_sepia = cv2.transform(img_sepia, np.matrix([[0.393,0.769,0.189],
                                    [0.349 , 0.686 , 0.168],
                                    [0.272 , 0.534 , 0.131]])) # multipying image with special sepia matrix
    img_sepia[np.where(img_sepia > 255)] = 255 # normalizing values greater than 255 to 255
    img_sepia = np.array(img_sepia, dtype=np.uint8)
    return img_sepia
