import cv2


def distinguish_gender(img1, img2, color):
    # The variable color will store the BGR value of a color
    # We have set the BGR value for brown
    # Since we will be using the brown color of hair to distinguish b/w the boy and the girl

    img1_mask = cv2.inRange(img1, color, color)
    img2_mask = cv2.inRange(img2, color, color)

    img1_count = cv2.countNonZero(img1_mask)
    img2_count = cv2.countNonZero(img2_mask)
    print(img2_count)
    print(img1_count)

    if img1_count > img2_count:
        print("Image 1 is of a girl while Image 2 is of a boy")

    else:
        print("Image 1 is of a boy while Image 2 is of a girl")


# Example usage:
img1 = cv2.imread('C:/Users/Hassan/Downloads/data/data/fig3.jpg')
img2 = cv2.imread('C:/Users/Hassan/Downloads/data/data/fig4.jpg')
color = (10, 19, 32)
distinguish_gender(img1, img2, color)
