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

model = YOLO("./detect_weight.pt")
# accepts all formats - image/dir/Path/URL/video/PIL/ndarray. 0 for webcam
# results = model.predict(source="0")
# results = model.predict(source="folder", show=True) # Display preds. Accepts all YOLO predict arguments

# from PIL
# im1 = Image.open(f"./{dir}")
results = model.predict(source=f"./{dir}/Original", save=True, save_crop=True, save_txt=False)  # save plotted images

src_folder = './runs/detect/predict/'

dest_folder = f"./{dir}/Detected"

for file_name in os.listdir(src_folder):

    src_file = os.path.join(src_folder, file_name)

    dest_file = os.path.join(dest_folder, file_name)

    shutil.move(src_file, dest_file)

os.rmdir(src_folder)
