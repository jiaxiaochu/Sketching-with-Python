# 用Python做素描图——Sketching with Python
import cv2

# 一、读取图片
ima_path = "./src_image/xiao.jpeg"
img_rgb = cv2.imread(ima_path)
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2GRAY)  # 将读取的图片转化为灰度图
# img_gray = cv2.medianBlur(img_gray, 5)
img_blur = cv2.GaussianBlur(img_gray, ksize=(21, 21), sigmaX=0, sigmaY=0)

# 使用高斯滤波进行图片模糊化
# 参数ksize表示高斯核的大小，sigmaX和sigmaY分别表示高斯核在 X 和 Y 方向上的标准差。


# 二、使用adaptiveThreshold()方法对图片进行二值化操作，函数中的参数大多用于设置自适应二值化的算法和阈值等。
img_edge = cv2.adaptiveThreshold(img_gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, blockSize=3, C=2)
# img_edge = cv2.adaptiveThreshold(img_gray, 255,
#                                  cv2.ADAPTIVE_THRESH_MEAN_C,
#                                  cv2.THRESH_BINARY, blockSize=3, C=2)
# img_blur = cv2.GaussianBlur(img_gray, ksize=(21, 21),sigmaX=0, sigmaY=0)
cv2.divide(img_gray, img_blur, scale=255)

# 三、保存转换后的图片
dest_image = './pic/qqq.jpg'
cv2.imwrite(dest_image, img_edge)
