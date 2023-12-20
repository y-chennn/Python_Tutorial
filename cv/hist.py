import matplotlib.pyplot as plt
import cv2
import numpy as np


PATH = "cv\djoko_air.jpg"
img = cv2.imread(PATH)

img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
hist = cv2.calcHist([img], [0], None, [256], [0, 255])
plt.imshow(img)
plt.show()
print(type(hist), hist.size, hist.shape)

# RGB histogram
# calcHist(img, channels, mask, histSize, ranges)
hist_r = cv2.calcHist([img], [0], None, [256], [0, 255])
hist_g = cv2.calcHist([img], [1], None, [256], [0, 255])
hist_b = cv2.calcHist([img], [2], None, [256], [0, 255])

plt.figure(figsize=(8, 6))
plt.plot(hist_r, color="red", label="Red")
plt.plot(hist_g, color="green", label="Green")
plt.plot(hist_b, color="blue", label="Blue")

plt.title("Color Histogram")
plt.show()


# RGB, HSV histogram
hist_r = cv2.calcHist([img], [0], None, [256], [0, 255])
hist_g = cv2.calcHist([img], [1], None, [256], [0, 255])
hist_b = cv2.calcHist([img], [2], None, [256], [0, 255])

img_hsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
hist_h = cv2.calcHist([img_hsv], [0], None, [180], [0, 179])
hist_s = cv2.calcHist([img_hsv], [1], None, [256], [0, 255])
hist_v = cv2.calcHist([img_hsv], [2], None, [256], [0, 255])

plt.figure(figsize=(15, 5))
plt.subplot(1, 2, 1)
plt.plot(hist_r, color="red", label="Red")
plt.plot(hist_g, color="green", label="Green")
plt.plot(hist_b, color="blue", label="Blue")
plt.title("RGB color histogram")

plt.subplot(1, 2, 2)
plt.plot(hist_h, color="orange", label="Hue")
plt.plot(hist_s, color="purple", label="Saturation")
plt.plot(hist_v, color="brown", label="Value")
plt.title("HSV color histogram")

plt.tight_layout()
plt.show()
