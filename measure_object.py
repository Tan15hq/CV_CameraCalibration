"""
Real-World Object Measurement Script
-----------------------------------
This script computes real-world dimensions of a planar object
using perspective projection equations and calibrated camera parameters.

Steps to run:
1. Place object image as 'object.jpeg'
2. Update distance Z in meters
3. Run: python measure_object_click.py
4. Click left, right, top, bottom edges of object

Dependencies:
- OpenCV
- NumPy
"""






import cv2
import numpy as np

# Camera parameters
fx = 914.4210222
fy = 915.51149098
Z = 2.0  # meters

points = []

def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        points.append((x, y))
        cv2.circle(img, (x, y), 5, (0,255,0), -1)
        cv2.imshow("Image", img)

img = cv2.imread("object_images/obj1.jpeg")
if img is None:
    raise RuntimeError("Image not loaded")

cv2.imshow("Image", img)
cv2.setMouseCallback("Image", click_event)

print("Click 4 points: left, right, top, bottom")
cv2.waitKey(0)
cv2.destroyAllWindows()

if len(points) != 4:
    raise RuntimeError("You must click exactly 4 points")

left, right, top, bottom = points

pixel_width = abs(right[0] - left[0])
pixel_height = abs(bottom[1] - top[1])

real_width = (pixel_width * Z) / fx
real_height = (pixel_height * Z) / fy

print("Pixel width:", pixel_width)
print("Pixel height:", pixel_height)
print("Measured width (m):", real_width)
print("Measured height (m):", real_height)
