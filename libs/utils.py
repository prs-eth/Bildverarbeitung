import cv2
from PyQt5.QtGui import QPixmap, QImage

def convert_cv2img_to_QPixmap(img):
    w,h,ch = img.shape
    if ch == 1:
        img =  cv2.cvtColor(img,cv2.COLOR_GRAY2RGB)

    qimg = QImage(img.data, h, w, 3*h, QImage.Format_RGB888) 
    qpixmap = QPixmap(qimg)
    
    return qpixmap