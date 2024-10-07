import numpy as np
import cv2
from matplotlib import pyplot as plt


import imageio

# read img
# img_path = "/home/rvl224/Documents/1121_python/cv/djoko_air.jpg"

# img = cv2.imread(img_path)
# cv2.namedWindow("airplane", cv2.WINDOW_NORMAL)
# # cv2.imshow("airplane", img)

# # cv2.waitKey(0)
# # cv2.destroyAllWindows()

# img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# plt.imshow(img_rgb)
# plt.show()

# read gif
# gif_path = "djoko_air.gif"

# gif = imageio.mimread(gif_path)
# frames = [cv2.cvtColor(img, cv2.COLOR_RGB2BGR) for img in gif]

# for frame in frames:
#     cv2.imshow("airplane", frame)
#     if cv2.waitKey(50) and 0xFF == 27:
#         break

# cv2.destroyAllWindows()


# # grayscale
# # img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# # filp
# # img_filp = cv2.flip(img, 1)


# # cv2.imshow("airplane", img, img_filp)

# # cv2.waitKey(0)
# # cv2.destroyAllWindows()


# 4 channels image
# img = cv2.imread("cv\sample.png")
# print(img.shape)
# imga = cv2.cvtColor(img, cv2.COLOR_BGR2RGBA)
# print(imga.shape)

# b, g, r, a = cv2.split(imga)

# plt.subplot(2, 3, 1)
# plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

# plt.subplot(2, 3, 2)
# plt.imshow(b, cmap="Blues")

# plt.subplot(2, 3, 3)
# plt.imshow(g, cmap="Greens")

# plt.subplot(2, 3, 4)
# plt.imshow(r, cmap="Reds")


# plt.tight_layout()
# plt.show()

# # resize image
# joko = cv2.imread("cv\djoko_air.jpg")
# print(joko.shape)
# joko = cv2.resize(joko, dsize=(540, 960))
# print(joko.shape)

# add annotation
# origin
sea = cv2.imread("cv\sea.jpg")
sea = cv2.cvtColor(sea, cv2.COLOR_BGR2RGB)
print(sea.shape)
plt.subplot(2, 2, 1)
plt.imshow(sea)

# line
sea_line = sea.copy()
cv2.line(
    sea_line,
    pt1=(200, 50),
    pt2=(400, 50),
    color=(255, 255, 0),
    thickness=2,
    lineType=cv2.LINE_AA,
)
plt.subplot(2, 2, 2)
plt.imshow(sea_line)

sea_circle = sea.copy()
cv2.circle(
    sea_circle,
    center=(290, 485),
    radius=30,
    color=(0, 0, 255),
    thickness=2,
    lineType=cv2.LINE_AA,
)
plt.subplot(2, 2, 3)
plt.imshow(sea_circle)

sea_rectangle = sea.copy()
cv2.rectangle(
    sea_rectangle,
    (350, 310),
    (550, 430),
    (255, 255, 0),
    thickness=2,
    lineType=cv2.LINE_AA,
)
plt.subplot(2, 2, 4)
plt.imshow(sea_rectangle)

sea_text = sea.copy()
text = "Sample, 6/12/2023"
cv2.putText(
    sea_text,
    text=text,
    org=(220, 580),
    fontFace=cv2.FONT_HERSHEY_PLAIN,
    fontScale=2.3,
    color=(0, 255, 255),
    thickness=2,
    lineType=cv2.LINE_AA,
)
plt.subplot(2, 2, 4)
plt.imshow(sea_text)
plt.show()
