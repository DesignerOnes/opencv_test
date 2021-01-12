import argparse
import cv2

parser = argparse.ArgumentParser()
parser.add_argument("video_output")

args = parser.parse_args()

# 获取摄像头
capture = cv2.VideoCapture(0)

if capture.isOpened() is False:
    print("Error")

# 获取帧的宽度
frame_width = capture.get(cv2.CAP_PROP_FRAME_WIDTH)
frame_height = capture.get(cv2.CAP_PROP_FRAME_HEIGHT)

fps = capture.get(cv2.CAP_PROP_FPS)
print(f"width:{frame_width} -> height:{frame_height} --> fps:{fps}")

fourcc = cv2.VideoWriter_fourcc(*'XVID')
output_gray = cv2.VideoWriter(args.video_output, fourcc, int(fps), (int(frame_width), int(frame_height)), False)

# 读取摄像头
while capture.isOpened():
    ret, frame = capture.read()
    if ret is True:
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        output_gray.write(gray_frame)
        cv2.imshow("gray", gray_frame)
        # 键盘输入Q关闭视频
        if cv2.waitKey(20) & 0xFF == ord('q'):
            break

capture.release()
cv2.destroyAllWindows()
