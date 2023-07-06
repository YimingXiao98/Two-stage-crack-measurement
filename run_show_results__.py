# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 13:48:39 2020

@author: Eric Bianchi
"""
import argparse
import datetime
import os
from show_results__ import *
from tqdm import tqdm
import torch

# Load the trained model, you could possibly change the device from cpu to gpu if 
# you have your gpu configured

today = datetime.date.today().strftime("%m-%d")

parser = argparse.ArgumentParser(description='the root path of the run')
parser.add_argument('--dir', '-d', type=str, default=f"{today}", help='dir')

args, unknown = parser.parse_known_args()

dir = args.dir

model = torch.load(f'./seg_weight.pt', map_location=torch.device('cuda'))
# model = torch.load(f'../Training-Testing//weights_20.pt', map_location=torch.device('cuda'))
# Set the model to evaluate mode
model.eval()

source_image_dir = f'./{dir}/Decropped/'
destination_mask = f'./{dir}/Mask/'
destination_overlays = f'./{dir}/Overlay/'

for image_name in tqdm(os.listdir(source_image_dir)):
    print(image_name)
    image_path = source_image_dir + image_name
    generate_images(model, image_path, image_name, destination_mask, destination_overlays)
