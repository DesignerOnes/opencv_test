import cv2

img = cv2.imread("face/child.jpg")
print(img.shape)  # 读取图片的形状（width，height，channel）   打印如下 (1261, 1920, 3)
img_type = img.dtype
print(img_type)
# 图片的BGR (6,40)这个点的bgr
(b, g, r) = img[6, 40]
print(b, g, r)

# 显示图片
cv2.imshow("image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
