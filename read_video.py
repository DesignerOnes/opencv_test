import argparse

import cv2

parser = argparse.ArgumentParser()
parser.add_argument("index_camera", help="camera id", type=int)
args = vars(parser.parse_args())
print(args['index_camera'])

# 获取摄像头视频
capture = cv2.VideoCapture(args['index_camera'])

# 获取帧的宽度
frame_width = capture.get(cv2.CAP_PROP_FRAME_WIDTH)
frame_height = capture.get(cv2.CAP_PROP_FRAME_HEIGHT)

fps = capture.get(cv2.CAP_PROP_FPS)
print(f"width:{frame_width} -> height:{frame_height} --> fps:{fps}")

# 判断摄像头是否打开
if capture.isOpened() is False:
    print("Camera Error")

# 从摄像头读取视频，直到关闭
while capture.isOpened():
    ret, frame = capture.read()
    # 变成灰度图片
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # 显示每一帧，形成视频流
    cv2.imshow("frame", frame)
    cv2.imshow("frame_gray", gray_frame)

    # 键盘输入Q关闭视频
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

# 释放资源
capture.release()
# 关闭窗口
cv2.destroyAllWindows()
