import os

from common import config


def rename(path, startNumber, fileType):

    seq = "0"
    name1 = seq * 11
    name2 = seq * 10
    name3 = seq * 9
    name4 = seq * 8
    name5 = seq * 7
    name6 = seq * 6
    name7 = seq * 5
    name8 = seq * 4
    name9 = seq * 3
    name10 = seq * 2
    name11 = seq * 1
    filelist = os.listdir(path)
    count = 0
    num = startNumber + count

    for files in filelist:
        Olddir=os.path.join(path,files)
        if os.path.isdir(Olddir):
            continue
        if num in range(0, 10):
            Newdir=os.path.join(path, name1 + str(count + int(startNumber)) + fileType)
        if num in range(10, 100):
            Newdir=os.path.join(path, name2 + str(count + int(startNumber)) + fileType)
        if num in range(100, 1000):
            Newdir=os.path.join(path, name3 + str(count + int(startNumber)) + fileType)
        if num in range(1000, 10000):
            Newdir=os.path.join(path, name4 + str(count + int(startNumber)) + fileType)
        if num in range(10000, 100000):
            Newdir=os.path.join(path, name5 + str(count + int(startNumber)) + fileType)
        if num in range(100000, 1000000):
            Newdir=os.path.join(path, name6 + str(count + int(startNumber)) + fileType)
        if num in range(1000000, 10000000):
            Newdir=os.path.join(path, name7 + str(count + int(startNumber)) + fileType)
        if num in range(10000000, 100000000):
            Newdir=os.path.join(path, name8 + str(count + int(startNumber)) + fileType)
        if num in range(100000000, 1000000000):
            Newdir=os.path.join(path, name9 + str(count + int(startNumber)) + fileType)
        if num in range(1000000000, 10000000000):
            Newdir=os.path.join(path, name10 + str(count + int(startNumber)) + fileType)
        if num in range(10000000000, 100000000000):
            Newdir=os.path.join(path, name11 + str(count + int(startNumber)) + fileType)
        os.rename(Olddir,Newdir)
        count+=1
        print('第七步：' + fileType + '文件重命名中...')
        print("------------------------------------------------------------")
        print("一共修改了"+str(count)+"个文件")
        print("------------------------------------------------------------\n\n")

if __name__ == '__main__':
    rename(config[config['dataset_like']]['annotation_save_path'], config['start_number'], config[config['dataset_like']]['annotation_filetype'])
    rename(config[config['dataset_like']]['pic_save_path'], config['start_number'], 'jpg')

