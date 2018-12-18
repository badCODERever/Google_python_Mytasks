import cv2
import numpy as np
image = cv2.imread('C:\Users\User\Downloads\wWIcR.png')
Conv_hsv_Gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(Conv_hsv_Gray, 0, 255,cv2.THRESH_BINARY_INV |cv2.THRESH_OTSU)
#image.Set(mask,cv2.Scalar(0,0,255)) #the problem
#indices = np.where(mask==255)
#image[indices[0], indices[1], :] = [0, 0, 255]
#cv2.imshow("new_IMAGE",image)
cv2.imshow("imgOriginal", image)
cv2.waitkey(0)
