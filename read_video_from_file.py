import argparse

import cv2

parser = argparse.ArgumentParser()
parser.add_argument("video_file", help="video_file")
args = vars(parser.parse_args())
print(args['video_file'])

# 获取摄像头视频
file = cv2.VideoCapture(args['video_file'])

ret, frame = file.read()  # ret 是否读取到了帧
while ret:
    cv2.imshow("video", frame)
    ret, frame = file.read()
    # 键盘输入Q关闭视频
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

file.release()
cv2.destroyAllWindows()
