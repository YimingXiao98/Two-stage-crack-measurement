import argparse
import datetime
import os
from PIL import Image

today = datetime.date.today().strftime("%m-%d")

parser = argparse.ArgumentParser(description='the root path of the run')
parser.add_argument('--dir', '-d', type=str, default=f"{today}", help='dir')

args, unknown = parser.parse_known_args()

dir = args.dir

# 图片文件夹路径
img_dir = f'./{dir}/detected/crops/Cracks'

# 获取所有图片文件名
img_list = os.listdir(img_dir)

# 定义正方形边长
w, h = 512, 512

# 循环遍历所有图片并进行处理
for img_name in img_list:
    img_path = os.path.join(img_dir, img_name)
    img = Image.open(img_path)
    width, height = img.size  # 获取图片宽高
    max_size = max(width, height)  # 先取宽高的最大值作为边长
    square_img = Image.new('RGB', (max_size, max_size), (0, 0, 0))  # 定义黑色背景的正方形图片
    square_img.paste(img, (int((max_size - width) / 2), int((max_size - height) / 2)))  # 将原图粘贴到正中心
    #resized_img = square_img.resize((w, h), Image.ANTIALIAS)  # 对正方形图片进行调整大小
    square_img.save(f'./{dir}/decropped/' + img_name)  # 保存输出图片到指定文件夹