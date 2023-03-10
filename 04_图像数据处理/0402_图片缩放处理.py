import os
from PIL import Image
import os.path

from PIL.Image import Resampling

from common import config, project_path

'''修改图片文件大小、file_path：文件夹路径；jpgfile：图片文件；savedir：修改后要保存的路径'''


def convertjpg(file_path, jpgfile, savedir, width_new, height_new):
    img = Image.open(file_path + jpgfile)
    width, height = img.size
    if width < height and width_new > height_new or width > height and width_new < height_new:
        t = width_new
        width_new = height_new
        height_new = t
    img = img.convert('RGB')
    # 判断长宽比
    if width / height >= width_new / height_new:
        new_img = img.resize((width_new, int(height * width_new / width)), Resampling.BICUBIC)
    else:
        new_img = img.resize((int(width * height_new / height), height_new), Resampling.BICUBIC)
    return new_img.save(os.path.join(savedir, jpgfile))

'''循环遍历路径下图片文件，并修改其大小'''
def modifyjpgSize(file_path, saveDir, width_new, height_new):
    filelist = os.listdir(file_path)
    for jpgfile in filelist:
        convertjpg(file_path, jpgfile, saveDir, width_new, height_new)


# 读取目录
if __name__ == '__main__':
    need_size = config[config['dataset_like']]
    need_width = need_size['width']  # 设置你想缩放的图片宽度的阈值，默认COCO图片格式，不用更改，VOC为500*400
    need_height = need_size['height']  # 设置你想缩放的图片宽度的阈值，默认COCO图片格式，不用更改，VOC为500*400

    line_list = config['keyword']
    file_path=''

    for word in line_list:
        file_path = os.path.join(project_path, config['mydataset_root'], word) + '/'  # 原图片路径，必须自行修改
        saveDir = os.path.join(project_path, config['mydataset_root'], word)   # 缩放后图片路径，必须自行修改
        filelist = os.listdir(file_path)
        count=0
        for jpgfile in filelist:
            convertjpg(file_path, jpgfile, saveDir, need_width, need_height)
            count+=1
        print('第九步：'+word + '文件夹图片缩放中...')
        print("------------------------------------------------------------")
        print(str(count)+"张图片缩放完成")
        print("------------------------------------------------------------\n\n")
