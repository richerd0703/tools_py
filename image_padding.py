import cv2
import matplotlib.pyplot as plt
import numpy as np
import os


path = r'G:\image\png'
fileset = []
fileLists = os.listdir(path)
for file in fileLists:
    if file.split(".")[-1] == ("png"):
        # print(file)
        whole_path = path + "\\" + file
        fileset.append(whole_path)
num = len(fileset)
for i in range(len(fileset)):
    print(fileset[i], '-----', i)
    # img = cv2.imread(fileset[i], 0)  # 灰度图

    img = cv2.imread(fileset[i], 1)  # 彩图
    # img = cv2.imread(r"‪I:\map_cut\test\1\20_2.png")
    # img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    top_size, bottom_size, left_size, right_size = (1, 0, 1, 0)

    replicate = cv2.copyMakeBorder(img, top_size, bottom_size, left_size, right_size, borderType=cv2.BORDER_REPLICATE)
    # reflect = cv2.copyMakeBorder(img, top_size, bottom_size, left_size, right_size, cv2.BORDER_REFLECT)
    # reflect101 = cv2.copyMakeBorder(img, top_size, bottom_size, left_size, right_size, cv2.BORDER_REFLECT_101)
    # wrap = cv2.copyMakeBorder(img, top_size, bottom_size, left_size, right_size, cv2.BORDER_WRAP)
    # constant = cv2.copyMakeBorder(img, top_size, bottom_size, left_size, right_size, cv2.BORDER_CONSTANT, value=0)
    name = fileset[i].split('\\')[-1]
    cv2.imwrite(r"G:\image\png\padding\{}".format(name), replicate)
    # plt.imshow(img)
    # plt.show()
    #
    # plt.subplot(231), plt.imshow(img, 'gray'), plt.title('ORIGINAL')
    # plt.subplot(232), plt.imshow(replicate, 'gray'), plt.title('REPLICATE')
    # # plt.subplot(233), plt.imshow(reflect, 'gray'), plt.title('REFLECT')
    # # plt.subplot(234), plt.imshow(reflect101, 'gray'), plt.title('REFLECT_101')
    # # plt.subplot(235), plt.imshow(wrap, 'gray'), plt.title('WRAP')
    # # plt.subplot(236), plt.imshow(constant, 'gray'), plt.title('CONSTANT')
    #
    # plt.show()
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

