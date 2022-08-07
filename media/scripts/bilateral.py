
import cv2
def convert(img):
    bilateral = cv2.bilateralFilter(img, 15, 75, 75)
    return bilateral

