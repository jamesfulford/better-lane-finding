import itertools
import functools
import operator

import numpy as np
import cv2

def get_corners(calibration_image, chessboard_dimensions=(9, 6), to_grayscale_flag=cv2.COLOR_BGR2GRAY):
    objp = np.zeros((chessboard_dimensions[0] * chessboard_dimensions[1], 3), np.float32)
    objp[:,:2] = np.mgrid[0:chessboard_dimensions[0],0:chessboard_dimensions[1]].T.reshape(-1,2)

    gray = cv2.cvtColor(calibration_image, to_grayscale_flag)
    ret, corners = cv2.findChessboardCorners(gray, chessboard_dimensions, None)
    if ret == True:
        return calibration_image, objp, corners
    return None  # return None if could not find corners

def calibrate(calibration_images, chessboard_dimensions=(9, 6), to_grayscale_flag=cv2.COLOR_BGR2GRAY):
    output = filter(  # filter out images where could not find chessboard corners
        functools.partial(operator.ne, None),
        map(
            functools.partial(get_corners, chessboard_dimensions=chessboard_dimensions, to_grayscale_flag=to_grayscale_flag), 
            calibration_images
        )
    )
    images, object_points, corners = zip(*output)
    
    ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(
        object_points,
        corners,
        images[0].shape[1::-1],
        None,
        None
    )
    
    return images, object_points, corners, lambda img: cv2.undistort(img, mtx, dist, None, mtx), mtx, dist