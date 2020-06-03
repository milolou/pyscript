
import os,shutil

path = r'D:\360MoveData\Users\lou\Documents\Python-100-Days-master'
os.makedirs('mdFile',exist_ok=True)
for folderName,subfolders,filenames in os.walk(path):
    for filename in filenames:
        if filename.endswith('.md'):
            try:
                shutil.copy(os.path.join(folderName,filename),os.path.join('mdFile',os.path.basename(filename)))
            except:
                print('file {} has some problems.'.format(filename))
            else:
                print('Nothing wrong.')
            
