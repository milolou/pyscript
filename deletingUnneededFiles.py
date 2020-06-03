# deletingUnneededFiles.py - find some files over 100MB, try to deleting them.

import os,send2trash

def deletingLargeFiles(folder):
    for foldername,subfolders,filenames in os.walk(folder):
        for filename in filenames:
            absPath = os.path.join(foldername,filename)
            if os.path.getsize(absPath) > (100 * 1024):
                send2trash.send2trash(absPath)


deletingLargeFiles('F:\\')
