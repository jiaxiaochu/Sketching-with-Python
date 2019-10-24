'''
一、读取图片
二、使用adaptiveThreshold()方法对图片进行二值化操作，函数中的参数大多用于设置自适应二值化的算法和阈值等。
三、保存转换后的图片
'''

import cv2

src_image = './src_image/xiao.jpeg'
img_rgb = cv2.imread(src_image)
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2GRAY)

img_edge = cv2.adaptiveThreshold(img_gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, blockSize=3, C=2)

dest_image = "./pic/1.jpg"
cv2.imwrite(dest_image, img_edge)
