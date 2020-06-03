# SelectiveCopy.py - walk through a folder tree , and find some specific files,
# copy them into a new folder.

import os,shutil

# Way to find the specific files,with os.walk() function.
def copyPDFToNewFolder(folder,newfolder):
    for foldername,subfolders,filenames in os.walk(folder):
        for filename in filenames:
            if filename.endswith('.pdf'):
                absPathOfFilenames = os.path.join(foldername,filename)
                shutil.copy(absPathOfFilenames,newfolder)

copyPDFToNewFolder(r'此电脑\HUAWEI CRR-UL00\内部存储',r'C:\Users\lou\Desktop\pyscript\newpdfcopy')
