import cv2
def convert(img):
    return cv2.detailEnhance(img, sigma_s=12, sigma_r=0.15)

if __name__=="__main__":
    img = cv2.imread('shop.jpg')
    bilateral = convert(img)
    cv2.imwrite('imageface_bilateral.jpg', bilateral)