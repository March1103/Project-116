import cv2 
image=cv2.imread('solar-system.jpg')

cv2.putText(image,"sun",(50,180),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText(image,"mercury",(100,280),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText(image,"venus",(150,180),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText(image,"earth",(300,280),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText(image,"mars",(400,180),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText(image,"jupiter",(600,180),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText(image,"satern",(850,280),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText(image,"uranus",(1000,180),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText(image,"neptune",(1100,280),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.imshow("output",image)
cv2.waitKey(0)
