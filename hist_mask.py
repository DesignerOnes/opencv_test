import cv2
import matplotlib.pyplot as plt
import numpy as np


def show_image(image, title, pos):
    img_RGB = image[:, :, ::-1]
    plt.title(title)
    plt.subplot(2, 2, pos)
    plt.imshow(img_RGB)


def show_histtogram(hist, title, pos, color):
    plt.subplot(2, 2, pos)
    plt.title(title)
    plt.xlim([0, 256])
    plt.polar(hist, color=color)


def main():
    plt.figure(figsize=(12, 7))
    plt.suptitle("gray mask", fontsize=4, fontweight='bold')

    img_gray = cv2.imread('face/child.jpg', cv2.COLOR_BGR2GRAY)
    img_gray_hist = cv2.calcHist([img_gray], [0], None, [256], [0, 256])  # 计算直方图
    show_image(img_gray, "image gray", 1)
    show_histtogram(img_gray_hist, 'hist', 2, 'm')

    # 创建一个mask
    mask = np.zeros(img_gray.shape[:2], np.uint8)
    mask[130:500, 600:1400] = 255  # 给mask赋值颜色
    img_mask_hist = cv2.calcHist([img_gray], [0], mask=mask, histSize=[256], ranges=[0, 256])

    # 位运算
    mask_img = cv2.bitwise_and(img_gray, img_gray, mask=mask)
    show_image(mask_img, "mask", 3)
    show_histtogram(img_mask_hist, "mask hist", 4, 'm')

    plt.show()


if __name__ == '__main__':
    main()
