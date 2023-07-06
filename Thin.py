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

# Define the input folder
input_folder = f'./{dir}/Mask/'

# Define the output folder
output_folder = f'./{dir}/Skeletonized/'

# Get the path of all the images in the input folder
file_paths = glob.glob(os.path.join(input_folder, '*.jpg')) + \
             glob.glob(os.path.join(input_folder, '*.png'))

for file_path in file_paths:
    # Read the image
    image = cv2.imread(file_path)

    # Skeletonize it
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    _, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

    thinned = thin(thresh)
    # Get out put path
    output_path = os.path.join(output_folder, os.path.basename(file_path).split('.')[0] + '.png')
    thinned = np.uint8(thinned) * 255
    # Save image
    cv2.imwrite(output_path, thinned)
