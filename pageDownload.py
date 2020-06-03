# linkVerification.py - Download every link in a given page.

import requests,bs4,os,random
import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s -  %(levelname)s -  %(message)s')
logging.debug('Start of program')

user_agents = ['Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1','Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50','Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11']
header = {'User-Agent':random.choice(user_agents)}

os.makedirs('htmls',exist_ok=True)

def linkVerification(url):
    res = requests.get(url,headers=header)
    soup = bs4.BeautifulSoup(res.text,'html.parser')
    linkElems = soup.select('a')
    logging.debug('(%s)'%(str(linkElems)))
    imgElems = soup.select('img')
    logging.debug('(%s)'%(str(imgElems)))
    scriptElems = soup.select('script')
    logging.debug('(%s)'%(str(scriptElems)))
    absPath = os.path.abspath('htmls')
    for i in linkElems:
        link1 = i.attrs.get('href',0)
        newLink = ''
        logging.debug('(%s)'%(str(link1)))
        if link1 == 0:
            print('Invalid link.')
            continue
        elif link1.startswith('https:'):
            newLink = link1
        elif link1.startswith('http:'):
            newLink = link1
        else:
            newLink = 'https:' + link1
        print('Downloading page %s'%(newLink))
        try:
            htmlName = os.path.join(absPath,os.path.basename(newLink))
            htmlPage = open(htmlName,'wb')
            hPage = requests.get(newLink)
            try:
                hPage.raise_for_status()
            except:
                print('Page not found!')
                htmlPage.close()
                continue
            for chunk1 in hPage.iter_content(100000):
                htmlPage.write(chunk1)
            htmlPage.close()
        except:
            print('Page %s has no basename.'%(newLink))
    for s in imgElems:
        link2 = s.attrs.get('src',1)
        newImg = ''
        logging.debug('(%s)'%(str(link2)))
        if link2 == 1:
            print('Invalid link.')
            continue
        elif link2.startswith('https:'):
            newImg = link2
        elif link2.startswith('http:'):
            newImg = link2
        else:
            newImg = 'https:' + link2
        print('Downloading page %s'%(newImg))
        try:
            imgName = os.path.join(absPath,os.path.basename(newImg))
            imgPage = open(imgName,'wb')
            iPage = requests.get(newImg)
            try:
                iPage.raise_for_status()
            except:
                print('Page not found!')
                imgPage.close()
                continue
            for chunk2 in iPage.iter_content(100000):
                imgPage.write(chunk2)
            imgPage.close()
        except:
            print('Page %s has no basename.'%(newImg))
    for j in scriptElems:
        link3 = j.attrs.get('src',2)
        newScript = ''
        logging.debug('(%s)'%(str(link3)))
        if link3 == 2:
            print('Invalid link.')
            continue
        elif link3.startswith('https:'):
            newScript = link3
        elif link3.startswith('http:'):
            newScript = link3
        else:
            newScript = 'https:' + link3
        print('Downloading page %s'%(newScript))
        try:
            scriptName = os.path.join(absPath,os.path.basename(newScript))
            sciptPage = open(scriptName,'wb')
            sPage = requests.get(newScript)
            try:
                sPage.raise_for_status()
            except:
                print('Page not found!')
                scriptPage.close()
                continue
            for chunk3 in sPage.iter_content(100000):
                scriptPage.write(chunk3)
            scriptPage.close()
        except:
            print('Page %s has no basename.'%(newScript))
    print('Done.')

newUrl = input('Please input an url.\n')
linkVerification(newUrl)

