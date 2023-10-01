import cv2
import numpy as np

image = cv2.imread('C:/Users/Hassan/Downloads/data/data/rect1.jpg', cv2.IMREAD_GRAYSCALE)
contours, _ = cv2.findContours(image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

largest_contour = max(contours, key=cv2.contourArea)

x, y, w, h = cv2.boundingRect(largest_contour)
centroid_x = x + w // 2
centroid_y = y + h // 2

if w == h:
    print("The Detected object is a Square")
else:
    print("The Detected object is a Rectangle")


print("Width:", w)
print("Height:", h)
print("Centroid (x, y):", centroid_x, centroid_y)

cv2.rectangle(image, (x, y), (x + w, y + h), 255, 2)

# Display the image with the detected rectangle
cv2.imshow('Detected Object', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
