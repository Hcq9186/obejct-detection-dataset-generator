import os

from common import config

if __name__ == '__main__':

    if config['dataset_like'] == 'coco':
        path_root = config['mydataset_root'] + r'/coco'

        path_annotations = r'/annotations'
        path_train2017 = r'/train2017'
        path_val2017 = r'/val2017'
        path_test2017 = r'/test2017'
        if not os.path.exists(path_root):
            os.makedirs(path_root + path_annotations)
            os.makedirs(path_root + path_train2017)
            os.makedirs(path_root + path_val2017)
            os.makedirs(path_root + path_test2017)
    elif config['dataset_like'] == 'voc':
        path_root = config['mydataset_root'] + r'/VOCdevkit/VOC2007'

        path_Annotations = r'/Annotations'
        path_ImageSets = r'/ImageSets/Main'
        path_JPEFImages = r'/JPEFImages'
        if not os.path.exists(path_root):
            os.makedirs(path_root + path_Annotations)
            os.makedirs(path_root + path_ImageSets)
            os.makedirs(path_root + path_JPEFImages)