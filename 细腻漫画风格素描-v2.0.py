'''
一、读取图片
二、使用adaptiveThreshold()方法对图片进行二值化操作，函数中的参数大多用于设置自适应二值化的算法和阈值等。
三、保存转换后的图片

从『v1.0版本』转换后的图片来看，虽然大概轮廓没有问题，但是效果很不理想，并不能够称之为素描图。
这主要是因为adaptiveThreshold()方法会在图片的每一个小的局部区域内进行二值化操作，因此对于一些清晰度比较高、色彩区分比较细腻的图片，就会出现上面这样密密麻麻的情况。
这个问题解决起来其实也很简单，只要在进行二值化之前使用medianBlur()方法对原图进行模糊化就可以了。
'''

import cv2

src_image = './src_image/xiao.jpeg'
img_rgb = cv2.imread(src_image)
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2GRAY)

img_gray = cv2.medianBlur(img_gray, 5)
img_edge = cv2.adaptiveThreshold(img_gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, blockSize=3, C=2)

dest_image = "./pic/2.jpg"
cv2.imwrite(dest_image, img_edge)
