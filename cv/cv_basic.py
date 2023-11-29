import numpy as py
import cv2
from matplotlib import pyplot as plt

import imageio

# read img
img_path = "/home/rvl224/Documents/1121_python/cv/djoko_air.jpg"

img = cv2.imread(img_path)
cv2.namedWindow("airplane", cv2.WINDOW_NORMAL)
# cv2.imshow("airplane", img)

# cv2.waitKey(0)
# cv2.destroyAllWindows()

img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(img_rgb)
plt.show()

# read gif
# gif_path = "/home/rvl224/Documents/1121_python/cv/djoko_air.gif"

# gif = imageio.mimread(gif_path)
# frames = [cv2.cvtColor(img, cv2.COLOR_RGB2BGR) for img in gif]

# for frame in frames:
#     cv2.imshow("airplane", frame)
#     if cv2.waitKey(50) and 0xFF == 27:
#         break

# cv2.destroyAllWindows()

# grayscale
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# filp
img_filp = cv2.flip(img, 1)


# cv2.imshow("airplane", img, img_filp)

# cv2.waitKey(0)
# cv2.destroyAllWindows()
