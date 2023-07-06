# Two stage crack measurement
A one-click tool to automatically detect, crop, segment, and calculate the cracks on concrete components.
# Requirements
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
 - ultralytics
# Usage
Two begin with, put the original images that you would like to perform the measurement on in the `Original` folder. Then simply run `run_all.py`. 

 It will do the following jobs:

1. Create seven folders to store results of every stage. (`create_folder.py`)
2. Perform object detection (in this scenario, the object is the crack). (`Thin.py`)
3. Crop the detected cracks and store them in to the folder `detected\`. (`detect_pred.py`)
4. Fill the cropped image into a rectangular, with the specific size of 512 * 512 pixels, since the segmentation model currently can only handle images with that size. (`rectangular.py`)
5. Perform segmentation task, generating predicted masks and overlays. (`run_show_results__.py`)
6. Skeletonize the masks. (`thin.py`)
7. Calculate the pixel-wise square and length of the cracks based on the number of white pixels in a skeletonized mask, then divide them to get the average crack width. (`measure.py`)

Note that the length is **Pixel-wised**, meaning currently it is not able to represent the actual length of the cracks in real world. Algorithm of converting the pixel length to actual length will be completed soon. 
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
