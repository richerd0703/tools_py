import cv2
import os
import shutil


sourcefile_dir = r"D:\dataset\cskin\flw\train_up2400_down1000_flw_1024\select_label"
destfile_dir = r"D:\dataset\cskin\flw\train_up2400_down1000_flw_1024\image"
destfile_dir1 = r"D:\dataset\cskin\flw\train_up2400_down1000_flw_1024\select_image"
for root, dirs, filenames in os.walk(sourcefile_dir):
    n = 1
    for filename in filenames:
        file = filename[:-4]+'.jpg'
        print(n)
        n += 1
        # img = cv2.imread("H:\\2c_zw\\test\\label\\11.png")
        # cv2.bitwise_not(img, img)
        # cv2.imwrite("H:\\2c_zw\\test\\label\\111.png",img)
        # # cv2.imshow('a',img)
        # # cv2.waitKey(0)
        # exit(0)
        # if len(img[img == 255]) / (1024 * 1024 * 3)==0.0:
        shutil.move(os.path.join(destfile_dir, file),destfile_dir1)