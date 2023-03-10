import os
from PIL import Image
import glob

from common import project_path, config


# dir1 = line_list[0]  # 图片路径，必须自行修改
dir1=''

need_size = config[config['dataset_like']]
need_width = need_size['width']   # 设置你想缩放的图片宽度的阈值，默认COCO图片格式，不用更改，VOC为500*400
need_height = need_size['height']   # 设置你想缩放的图片宽度的阈值，默认COCO图片格式，不用更改，VOC为500*400

line_list = config['keyword']
for word in line_list:
    dir1 = os.path.join(project_path, config['save_path'],word)
    paths = glob.glob(os.path.join(dir1, '*.jpg'))
    count = 0
    # 输出所有文件和文件夹
    for file in paths:
        fp = open(file, 'rb')
        img = Image.open(fp)
        fp.close()
        width = img.size[0]
        height = img.size[1]
        if (width < need_width) and (height < need_height) or (height < need_width) and (width < need_height):
            os.remove(file)
            count+=1
    print('第三步：'+word + '文件夹图片去除模糊中...')
    print("------------------------------------------")
    print("一共删除了"+str(count)+"张模糊图片")
    print("------------------------------------------\n\n")