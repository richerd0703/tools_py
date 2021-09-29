import os
import cv2
'''
将24位的label转为8位
'''
bacepath = r"G:\test\xihu+beijing\train\label"
savepath = r'G:\test\xihu+beijing\train\label'
f_n = os.listdir(bacepath)
for n in f_n:
    imdir = bacepath + '\\' + n
    print(n)
    img = cv2.imread(imdir)

    cropped = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imwrite(savepath + '\\' + n.split('.')[0] + '.png', cropped)  # NOT CAHNGE THE TYPE