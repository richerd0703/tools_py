from PIL import Image
import random

im = Image.open("1.png")
img_size = im.size
m = img_size[0]    #读取图片的宽度
n = img_size[1]     #读取图片的高度
w = 512                  #设置你要裁剪的小图的宽度
h = 1024                   #设置你要裁剪的小图的高度
for i in range(3):         #裁剪为100张随机的小图
    # x = random.randint(0, m-w)       #裁剪起点的x坐标范围
    # y = random.randint(0, n-h)        #裁剪起点的y坐标范围
    region = im.crop((0, 0, w, h))     #裁剪区域

    region.save("1_"+str(i)+".png")      #str(i)是裁剪后的编号，此处是0到99
