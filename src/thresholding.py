import cv2
import numpy as np


def thresh(sc, thresh):
    binary_output = np.zeros_like(sc)
    binary_output[(sc > thresh[0]) & (sc < thresh[1])] = 1
    return binary_output


def and_binary(a, b):
    binary_output = np.zeros_like(a)
    binary_output[(a == 1) & (b == 1)] = 1
    return binary_output


def or_binary(a, b):
    binary_output = np.zeros_like(a)
    binary_output[(a == 1) | (b == 1)] = 1
    return binary_output


def region_of_interest(binary, vertices):
    # defining a blank mask to start with
    mask = np.zeros_like(binary)

    #filling pixels inside the polygon defined by "vertices" with the fill color    
    cv2.fillPoly(mask, vertices, 1)
    
    #returning the image only where mask pixels are nonzero
    masked_image = cv2.bitwise_and(binary, mask)
    return masked_image
