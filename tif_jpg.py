import cv2.cv2 as cv
import cv2
import os


path = r'G:\dataset\Massachusetts buildings dataset\test\img'  # 获取图片所在目录
save_path = r'G:\dataset\Massachusetts buildings dataset\test\img\png'

tif_list = [x for x in os.listdir(path) if x.endswith(".tiff")]   # 获取目录中所有tif格式图像列表
for num, i in enumerate(tif_list):      # 遍历列表
    img_path = os.path.join(path, i)
    img = cv.imread(img_path, -1)       #  读取列表中的tif图像
    print('------>', i)
    # cv.imwrite(r'I:\hezhiyu\cut\png\{}'.format(i.split('.')[0]+".png"), img)    # tif 格式转 jpg 并按原名称命名

    cv.imwrite(os.path.join(save_path, '{}'.format(i.split('.')[0] + ".png")), img)
# path = r'I:\data\drone\hk_drone'
#
# jpg_path = r'I:\data\drone\jpg'
#
# for j in range(1, 41):
#     tif_path = path + '\\' + 'group{}'.format(j)
#     imgs = os.listdir(tif_path)
#
#     for i, img in enumerate(imgs):
#
#         img_name = os.path.join(tif_path, img)
#         file = cv2.imread(img_name)
#         save_file = os.path.join(jpg_path, 'group{}_'.format(j) + img.strip('.tiff')+'.jpg')
#         cv2.imwrite(save_file, file)
#         print(j, ':', i)

