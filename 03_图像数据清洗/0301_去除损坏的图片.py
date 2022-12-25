import os
import imghdr
from progressbar import ProgressBar
from common import project_path, config

path = os.path.join(project_path, config['save_path'])
original_images = []

for root, dirs, filenames in os.walk(path):
    for filename in filenames:
        original_images.append(os.path.join(root, filename))
original_images = sorted(original_images)
print('num:', len(original_images))
f = open('check_error.txt', 'w+')
error_images = []
progress = ProgressBar()
for filename in progress(original_images):
    check = imghdr.what(filename)
    if check == None:
        f.write(filename)
        f.write('\n')
        error_images.append(filename)
        os.remove(filename)
print(len(error_images))
f.seek(0)
for s in f:
    print(s)
f.close()