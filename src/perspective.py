import cv2

def get_transformers(src, dst):
    M = cv2.getPerspectiveTransform(src, dst)
    Minv = cv2.getPerspectiveTransform(dst, src)
    return (
        # Transform
        lambda i: cv2.warpPerspective(i, M, (i.shape[1], i.shape[0])),
        # Undo transform
        lambda i: cv2.warpPerspective(i, Minv, (i.shape[1], i.shape[0])),
    )