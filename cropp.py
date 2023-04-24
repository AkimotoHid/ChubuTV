from pdf2image import convert_from_path
import os
import numpy as np
import cv2
import sys
from PIL import Image

images = convert_from_path(r"test.pdf",poppler_path = r"C:\poppler-23.01.0\Library\bin")
for i in range(len(images)):
          images[i].save('test_data'+str(i)+'.jpg', 'JPEG')
# 画像ファイルの読み込み(カラー画像(3チャンネル)として読み込まれる)
img = cv2.imread('test_data'+str(i)+'.jpg')
height, width, ch = img.shape
# 画素数 = 幅 * 高さ
size = width * height
# 情報表示
print("元画像の幅：", width)
print("元画像の高さ：", height)
print()

cropped= img[0:1000, 0:1000]
#imgをクロップした画像がcroppedに格納される

current_dir = os.getcwd()
# 保存するファイル名
filename = "cropped_data.jpg"
# 画像の保存
cv2.imwrite(os.path.join(current_dir, filename), cropped)
#open cvは日本語に対応していないため、「デスクトップ」が含まれるパスを指定したら動作しない

cv2.imshow('Cropped Image', cropped)
# キー入力待ち(ここで画像が表示される)
cv2.waitKey()