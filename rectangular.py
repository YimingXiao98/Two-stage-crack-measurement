import argparse
import datetime
import os
from PIL import Image

today = datetime.date.today().strftime("%m-%d")

parser = argparse.ArgumentParser(description='the root path of the run')
parser.add_argument('--dir', '-d', type=str, default=f"{today}", help='dir')

args, unknown = parser.parse_known_args()

dir = args.dir

# Path to the original image folder
img_dir = f'./{dir}/detected/crops/Cracks'

# get all the iamges in the folder
img_list = os.listdir(img_dir)

# define the length of the images that are being send into the segmentation model
w, h = 512, 512

# iterate over them
for img_name in img_list:
    img_path = os.path.join(img_dir, img_name)
    img = Image.open(img_path)
    width, height = img.size  
    max_size = max(width, height)  
    square_img = Image.new('RGB', (max_size, max_size), (0, 0, 0))  # Get a square image that is whole black
    square_img.paste(img, (int((max_size - width) / 2), int((max_size - height) / 2)))  # Paste the crack image on the center
    resized_img = square_img.resize((w, h), Image.ANTIALIAS)  # Adjust the size to 512
    square_img.save(f'./{dir}/Decropped/' + img_name)