import os
import shutil
import datetime

today = today = datetime.date.today().strftime("%m-%d")

sdir = './Original'
ddir = f'./{today}/Original'

files = os.listdir(sdir)
# Move images
for file in files:
    if file.lower().endswith(('.jpg', '.jpeg', '.png')):
        s_path = os.path.join(sdir, file)
        d_path = os.path.join(ddir, file)

    shutil.copy(s_path, d_path)
