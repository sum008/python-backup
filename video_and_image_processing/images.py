import cv2

img = cv2.imread("Demon.jpg",1)
print(img)
print(img.shape)

resize_img = cv2.resize(img,(img.shape[0]//2,img.shape[1]//2))
cv2.imshow("demon",resize_img)
cv2.waitKey(0) #0-->press any key and window will close
cv2.destroyAllWindows()