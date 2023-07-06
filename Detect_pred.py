from ultralytics import YOLO
from PIL import Image
import cv2
import argparse
import os
import datetime
import shutil

today = datetime.date.today().strftime("%m-%d")

parser = argparse.ArgumentParser(description='the root path of the run')
parser.add_argument('--dir', '-d', type=str, default=f"{today}", help='dir')

args, unknown = parser.parse_known_args()

dir = args.dir

model = YOLO("./best.pt")
# accepts all formats - image/dir/Path/URL/video/PIL/ndarray. 0 for webcam
# results = model.predict(source="0")
# results = model.predict(source="folder", show=True) # Display preds. Accepts all YOLO predict arguments

# from PIL
# im1 = Image.open(f"./{dir}")
results = model.predict(source=f"./{dir}/original", save=True, save_crop=True, save_txt=False)  # save plotted images

# 要移动的源文件夹路径
src_folder = './runs/detect/predict/'

# 目标文件夹路径
dest_folder = f"./{dir}/detected"

# 遍历源文件夹中的文件，移动并删除
for file_name in os.listdir(src_folder):
    # 构造源文件路径
    src_file = os.path.join(src_folder, file_name)

    # 构造目标文件路径
    dest_file = os.path.join(dest_folder, file_name)

    # 移动文件
    shutil.move(src_file, dest_file)

# 删除源文件夹
os.rmdir(src_folder)
