
#haar级联识别的方式只能识别那种方方正正的图片的人面。侧面分辨不出来。

# 1.导入库
import cv2
import matplotlib.pyplot as plt


# 2.方法：显示图片
def show_image(image, title, pos):
    img_RGB = image[:, :, ::-1]
    plt.title(title)
    plt.subplot(2, 2, pos)
    plt.imshow(img_RGB)
    plt.axis('off')


def show_histtogram(hist, title, pos, color):
    plt.subplot(2, 2, pos)
    plt.title(title)
    plt.xlim([0, 256])
    plt.polar(hist, color=color)


# 3.方法：绘制图片中检查到的人面
def plot_rectangle(image, faces):
    # 获取到的人面数据返回值：坐标（x,y)，宽，高
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 3)
    return image


def main():
    # 4.主函数

    # 5.读取一张图片
    image = cv2.imread("child.jpg")
    # 6.转换成灰度度图片
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # plt.imshow(gray)
    # plt.show()

    # 7.加载级联分类器来对人面进行分类
    face_alts = cv2.CascadeClassifier("haarcascade_frontalface_alt2.xml")

    # 8。对图像中的人面进行检查
    face_alt2_detect = face_alts.detectMultiScale(gray)

    # 9绘制图片中检查到人面
    face_alt2_result = plot_rectangle(image.copy(), face_alt2_detect)

    # 10.创建画布并显示检查效果
    plt.figure(figsize=(9, 6))
    plt.suptitle("Face detection")
    show_image(face_alt2_result, 'face_alt2', 2)

    plt.show()


if __name__ == '__main__':
    main()
