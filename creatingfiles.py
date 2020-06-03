# creatingFiles.py - creating a series of files for samples.

import os
opFolders = r'C:\Users\lou\Desktop\pyscript\seriesfiles'
for i in range(9):
    filename = 'spam' + '00' + str(i) + '.txt'
    newFile = open(os.path.join(opFolders,filename),'w')
    newFile.close()
