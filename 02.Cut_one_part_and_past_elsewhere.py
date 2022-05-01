#modify an image 
import cv2
img=cv2.imread("img3.jpg", 1)
img=cv2.resize(img,(0,0), fx=0.5,fy=0.5)
print(img.shape)
#cut one part of imag and past it to another location
cut=img[200:300,300:400]
img[410:510,650:750]=cut


cv2.imshow("image" ,img)
cv2.waitKey(0)
cv2.destroyAllWindows()
