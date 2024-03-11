import os

import cv2
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import paddleseg.transforms as T
from paddleseg.core import predict
from paddleseg.models import HarDNet

execution_path = os.getcwd()


def main(image_path):
    # 标签
    labels = ['bare soil', 'building', 'pavement', 'road', 'vegetation', 'water']
    num_classes = 6

    # 获取待预测图像
    valid_suffix = [
        '.JPEG', '.jpeg', '.JPG', '.jpg', '.BMP', '.bmp', '.PNG', '.png'
    ]
    image_list = []
    image_dir = None
    if os.path.isfile(image_path):  # 传入参数为一张图片时
        if os.path.splitext(image_path)[-1] in valid_suffix:
            image_list.append(image_path)
    elif os.path.isdir(image_path):  # 传入参数为含有多张图片的文件夹时
        image_dir = image_path
        for root, dirs, files in os.walk(image_path):
            for f in files:
                if os.path.splitext(f)[-1] in valid_suffix:
                    image_list.append(os.path.join(root, f))
    else:
        raise FileNotFoundError(
            '`--image_path` is not found. it should be an image file or a directory including images'
        )

    if len(image_list) == 0:
        raise RuntimeError('There are not image file in `--image_path`')

    # 自定义分割预测颜色
    custom_color = [
        255, 0, 0,  # building(red)
        255, 255, 0,  # road(yellow)
        192, 192, 0,  # pavement(darkkhaki)
        0, 255, 0,  # vegetation(green)
        128, 128, 128,  # bare soil(gray)
        0, 0, 255  # water(blue)
    ]

    # 构建模型
    model = HarDNet(num_classes=num_classes)

    # 创建transforms
    transforms = T.Compose([
        T.Resize(target_size=(256, 256)),
        T.Normalize()
    ])

    # 预测
    predict(
        model,
        model_path='static/model/model(2).pdparams',
        transforms=transforms,
        image_list=image_list,
        image_dir=image_dir,
        save_dir='static/image',
        custom_color=custom_color
    )

    # 待可视化的图像列表
    img_list = [
        image_path,
        os.path.join("static\\image\\pseudo_color_prediction", image_path[14:-3] + "png"),
        os.path.join("static\\image\\added_prediction", image_path[14:]),
    ]

    # 可视化
    fig = plt.figure(figsize=(10, 7))
    # 图例
    building = mpatches.Patch(color='red', label='Buildings')
    road = mpatches.Patch(color='yellow', label='Road')
    pavement = mpatches.Patch(color='darkkhaki', label='Pavement')
    vegetation = mpatches.Patch(color='lime', label='Vegetation')
    water = mpatches.Patch(color='mediumblue', label='Water')
    soil = mpatches.Patch(color='grey', label='Bare Soil')
    fig.legend(
        handles=[building, road, pavement, vegetation, water, soil],
        loc='upper center',
        ncol=6
    )
    # 拼接子图 左/中/右: 原图/原标注/伪彩色预测效果
    cnt = 0
    res_path = "/static/image/result/" + image_path[14:]
    for i in img_list:
        print(i)
        img = plt.imread(i)
        plt.subplot(231 + cnt)  # 拼接子图
        plt.imshow(img)
        plt.savefig(res_path[1:])
        cnt += 1

    return res_path
