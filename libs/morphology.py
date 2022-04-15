import numpy as np
from cv2 import imread, imwrite, dilate, erode
from cv2 import cvtColor, COLOR_BGR2HLS
from matplotlib import pyplot as plt
from skimage.measure import label       # pip install scikit-image


# --------------------------------- Zusatzaufgabe ---------------------------------------
def segment_util(img):
    """
    Given an input image, output the semantic segmentation result
    Input:  
        img:        n x m x 3, values are within [0,255]
    Output:
        img_seg:    n x m
    """

    ## TODO
    img_seg = ...

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


def count_coins_util(img):
    """
    Given the closed segmentation image, count how many coins
    Input:
        img:          n x m
    Output:
        labelde_img:  n x m
        n_components: integer

    """
    ## TODO
    labeled_img = ...
    n_components = ...
    return labeled_img, n_components


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