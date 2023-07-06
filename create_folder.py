import os
import datetime

# 获取今天的日期（月-日）
today = datetime.date.today().strftime("%m-%d")

# 创建一个以今天日期为名的文件夹
os.makedirs(today)

# 在文件夹中创建六个子文件夹
for folder_name in ['original', 'detected', 'mask', 'overlay', 'decropped', 'skeletonized', 'length']:
    os.makedirs(os.path.join(today, folder_name))
