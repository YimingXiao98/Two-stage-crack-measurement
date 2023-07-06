import argparse
import datetime
from math import nan
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

# Define the input folders
input_folder_mask = f'./{dir}/Mask/'
input_folder_skel = f'./{dir}/Skeletonized/'

# Define the output folder
output_folder_mask = f'./{dir}/Length_and_width/'

# Define the scale, by default is 1:1 (1 pixel equals to 1 millimeter)
scale = 1.0

# Get the paths of all the images
file_paths_skel = glob.glob(os.path.join(input_folder_skel, '*.jpg')) + \
                  glob.glob(os.path.join(input_folder_skel, '*.png'))

file_paths_mask = glob.glob(os.path.join(input_folder_mask, '*.jpg')) + \
                  glob.glob(os.path.join(input_folder_mask, '*.png'))

n = len(file_paths_mask)
i = 0
# An array to store length
L = np.zeros(n)
for file_path in file_paths_skel:
    # Read the image
    image = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)

    # Get the medial axis
    skeleton, distance = medial_axis(image, return_distance=True)

    # Calculate the length in pixels
    length_o = np.sum(distance * skeleton)

    # Convert into real world length
    length = length_o * scale

    # Save the length
    L[i] = length
    i += 1


   
i = 0
S = np.zeros(n)
for file_path_mask in file_paths_mask:

    image_mask = cv2.imread(file_path_mask, cv2.IMREAD_GRAYSCALE)

    num_white_pixels = cv2.countNonZero(image_mask) # Count the number of white pixels as the square

    S[i] = num_white_pixels

    i += 1
    
W = np.zeros(n)

i = 0
for i in range(n):
    if L[i] == 0:
        W[i] = 0  # To prevent being divided by 0
    else: 
        W[i] = S[i] / L[i]


i = 0

for file_path in file_paths_skel:

    image = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)
    # Write length and width on the image
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(image, f'Length: {L[i]:.2f} mm', (50, 50), font, 1, (255, 255, 255), 2, cv2.LINE_AA)
    cv2.putText(image, f'Avg_Width: {W[i]:.2f} mm', (50, 100), font, 1, (255, 255, 255), 2, cv2.LINE_AA)
    # Get the output path
    output_path = os.path.join(output_folder_mask, os.path.basename(file_path))

    cv2.imwrite(output_path, image)
    i += 1


i = 0
for file_path in file_paths_mask:

    image = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)
    # Write length and width on the image
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(image, f'Length: {L[i]:.2f} mm', (50, 50), font, 1, (255, 255, 255), 2, cv2.LINE_AA)
    cv2.putText(image, f'Avg_Width: {W[i]:.2f} mm', (50, 100), font, 1, (255, 255, 255), 2, cv2.LINE_AA)
    # Get the output path
    output_path = os.path.join(output_folder_mask, os.path.basename(file_path))

    cv2.imwrite(output_path, image)
    i += 1