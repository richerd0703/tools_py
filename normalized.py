import numpy as np
import cv2
import random
import os
# calculate means and std
from tqdm import tqdm
import numpy as np
import random

train_txt_path = r'I:\data\oil_tank\ImageSets\Segmentation\all.txt'  # 数据集images name索引txt
image_prefix = r'I:\data\oil_tank\JPEGImages'  # 图片

CNum = 500  # select images 取前10000张图片作为计算样本

img_h, img_w = 512, 512
imgs = np.zeros([img_w, img_h, 3, 1])
means, stdevs = [], []

with open(train_txt_path, 'r') as f:
    lines = f.readlines()  # 读取全部image name
    random.shuffle(lines)  # shuffle images

    for i in tqdm(range(CNum)):
        file_name = lines[i].strip() + '.TIF'
        img_path = os.path.join(image_prefix, file_name)

        img = cv2.imread(img_path)
        img = cv2.resize(img, (img_h, img_w))  # 将图片进行裁剪[32,32]
        img = img[:, :, :, np.newaxis]
        imgs = np.concatenate((imgs, img), axis=3)
#         print(i)

imgs = imgs.astype(np.float32) / 255.

for i in tqdm(range(3)):
    pixels = imgs[:, :, i, :].ravel()  # flatten
    means.append(np.mean(pixels))
    stdevs.append(np.std(pixels))

# cv2 : BGR
means.reverse()  # BGR --> RGB
stdevs.reverse()

print("normMean = {}".format(means))
print("normStd = {}".format(stdevs))
print('transforms.Normalize(normMean = {}, normStd = {})'.format(means, stdevs))


# 文件写入TXT

# paths = r'G:\Unet\\Medical_Datasets\Images'
# f = open(r'G:\Unet\\Medical_Datasets\ImageSets\Segmentation\train.txt', 'w')  # 只写文件名
# filenames = os.listdir(paths)
# count = 0
# for filename in filenames:
#     if os.path.splitext(filename)[1] == '.png':
#         # out_path = "phoneProject/img/" + filename
#         out_path = filename.split('.')[0]
#         count += 1
#         print(out_path, ": ", count)
#         #f.writable(out_path+'\n')
#         f.write(out_path+'\n')
# f.close()
