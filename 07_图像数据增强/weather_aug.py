import cv2
from imgaug import augmenters as iaa
import os

# sometimes = lambda aug: iaa.Sometimes(0.5, aug)   # 所有情况的 50% 中应用给定的增强器

seq = iaa.Sequential([
    # 选择2到3种方法做变换
    iaa.SomeOf((2, 3),
               [
                   iaa.imgcorruptlike.MotionBlur(severity=(1, 2)),  # 运动模糊
                   # iaa.Clouds(),  # 云雾
                   iaa.imgcorruptlike.Fog(severity=1),  # 多雾/霜
                   # iaa.imgcorruptlike.Snow(severity=2),  # 下雨、大雪
                   iaa.Rain(drop_size=(0.10, 0.15), speed=(0.1, 0.2)),  # 雨
                   iaa.Snowflakes(flake_size=(0.1, 0.4), speed=(0.01, 0.03)), # 雪点
                   # iaa.FastSnowyLandscape(lightness_threshold=(100, 255),lightness_multiplier=(1.5, 2.0)), # 雪地   亮度阈值是从 uniform(100, 255)（每张图像）和来自 uniform(1.5, 2.0)（每张图像）的乘数采样的。 这似乎产生了良好而多样的结果。
                   # iaa.imgcorruptlike.Spatter(severity=5),  # 溅 123水滴、45泥

                   # 对比度 亮度 饱和度 选其一
                   iaa.SomeOf((1, 1),
                       [
                           iaa.imgaug.augmenters.contrast.LinearContrast((0.5, 2.0), per_channel=0.5),  # 对比度变为原来的一半或者二倍
                           iaa.imgcorruptlike.Brightness(severity=(1, 2)),  # 亮度增加
                           iaa.imgcorruptlike.Saturate(severity=(1, 3)),  # 色彩饱和度
                       ]
                   )
               ],
               # 随机顺序运行augmentations
               random_order=True
               )
], random_order=True)  # 随机运行augmenters数量

# 图片文件相关路径
path = '/data/objectDetection/dataset/mydataset/VOCdevkit/VOC2007/JPEGImages/'
savedpath = '/data/objectDetection/dataset/mydataset/VOCdevkit/VOC2007/output/'

imglist = []
filelist = os.listdir(path)

# 遍历要增强的文件夹，把所有的图片保存在imglist中
for item in filelist:
    img = cv2.imread(path + item)
    # print('item is ',item)
    # print('img is ',img)
    # images = load_batch(batch_idx)
    imglist.append(img)
# print('imglist is ' ,imglist)
print('all the picture have been appent to imglist')


for count in range(1):
    images_aug = seq.augment_images(imglist)
    for index in range(len(images_aug)):
        # 保存图片 文件名和源文件相同
        filename = str(filelist[index])
        cv2.imwrite(savedpath + filename, images_aug[index])
        print('image of count%s index%s has been writen' % (count, index))

