# import cv2
# import os
#
# if __name__ == "__main__":
#     #图像文件原始路径
#     path = r"I:\test\1\image"
#     listdir = os.listdir(path)
#     # 新建split文件夹用于保存
#     newdir = os.path.join(path, 'split')
#     if (os.path.exists(newdir) == False):
#         os.mkdir(newdir)
#     for i in listdir:
#         # if i.split('.')[1] == "png" or i.split('.')[1] == "JPG" or i.split('.')[1] == "jpg" :
#         if i.split('.')[1] == 'TIF':
#             filepath = os.path.join(path, i)
#
#             filename = i.split('.')[0]
#             leftpath1 = os.path.join(newdir, filename) + "_left1.png"
#             leftpath2 = os.path.join(newdir, filename) + "_left2.png"
#             rightpath1 = os.path.join(newdir, filename) + "_right1.png"
#             rightpath2 = os.path.join(newdir, filename) + "_right2.png"
#             img = cv2.imread(filepath)
#             [h, w] = img.shape[:2]
#             print(filepath, (h, w))
#             # l1img = img[:int(h / 2), :int(w / 2), :]
#             # l2img=img[int(h /2+1):, :int(w / 2), :]
#             # r1img = img[:int(h / 2), int(w / 2 + 1):, :]
#             # r2img = img[int(h /2+1):, int(w / 2 + 1):, :]
#             l1img = img[0: 512, 0: 512, :]
#             l2img = img[400: 912, 0: 512, :]
#             r1img = img[0: 512, 400: 912, :]
#             r2img = img[400: 912, 400: 912, :]
#             cv2.imwrite(leftpath1, l1img)
#             cv2.imwrite(leftpath2, l2img)
#             cv2.imwrite(rightpath1, r1img)
#             cv2.imwrite(rightpath2, r2img)

net_struct = {
    'alexnet': {'net': [[11, 4, 0], [3, 2, 0], [5, 1, 2], [3, 2, 0], [3, 1, 1], [3, 1, 1], [3, 1, 1], [3, 2, 0]],
                'name': ['conv1', 'pool1', 'conv2', 'pool2', 'conv3', 'conv4', 'conv5', 'pool5']},
    'vgg16': {'net': [[3, 1, 1], [3, 1, 1], [2, 2, 0], [3, 1, 1], [3, 1, 1], [2, 2, 0], [3, 1, 1], [3, 1, 1], [3, 1, 1],
                      [2, 2, 0], [3, 1, 1], [3, 1, 1], [3, 1, 1], [2, 2, 0], [3, 1, 1], [3, 1, 1], [3, 1, 1],
                      [2, 2, 0]],
              'name': ['conv1_1', 'conv1_2', 'pool1', 'conv2_1', 'conv2_2', 'pool2', 'conv3_1', 'conv3_2',
                       'conv3_3', 'pool3', 'conv4_1', 'conv4_2', 'conv4_3', 'pool4', 'conv5_1', 'conv5_2', 'conv5_3',
                       'pool5']},
    'zf-5': {'net': [[7, 2, 3], [3, 2, 1], [5, 2, 2], [3, 2, 1], [3, 1, 1], [3, 1, 1], [3, 1, 1]],
             'name': ['conv1', 'pool1', 'conv2', 'pool2', 'conv3', 'conv4', 'conv5']}}

imsize = 224


def outFromIn(isz, net, layernum):
    totstride = 1
    insize = isz
    for layer in range(layernum):
        fsize, stride, pad = net[layer]
        outsize = (insize - fsize + 2 * pad) / stride + 1
        insize = outsize
        totstride = totstride * stride
    return outsize, totstride


def inFromOut(net, layernum):
    RF = 1
    for layer in reversed(range(layernum)):
        fsize, stride, pad = net[layer]
        RF = ((RF - 1) * stride) + fsize
    return RF


if __name__ == '__main__':
    print("layer output sizes given image = %dx%d" % (imsize, imsize))

    for net in net_struct.keys():
        print('************net structrue name is %s**************' % net)
        for i in range(len(net_struct[net]['net'])):
            p = outFromIn(imsize, net_struct[net]['net'], i + 1)
            rf = inFromOut(net_struct[net]['net'], i + 1)
            print("Layer Name = %s, Output size = %3d, Stride = % 3d, RF size = %3d" % (
            net_struct[net]['name'][i], p[0], p[1], rf))
