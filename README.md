# Two stage crack measurement
A one-click tool to automatically detect, crop, segment, and calculate the cracks on concrete components.
# Requirements
 - git lfs
 - Pytorch >= 1.10
 - Python >= 3.6
 - tqdm
 - matplotlib
 - sklearn
 - cv2
 - Pillow
 - pandas
 - shutil
 - opencv
 - skimage
 - ultralytics
# Usage
Clone the repository by
`git clone https://github.com/YimingXiao98/Two-stage-crack-measurement.git`

When done cloning, navigate to the repository folder, open your terminal, activate `Git Lfs`by
`git lfs install`

and pull the two .pt files by

`git lfs pull`

Install the requirements by

`pip install -r requirements`

Two begin with, put the original images that you would like to perform the measurement on in the `Original` folder. Then simply run `run_all.py`.

 It will do the following jobs:

1. Create seven folders to store results of every stage. (`create_folder.py`)
2. Perform object detection (in this scenario, the object is the crack). (`Thin.py`)
3. Crop the detected cracks and store them in to the folder `detected\`. (`detect_pred.py`)
4. Perform segmentation task, generating predicted masks and overlays. (`run_show_results__.py`)
5. Skeletonize the masks. (`thin.py`)
6. Calculate the pixel-wise square and length of the cracks based on the number of white pixels in a skeletonized mask, then divide them to get the average crack width. (`measure.py`)

Note that the length by default is **Pixel-wised**, meaning currently it is not able to represent the actual length of the cracks in real world. 

If you have the conversion scale of the images, rename your images such that the scale (> 1) is at the ending of your images' file names without suffix, e.g. `image_12.61.png`, where 12.61 is your conversion scale. Then the scripts should read the scale correctly.
# Acknowledgements
The code of the segmentation task and the trained model is based in part on the source code of E. Bianchi et al (2021) at Virginia Tech:
```
Bianchi, Eric; Hebdon, Matthew (2021): Concrete Crack Conglomerate Dataset. 
University Libraries, Virginia Tech. Dataset. https://doi.org/10.7294/16625056.v1 
```
```
Bianchi, Eric; Hebdon, Matthew (2021): Trained Model for the Semantic Segmentation of Concrete Cracks (Conglomerate). 
University Libraries, Virginia Tech. Software. https://doi.org/10.7294/16628596.v1 
```
