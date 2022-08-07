import cv2
def convert(img):
    #inbuilt function to create sketch effect in colour and greyscale
    sk_gray, sk_color = cv2.pencilSketch(img, sigma_s=60, sigma_r=0.07, shade_factor=0.1) 
    return  sk_color

if __name__=="__main__":
    img = cv2.imread('shop.jpg')
    bilateral = convert(img)
    cv2.imwrite('imageface_bilateral.jpg', bilateral)