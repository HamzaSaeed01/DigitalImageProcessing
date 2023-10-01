import cv2


def AreaFinder(img1, color, original_count):
    img1_mask = cv2.inRange(img1, color, color)
    img1_count = cv2.countNonZero(img1_mask)
    diff = original_count - img1_count
    percentage = (diff/original_count) * 100
    print(diff)
    return percentage


img1 = cv2.imread('C:/Users/Hassan/Downloads/data/data/fig2.jpg')
yellow = (102, 217, 254)
grey1 = (230, 229, 231)
grey2 = (217, 217, 217)
grey3 = (169, 170, 174)

# Using our Knowledge from question 4
Yellow = 20893
Gray1 = 24411
Gray2 = 24720
Gray3 = 24640

print("The Area covered of Yellow : ", AreaFinder(img1, yellow, Yellow), "%")
print("The Area covered of Light Gray : ", AreaFinder(img1, grey1, Gray1), "%")
print("The Area covered of Dark Gray : ", AreaFinder(img1, grey2, Gray2), "%")
print("The Area covered of Darkest Gray : ", AreaFinder(img1, grey3, Gray3), "%")
