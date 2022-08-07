import cv2
def convert(img):
    greyscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return greyscale


if __name__=="__main__":
    img = cv2.imread('comparison.jpg')
    bilateral = convert(img)
    cv2.imwrite('imageface_bilateral.jpg', bilateral)