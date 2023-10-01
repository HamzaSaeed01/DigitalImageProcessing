import cv2
import numpy as np


def is_blurred(img1, img2):

    # Taking the variance with laplacian will help us understand which image has mor sharper edges
    # Thereby more fine detail.

    img1_var = cv2.Laplacian(img1, cv2.CV_64F).var()
    img2_var = cv2.Laplacian(img2, cv2.CV_64F).var()

    if img1_var < img2_var:
        print("Image 1 is blurred while Image 2 is clear")
        cv2.imshow('Clear Image', img2)
        cv2.imshow('Blurred Image', img1)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        print("Image 1 is clear while Image 2 is blurred")
        cv2.imshow('Clear Image', img1)
        cv2.imshow('Blurred Image', img2)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


img1 = cv2.imread('C:/Users/Hassan/Downloads/data/data/fig5.jpg', cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread('C:/Users/Hassan/Downloads/data/data/fig5_blur.jpg', cv2.IMREAD_GRAYSCALE)

is_blurred(img1, img2)
