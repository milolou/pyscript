#! python3
# imageDownloader.py - Download every photo from the searching result.

import requests, os
from selenium import webdriver

wantingObjects = input('Type an object you want to see.\n')

# Creating folder.
flickr = 'https://flickr.com/search/?text=' + wantingObjects
os.makedirs('photos',exist_ok=True)

# Opening website and searching photos' url.
browser = webdriver.Chrome()
browser.get(flickr)
elems = browser.find_elements_by_class_name('awake')
l_1 = len(elems)
for i in range(l_1):
    style = elems[i].get_attribute('style')
    styleList = style.split('url')
    rawUrl = styleList[1]
    l_2 = len(rawUrl)
    new_url = rawUrl[2:(l_2 - 3)]
    newUrl = 'https:' + new_url
    print('Downloading page %s'%(newUrl))
    res = requests.get(newUrl)
    pictureFile = open(os.path.join('photos',os.path.basename(newUrl)),'wb')
    for chunk in res.iter_content(100000):
        pictureFile.write(chunk)
    pictureFile.close()
    
print('Done')


