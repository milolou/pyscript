
import shutil,os,re

path = r'D:\moveData_360\Users\lou\Documents\Python_100_Days_master'
for folder in os.listdir(path):
    if folder.startswith('Day'):
        new_folder = re.sub('-','_',folder)
        shutil.move(os.path.join(path,folder),os.path.join(path,new_folder))
