'''
一、读取图片
    使用高斯滤波进行图片模糊化
    参数ksize表示高斯核的大小，sigmaX和sigmaY分别表示高斯核在 X 和 Y 方向上的标准差。
二、使用adaptiveThreshold()方法对图片进行二值化操作，函数中的参数大多用于设置自适应二值化的算法和阈值等。
三、保存转换后的图片

经过『v1.0版本』和『v2.0版本』试验，使用上面提到的中值滤波函数cv2.medianBlur()进行模糊化操作最终得到的素描图效果并不好，这里我们尝试使用高斯滤波进行图片模糊化
'''

import cv2

src_image = './src_image/xiao.jpeg'
img_rgb = cv2.imread(src_image)
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2GRAY)

img_gray = cv2.medianBlur(img_gray, 5)
img_edge = cv2.adaptiveThreshold(img_gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, blockSize=3, C=2)

img_blur = cv2.GaussianBlur(img_gray, ksize=(21, 21),sigmaX=0, sigmaY=0)
cv2.divide(img_gray, img_blur, scale=255)


dest_image = "./pic/3.jpg"
cv2.imwrite(dest_image, img_edge)
