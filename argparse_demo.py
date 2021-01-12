import argparse

import cv2

parser = argparse.ArgumentParser()  # 获取所有的参数
# parser.add_argument("n1", help="第一个参数", type=int)
# parser.add_argument("n2", help="第二个参数", type=int)
parser.add_argument("path_image", help='图片的路径')
args = parser.parse_args()  # 解析所有的参数
print(args.n1)

#获取图片的方式1
img = cv2.imread(args.path_image)
cv2.imshow("log1", img)

#获取图片的方式2
args_dict = vars(args)
img2 = cv2.imread(args_dict['path_image'])
cv2.imshow("log2", img2)

cv2.waitKey(0)
cv2.destroyAllWindows()