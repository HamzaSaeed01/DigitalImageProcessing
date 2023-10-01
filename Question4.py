import cv2


def AreaFinder(img1, color):
    img1_mask = cv2.inRange(img1, color, color)
    img1_count = cv2.countNonZero(img1_mask)

    return img1_count


img1 = cv2.imread('C:/Users/Hassan/Downloads/data/data/fig1.jpg')
yellow = (102, 217, 254)
grey1 = (230, 229, 231)
grey2 = (217, 217, 217)
grey3 = (169, 170, 174)

print("The Area of Yellow : ", AreaFinder(img1, yellow))
print("The Area of Light Gray : ", AreaFinder(img1, grey1))
print("The Area of Dark Gray : ", AreaFinder(img1, grey2))
print("The Area of Darkest Gray : ", AreaFinder(img1, grey3))
