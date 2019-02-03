import cv2
import numpy as np

def abs_sobel(
    gray,
    orient='x',
    sobel_kernel=3
):
    assert orient in ("x", "y")
    derivative = cv2.Sobel(
        gray,
        cv2.CV_64F,
        int(orient == 'x'),
        int(orient == 'y'),
        ksize=sobel_kernel
    )
    absolute = np.absolute(derivative)

    # scale to 0-255
    scaled_sobel = np.uint8(255 * absolute / np.max(absolute))

    return scaled_sobel


def magnitude(gray, sobel_kernel=3):
    dx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=sobel_kernel)
    dy = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=sobel_kernel)

    mag = np.sqrt((dx ** 2) + (dy ** 2))

    scaled = np.uint8(255 * mag / np.max(mag))

    return scaled


def direction(gray, sobel_kernel=3):
    dx = np.absolute(cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=sobel_kernel))
    dy = np.absolute(cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=sobel_kernel))

    grad_dir = np.arctan2(dy, dx)

    return grad_dir
