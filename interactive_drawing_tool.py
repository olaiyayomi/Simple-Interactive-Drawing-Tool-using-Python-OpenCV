import numpy as np
import cv2 as cv



def myfunc(event, x, y, other1, other2):
    if event == cv.EVENT_LBUTTONDBLCLK:
        cv.circle(img, (x,y), 50, (0,0,255), -1)

    elif event == cv.EVENT_RBUTTONDBLCLK:
        cv.circle(img, (x,y), 50, (0,255,0), -1)

    elif event == cv.EVENT_LBUTTONDOWN:
        cv.circle(img, (x,y), 50, (255,0,0), -1)

img = np.zeros((500,500,3), np.uint8)
cv.namedWindow("image")

cv.setMouseCallback('image', myfunc)



while(1):
    cv.imshow("image", img)
    if(cv.waitKey(1) == ord("q")):
        
        break
cv.destroyAllWindows()
