import requests, bs4,webbrowser, re
from selenium import webdriver

url = str(input())
res = requests.get(url)

try:
    res.raise_for_status()
except Exception as err:
    print('There was a probelm with the first url: %s' % (err))

soup = bs4.BeautifulSoup(res.text, "html.parser")
linkElems = soup.select('a')
hrefRegex = re.compile(r'^"http(s)?://.*?"')
urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', res.text)
mo = hrefRegex.search(linkElems)
for i in range (len(linkElems[i])
    mo = hrefRegex.search(linkElems[i])
    res = requests.get(mo.group())
        if res.status_code != requests.codes.ok:
                print('%s is broken link. Response: 404 "Not Found"' % (mo.group()))
