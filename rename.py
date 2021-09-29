# -*- coding: utf-8 -*-
import os
#设定文件路径
path = r'I:\test\remove\lab1'
# "戴村镇", "_dcz"  "党湾镇", "_dwz" "益农镇", "_ynz" "进化镇", "_jhz" "新湾街道", "_xwjd"
#对目录下的文件进行遍历 "所前镇", "_sqz" "新塘街道(0)", "_xtjd" "河上镇", "_hsz"
for file in os.listdir(path):
#判断是否是文件
    if os.path.isfile(os.path.join(path,file))==True:
#设置新文件名
        name = file
        new_name = file.replace("_line", "")
#重命名
        os.rename(os.path.join(path, file), os.path.join(path, new_name))

        print('running ----->', name)
#结束
print ("End")