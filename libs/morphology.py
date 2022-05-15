import numpy as np
from cv2 import IMWRITE_PNG_STRATEGY, imread,imwrite, dilate, erode
from cv2 import cvtColor, COLOR_BGR2HLS, calcHist
import cv2 as cv
import random
from matplotlib import pyplot as plt
from skimage.measure import label



# --------------------------------- Zusatzaufgabe ---------------------------------------
def segment_util(img):
    """
    Given an input image, output the segmentation result
    Input:  
        img:        n x m x 3, values are within [0,255]
    Output:
        img_seg:    n x m
    """
    ## TODO
    img_rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    img_hsv = cv.cvtColor(img_rgb, cv.COLOR_RGB2HSV)

    mask = cv.bitwise_not(cv.inRange(img_hsv, (0, 0, 0), (255, 25, 255)))

    white = np.ones((img.shape[0], img.shape[1]), np.uint8)

    img_seg = cv.bitwise_and(white, white, mask=mask)

    return img_seg

def close_hole_util(img):
    """
    Given the segmented image, use morphology techniques to close the holes
    Input:
        img:        n x m, values are within [0,1]
    Output:
        closed_img: n x m
    """
    ## TODO
    closed_img = ...

    return closed_img

def instance_segmentation_util(img):
    """
    Given the closed segmentation image, output the instance segmentation result
    Input:  
        img:        n x m, values are within [0,255]
    Output:
        instance_seg_img:    n x m x 3, different coin instances have different colors
    """
    ## TODO
    instance_seg_img = ...

    return instance_seg_img

def text_recog_util(text, letter_not):
    """
    Given the text and the character, recognise the character in the text
    Input:
        text:           n x m
        letter_not:     a x b
    Output:
        text_er_dil:    n x m
    """
    from scipy.ndimage import binary_erosion as erode
    from scipy.ndimage import binary_dilation as dilate
    ## TODO
    text_er_dil = ...

    return text_er_dil