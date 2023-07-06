import argparse
import datetime
import os
import glob
import cv2
import numpy as np
from skimage.morphology import medial_axis
from skimage.draw import line

today = datetime.date.today().strftime("%m-%d")

parser = argparse.ArgumentParser(description='the root path of the run')
parser.add_argument('--dir', '-d', type=str, default=f"{today}", help='dir')

args, unknown = parser.parse_known_args()

dir = args.dir

# 定义要遍历的文件夹路径
input_folder = f'./{dir}/skeletonized/'

# 定义输出文件夹路径
output_folder = f'./{dir}/length/'

# 定义比例尺，默认一个像素为1毫米
scale = 1.0

# 获取文件夹中所有jpg和png文件的路径
file_paths = glob.glob(os.path.join(input_folder, '*.jpg')) + \
             glob.glob(os.path.join(input_folder, '*.png'))

for file_path in file_paths:
    # 读取图像
    image = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)

    # 提取骨架的中轴线
    skeleton, distance = medial_axis(image, return_distance=True)

    # 计算中轴线的长度
    length = np.sum(distance * skeleton)

    # 将长度转换为实际长度单位
    length = length * scale

    # 在原图上写入长度
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(image, f'Length: {length:.2f} mm', (50, 50), font, 1, (255, 255, 255), 2, cv2.LINE_AA)

    # 将中轴线可视化并保存
    #for r, c in np.transpose(np.nonzero(skeleton)):
        #rr, cc = line(r, c, *np.transpose(np.nonzero(distance[r, c] > distance)))
        #image[rr, cc] = 255

    # 获取输出文件路径
    output_path = os.path.join(output_folder, os.path.basename(file_path))

    # 保存图像
    cv2.imwrite(output_path, image)
