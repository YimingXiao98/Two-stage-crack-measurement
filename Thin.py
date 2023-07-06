import argparse
import datetime
import os
import glob
import cv2
import numpy as np
from skimage.morphology import skeletonize, thin

today = datetime.date.today().strftime("%m-%d")

parser = argparse.ArgumentParser(description='the root path of the run')
parser.add_argument('--dir', '-d', type=str, default=f"{today}", help='dir')

args, unknown = parser.parse_known_args()

dir = args.dir

# 定义要遍历的文件夹路径
input_folder = f'./{dir}/mask/'

# 定义输出文件夹路径
output_folder = f'./{dir}/skeletonized/'

# 获取文件夹中所有jpg和png文件的路径
file_paths = glob.glob(os.path.join(input_folder, '*.jpg')) + \
             glob.glob(os.path.join(input_folder, '*.png'))

for file_path in file_paths:
    # 读取图像
    image = cv2.imread(file_path)

    # 骨架化
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    _, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

    thinned = thin(thresh)
    # 获取输出文件路径
    output_path = os.path.join(output_folder, os.path.basename(file_path).split('.')[0] + '.png')
    thinned = np.uint8(thinned) * 255
    # 保存图像
    cv2.imwrite(output_path, thinned)
