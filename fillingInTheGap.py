# fillingInTheGap.py - rename the file to let the gaps of numbers
# in filename disappear.

import os,shutil

def eliminateGaps(folder):
    listOfFiles = os.listdir(folder)
    filesWithSpecificPrefix = []
    for filename in listOfFiles:
        if filename.startswith('spam'):
            filesWithSpecificPrefix.append(filename)
    length = len(filesWithSpecificPrefix)
    gapsOfNum = []
    glob = int(filesWithSpecificPrefix[0][6])
    for file in filesWithSpecificPrefix:
        num = int(file[6])
        if  glob !=num:
            print(f'There  is gap in {glob-1} and {glob+1}.')
            gapsOfNum.append(glob)
            glob += 1
        glob += 1
        # insert gaps.
    for N in gapsOfNum:
        insertFilename = filesWithSpecificPrefix[N][0:6] + str(N) + \
                         filesWithSpecificPrefix[N][7:]
        insertfile = open(os.path.join(folder,insertFilename),'w')
        insertfile.close()
        
'''    startNum = gapsOfNum[0]
    for i in range(startNum,length):
        originalName = filesWithSpecificPrefix[i]
        newFilename = filesWithSpecificPrefix[i][0:6] + str(i) + \
                      filesWithSpecificPrefix[i][7:]
        # rename the file.
        shutil.move(os.path.join(folder,originalName),\
                    os.path.join(folder,newFilename)) '''
    

eliminateGaps(r'C:\Users\lou\Desktop\pyscript\seriesfiles')
