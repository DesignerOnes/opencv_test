import argparse

import cv2

parser = argparse.ArgumentParser()
parser.add_argument("img_input", help="read image")
parser.add_argument("img_output", help="save image")

args = vars(parser.parse_args())

img = cv2.imread(args['img_input'])
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imwrite(args['img_output'], img_gray)

cv2.imshow("img",img)
cv2.imshow("img_gray",img_gray)

cv2.waitKey(0)

cv2.destroyAllWindows()
