"""
此代码将给定的两张图片及其标签切分成1024*1024的小图，步长可自行调整
随后会随机分成训练集和验证集，比例亦可随机调整
"""
import os
import numpy as np
from PIL import Image
import cv2 as cv
from tqdm import tqdm
import random
import shutil

Image.MAX_IMAGE_PIXELS = 1000000000000000
TARGET_W, TARGET_H = 256, 256
STEP = 448


def cut_images(image_name, image_path, save_dir, is_show=False):
    # 初始化路径
    image_save_dir = os.path.join(save_dir, "images/")
    if not os.path.exists(image_save_dir): os.makedirs(image_save_dir)
    if is_show:
        label_show_save_dir = os.path.join(save_dir, "labels_show/")
        if not os.path.exists(label_show_save_dir): os.makedirs(label_show_save_dir)

    target_w, target_h = TARGET_W, TARGET_H
    stride = 256
    image = np.asarray(cv.imread(image_path, 1))
    # img = cv2.imread(srcpath, 1)
    h, w = image.shape[0], image.shape[1]
    print("origal size: ", w, h)
    if (w - target_w) % stride:
        new_w = ((w - target_w) // stride + 1) * stride + target_w
    if (h - target_h) % stride:
        new_h = ((h - target_h) // stride + 1) * stride + target_h
    image = cv.copyMakeBorder(image, 0, new_h - h, 0, new_w - w, cv.BORDER_CONSTANT, 0)
    # label = cv.copyMakeBorder(label, 0, new_h - h, 0, new_w - w, cv.BORDER_CONSTANT, 1)
    h, w = image.shape[0], image.shape[1]
    print("padding to : ", w, h)

    def crop(cnt, crop_image):
        _name = image_name.split(".")[0]
        image_save_path = os.path.join(image_save_dir, _name + "_" + str(cnt[1]) + "_" + str(cnt[0]) + ".png")

        cv.imwrite(image_save_path, crop_image)

    h, w = image.shape[0], image.shape[1]
    for i in tqdm(range((w - target_w) // stride + 1)):
        for j in range((h - target_h) // stride + 1):
            topleft_x = i * stride
            topleft_y = j * stride
            crop_image = image[topleft_y:topleft_y + target_h, topleft_x:topleft_x + target_w]
            # crop_label = label[topleft_y:topleft_y + target_h, topleft_x:topleft_x + target_w]

            crop((i, j), crop_image)


if __name__ == "__main__":
    data_dir = r"D:\test\temp"
    img_name1 = "1.png"
    cut_images(img_name1, os.path.join(data_dir, img_name1), data_dir)


