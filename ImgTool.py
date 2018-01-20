#! /usr/bin/env python
# -*- coding: utf-8 -*-
#author sduxiaoma

from PIL import Image


#缩小图片
def ImgThumbnail(img_path, saved_Name):
    # 打开一个jpg图像文件，注意是当前路径:
    im = Image.open(img_path)
    # 获得图像尺寸:
    w, h = im.size
    print 'Original image size: %sx%s' % (w, h)
    # 缩放到50%:
    im.thumbnail((w // 2, h // 2))
    print 'Resize image to: %sx%s' % (w // 2, h // 2)
    # 把缩放后的图像用jpeg格式保存:
    im.save(saved_Name, 'jpeg')


if __name__ == '__main__':
    print 'start'
    ImgThumbnail('./image/input/hand.jpg', './image/output/save.jpg')
    print 'end'