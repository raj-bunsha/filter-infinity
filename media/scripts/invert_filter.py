import cv2
def convert(img):
    return  cv2.bitwise_not(img)

if __name__=="__main__":
    img = cv2.imread('shop.jpg')
    bilateral = convert(img)
    cv2.imwrite('imageface_bilateral.jpg', bilateral)