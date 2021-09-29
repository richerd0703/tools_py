import os

import cv2
import matplotlib.pyplot as plt
import numpy as np


def one_pic_padding(srcpath, savepath):
    file_name = os.path.basename(srcpath)
    img = cv2.imread(srcpath, 1)
    print("img size :", img.shape[0], img.shape[1])
    h, w = img.shape[0], img.shape[1]
    new_h, new_w = (h, w)
    if w % 512 != 0:
        new_w = ((w // 512) + 1) * 512
    if h % 512 != 0:
        new_h = ((h // 512) + 1) * 512
    padd_h = new_h - h
    padd_w = new_w - w

    # img2 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    # top_size, bottom_size, left_size, right_size = (24, 0, 24, 0)
    top_size, bottom_size, left_size, right_size = (padd_h, 0, padd_w, 0)
    print("top_size padding :{0} , left_size padding :{1}".format(padd_h, padd_w))

    # replicate = cv2.copyMakeBorder(img, top_size, bottom_size, left_size, right_size, borderType=cv2.BORDER_REPLICATE)
    # reflect = cv2.copyMakeBorder(img, top_size, bottom_size, left_size, right_size,cv2.BORDER_REFLECT)
    # reflect101 = cv2.copyMakeBorder(img, top_size, bottom_size, left_size, right_size, cv2.BORDER_REFLECT_101)
    # wrap = cv2.copyMakeBorder(img, top_size, bottom_size, left_size, right_size, cv2.BORDER_WRAP)
    constant = cv2.copyMakeBorder(img, top_size, bottom_size, left_size, right_size, cv2.BORDER_CONSTANT, value=0)
    plt.imshow(constant)

    cv2.imwrite(os.path.join(savepath, file_name), constant)
    print("after padding size :", constant.shape[0], constant.shape[1])

    # crop
    # cropimg = constant[padd_h:, padd_w:, :]
    # cv2.imwrite("res.png", cropimg)


def padding(path):
    files = os.listdir(path)
    for file in files:
        img = cv2.imread(os.path.join(path, file), 1)
        print(img.shape[0], img.shape[1])
        h, w = img.shape[0], img.shape[1]
        new_h, new_w = (h, w)
        if w % 512 != 0:
            new_w = ((w // 512) + 1) * 512
        if h % 512 != 0:
            new_h = ((h // 512) + 1) * 512
        padd_h = new_h - h
        padd_w = new_w - w

        # img2 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        # top_size, bottom_size, left_size, right_size = (24, 0, 24, 0)
        top_size, bottom_size, left_size, right_size = (padd_h, 0, padd_w, 0)

        # 在图片左边和上边填充 0
        constant = cv2.copyMakeBorder(img, top_size, bottom_size, left_size, right_size, cv2.BORDER_CONSTANT, value=0)
        plt.imshow(constant)
        cv2.imwrite("gongshu.png", constant)
        # plt.imsave("1.png", img2)
        # plt.show()

if __name__ == '__main__':
    src_path = r"D:\code\Road_segmentation\image\7.png"
    save_path = r"D:\code\Road_segmentation\image\res"
    # padding(path)
    one_pic_padding(src_path, save_path)