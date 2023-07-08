import os
import datetime

# Get the current time
today = datetime.date.today().strftime("%m-%d")

# Create a folder with the name of the date
# If the folder doesn't exist, create it
if not os.path.exists(today):
    os.makedirs(today)
    
    # Create seven subfolders in the date-folder
    for folder_name in ['Original', 'Detected', 'Mask', 'Overlay', 'Decropped', 'Skeletonized', 'Length_and_width']:
        os.makedirs(os.path.join(today, folder_name))