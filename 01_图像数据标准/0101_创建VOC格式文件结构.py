import os

from common import config

if __name__ == '__main__':

    path_root = config['mydataset_root'] + r'/VOCdevkit/VOC2007'

    path_Annotations = r'/Annotations'
    path_ImageSets = r'/ImageSets/Main'
    path_JPEFImages = r'/JPEFImages'
    if not os.path.exists(path_root):
        os.makedirs(path_root + path_Annotations)
        os.makedirs(path_root + path_ImageSets)
        os.makedirs(path_root + path_JPEFImages)