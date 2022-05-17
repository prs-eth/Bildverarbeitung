from csv import Dialect
from ipykernel import kernel_protocol_version
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
    kernel = np.ones((2, 2), np.uint8)
    iterations = 5

    img_dilated = dilate(img, kernel, iterations=iterations)
    img_normal = erode(img_dilated, kernel, iterations=iterations)

    closed_img = img_normal

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
    kernel = np.ones((5, 5), dtype=np.uint8)

    _, thresh = cv.threshold(img, 127, 255, cv.THRESH_BINARY)  # thresh is [0, 1]
    dist_transform = cv.distanceTransform(thresh, cv.DIST_L2, 3)  # dist_transform is [0, 255]

    sure_bg = dilate(thresh, kernel, iterations=3)
    _, sure_fg = cv.threshold(dist_transform, 0.5 * dist_transform.max(), 225, 0)  # sure_bg and sure_fg are [0, 1]
    sure_fg = np.uint8(sure_fg)

    unknown = cv.subtract(sure_bg, sure_fg)  # unknown area

    _, markers = cv.connectedComponents(sure_fg)  # assign a marker to each coin
    markers += 1
    markers[unknown == 255] = 0

    img = cv.merge((img, img, img))  # img needs to be 8-bit 3 channel

    markers = cv.watershed(img, markers)
    
    for segment in np.unique(markers):
        img[markers == segment] = [255 * random.random(), 255 * random.random(), 255 * random.random()]

    instance_seg_img = img * 255

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
    _, text_binary = cv.threshold(text, 0.5, 1, cv.THRESH_BINARY_INV)
    _, letter_binary = cv.threshold(letter_not, 0.5, 1, cv.THRESH_BINARY)

    img_eroded = erode(text_binary, letter_binary)
    img_dilated = dilate(img_eroded, letter_binary)

    text_er_dil = img_dilated

    return text_er_dil