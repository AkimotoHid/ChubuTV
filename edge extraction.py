import cv2
import numpy as np

img = cv2.imread('test_data0.jpg')

# BGR -> グレースケール
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# エッジ抽出 (Canny)
edges = cv2.Canny(gray, 1, 100, apertureSize=3)
cv2.imwrite('edges.png', edges)

# 膨張処理
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
edges = cv2.dilate(edges, kernel)

# 輪郭抽出
contours, hierarchy = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# 面積でフィルタリング
rects = []
if hierarchy is not None and len(hierarchy) > 0:
    for cnt, hrchy in zip(contours, hierarchy[0]):
        if cv2.contourArea(cnt) < 1900:
            continue
        if hrchy[3] == -1:
            continue  # ルートノードは除く
        # 輪郭を囲む長方形を計算する。
        rect = cv2.minAreaRect(cnt)
        rect_points = cv2.boxPoints(rect).astype(int)
        rects.append(rect_points)

# x-y 順でソート
rects = sorted(rects, key=lambda x: (x[0][1], x[0][0]))

# 追加された部分: 取り出した四角形の座標をプレーンな画像に描画する
canvas = np.zeros_like(img)
for i, rect in enumerate(rects):
    color = np.random.randint(0, 255, 3).tolist()
    cv2.drawContours(canvas, rects, i, color, 2)
    cv2.putText(canvas, str(i), tuple(rect[0]), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 3)
cv2.imwrite('canvas.jpg', canvas)

# 描画する。
for i, rect in enumerate(rects):
    color = np.random.randint(0, 255, 3).tolist()
    cv2.drawContours(img, rects, i, color, 2)
    cv2.putText(img, str(i), tuple(rect[0]), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 3)

    print('rect:\n', rect)

cv2.imwrite('img.jpg', img)
