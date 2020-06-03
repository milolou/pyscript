# 2048bot.py - create a bot automatically playing 2048.

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random

def bot_2048(start):
    if start == 'human':
        browser0 = webdriver.Chrome()
        browser0.get('https://play2048.co/')
    if start == 'bot':
        browser = webdriver.Chrome()
        browser.get('https://play2048.co/')
        elem = browser.find_element_by_tag_name('html')
        for i in range(500):
            o = random.randint(0,3)
            if o == 0:
                elem.send_keys(Keys.UP)
            if o == 1:
                elem.send_keys(Keys.DOWN)
            if o == 2:
                elem.send_keys(Keys.RIGHT)
            if o == 3:
                elem.send_keys(Keys.LEFT)

bot_2048('bot')
            
