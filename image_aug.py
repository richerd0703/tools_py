import os
import random
import glob
import numpy as np
import imgaug as ia
import imgaug.augmenters as iaa
from imgaug.augmentables.segmaps import SegmentationMapsOnImage
from PIL import Image


class ImageAugmentation(object):
    def __init__(self, image_aug_dir, segmentationClass_aug_dir, image_start_num=1):
        self.image_aug_dir = image_aug_dir
        self.segmentationClass_aug_dir = segmentationClass_aug_dir
        self.image_start_num = image_start_num  # 增强后图片的起始编号
        self.seed_set()
        if not os.path.exists(self.image_aug_dir):
            os.mkdir(self.image_aug_dir)
        if not os.path.exists(self.segmentationClass_aug_dir):
            os.mkdir(self.segmentationClass_aug_dir)

    def seed_set(self, seed=1):
        np.random.seed(seed)
        random.seed(seed)
        ia.seed(seed)

    def array2p_mode(self, alpha_channel):
        """alpha_channel is a binary image."""
        # assert set(alpha_channel.flatten().tolist()) == {0, 1}, "alpha_channel is a binary image."
        alpha_channel[alpha_channel == 1] = 128
        h, w = alpha_channel.shape
        image_arr = np.zeros((h, w, 3))
        image_arr[:, :, 0] = alpha_channel
        img = Image.fromarray(np.uint8(image_arr))
        img_p = img.convert("P")
        return img_p

    def augmentor(self, image):
        height, width, _ = image.shape
        # resize = iaa.Sequential([
        #     iaa.Resize({"height": int(height/2), "width": int(width/2)}),
        # ])  # 缩放

        fliplr_flipud = iaa.Sequential([
            iaa.Fliplr(),
            iaa.Flipud(),
        ])  # 左右+上下翻转

        # rotate = iaa.Sequential([
        #     iaa.Affine(rotate=(-70, 70))
        # ])  # 旋转
        #
        # translate = iaa.Sequential([
        #     iaa.Affine(translate_percent=(0.2, 0.35))
        # ])  # 平移

        # crop_and_pad = iaa.Sequential([
        #     iaa.CropAndPad(percent=(-0.25, 0), keep_size=False),
        # ])  # 裁剪

        # rotate_and_crop = iaa.Sequential([
        #     iaa.Affine(rotate=45),
        #     iaa.CropAndPad(percent=(-0.25, 0), keep_size=False)
        # ])  # 旋转 + 裁剪

        guassian_blur = iaa.Sequential([
            iaa.GaussianBlur(sigma=(2, 3)),
        ])  # 增加高斯噪声

        sharpen = iaa.Sequential([
            iaa.Sharpen(alpha=(0, 1.0), lightness=(0.75, 1.5)),
        ])  # 锐化

        piecewise_affine = iaa.Sequential([
            iaa.PiecewiseAffine(scale=(0.01, 0.05)),
        ])  # 扭曲图像的局部区域

        # ops = [fliplr_flipud, guassian_blur, sharpen, piecewise_affine]
        ops = piecewise_affine
        #      镜像+上下翻转、   旋转、    xy平移、     高斯平滑         锐化         扭曲
        return ops


    def augment_img(self, image_name, segmap_name):
        # 1.Load an image.
        img_name = image_name.split('\\')[-1]
        image = Image.open(image_name)  # RGB
        segmap = Image.open(segmap_name)  # P

        name = f"{self.image_start_num:04d}"
        # image.save(self.image_aug_dir + str(int(name)) + ".png")
        # segmap.save(self.segmentationClass_aug_dir + str(int(name)) + ".png")
        # for i in range(5):
        # image.save(self.image_aug_dir + img_name.split('.')[0] + '_' + str(i) + '.png')
        # segmap.save(self.segmentationClass_aug_dir + img_name.split('.')[0] + '_' + str(i) + '.png')
        self.image_start_num += 1

        image = np.array(image)
        segmap = SegmentationMapsOnImage(np.array(segmap), shape=image.shape)

        # 2. define the ops
        ops = self.augmentor(image)

        # 3.execute ths ops
        for _, op in enumerate(ops):
            name = f"{self.image_start_num:04d}"
            print(f"当前增强了{self.image_start_num:04d}张数据...")
            images_aug_i, segmaps_aug_i = op(image=image, segmentation_maps=segmap)
            images_aug_i = Image.fromarray(images_aug_i)
            images_aug_i.save(self.image_aug_dir + str(int(name)) + ".png")
            segmaps_aug_i_ = segmaps_aug_i.get_arr()
            segmaps_aug_i_[segmaps_aug_i_ > 0] = 1
            segmaps_aug_i_ = self.array2p_mode(segmaps_aug_i_)
            segmaps_aug_i_.save(self.segmentationClass_aug_dir + str(int(name)) + ".png")
            self.image_start_num += 1

    def augment_images(self, image_dir, segmap_dir):
        image_names = sorted(glob.glob(image_dir + "*"))
        segmap_names = sorted(glob.glob(segmap_dir + "*"))
        image_num = len(image_names)

        count = 1
        for image_name, segmap_name in zip(image_names, segmap_names):
            print("*"*20, f"正在增强第【{count:04d}/{image_num:04d}】张图片...", "*"*20)
            self.augment_img(image_name, segmap_name)
            count += 1


if __name__ == "__main__":
    image_dir = r"I:\test\remove\aug\img/"                                 # image目录，必须是RGB
    segmap_dir = r"I:\test\remove\aug\lab/"                         # segmap目录，必须是p模式的图片
    image_aug_dir = r"I:\test\remove\aug\after\img/"                           # image增强后存放目录
    segmentationClass_aug_dir = r"I:\test\remove\aug\after\lab/"  # segmap增强后存放目录

    image_start_num = 1
    image_augmentation = ImageAugmentation(image_aug_dir, segmentationClass_aug_dir, image_start_num)
    image_augmentation.augment_images(image_dir, segmap_dir)


 # -*- coding: utf-8 -*-

# import Augmentor
# import glob
# import os
# import random
# from keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img
#
# train_path = 'I:/test/add/aug/image'
# groud_truth_path = 'I:/test/add/aug/label'
# img_type = 'png'
# train_tmp_path = 'I:/test/add/aug/img_aug'
# mask_tmp_path = 'I:/test/add/aug/label_aug'
#
#
# def start(train_path,groud_truth_path):
#     train_img = glob.glob(train_path+'/*.'+img_type)
#     masks = glob.glob(groud_truth_path+'/*.'+img_type)
#
#     if len(train_img) != len(masks):
#         print ("trains can't match masks")
#         return 0
#     for i in range(len(train_img)):
#         train_img_tmp_path = train_tmp_path + '/'+str(i)
#         if not os.path.lexists(train_img_tmp_path):
#             os.mkdir(train_img_tmp_path)
#         img = load_img(train_path+'/'+str(i)+'.'+img_type)
#         x_t = img_to_array(img)
#         img_tmp = array_to_img(x_t)
#         img_tmp.save(train_img_tmp_path+'/'+str(i)+'.'+img_type)
#
#         mask_img_tmp_path =mask_tmp_path +'/'+str(i)
#         if not os.path.lexists(mask_img_tmp_path):
#             os.mkdir(mask_img_tmp_path)
#         mask = load_img(groud_truth_path+'/'+str(i)+'.'+img_type)
#         x_l = img_to_array(mask)
#         mask_tmp = array_to_img(x_l)
#         mask_tmp.save(mask_img_tmp_path+'/'+str(i)+'.'+img_type)
#         print ("%s folder has been created!"%str(i))
#     return i+1
#
#
# def doAugment(num):
#     sum = 0
#     for i in range(num):
#         p = Augmentor.Pipeline(train_tmp_path+'/'+str(i))
#         p.ground_truth(mask_tmp_path+'/'+str(i))
#         p.rotate(probability=0.5, max_left_rotation=5, max_right_rotation=5)#旋转
#         p.flip_left_right(probability=0.5)#按概率左右翻转
#         p.zoom_random(probability=0.6, percentage_area=0.99)#随即将一定比例面积的图形放大至全图
#         p.flip_top_bottom(probability=0.6)#按概率随即上下翻转
#         p.random_distortion(probability=0.8,grid_width=10,grid_height=10, magnitude=20)#小块变形
#         count = random.randint(40, 60)
#         print("\nNo.%s data is being augmented and %s data will be created"%(i,count))
#         sum = sum + count
#         p.sample(count)
#         print("Done")
#     print("%s pairs of data has been created totally"%sum)
#
#
# a = start(train_path, groud_truth_path)
# doAugment(4)



