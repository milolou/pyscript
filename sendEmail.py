#! python3

from selenium import webdriver
import pyinputplus as pyip
import time

account = 'milofromlou@gmail.com'
password = pyip.inputPassword('Enter a password!')

def sendEmail(address,text):
    browser = webdriver.Chrome()
    browser.get('https://accounts.google.com/ServiceLogin/identifier?service=mail&passive=true&rm=false&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&ss=1&scc=1&ltmpl=default&ltmplcache=2&emr=1&osid=1&flowName=GlifWebSignIn&flowEntry=AddSession')
    inputElem1 = browser.find_element_by_id('identifierId')
    inputElem1.send_keys(account)
    inputElem2 = browser.find_element_by_id('identifierNext')
    inputElem2.click()
    time.sleep(3)
    inputElem3 = browser.find_element_by_class_name('whsOnd')
    inputElem3.send_keys(password)
    time.sleep(1)
    inputElem4 = browser.find_element_by_class_name('RveJvd')
    inputElem4.click()
    time.sleep(15)
    inputElem5 = browser.find_element_by_css_selector('div.T-I.J-J5-Ji.T-I-KE.L3')
    inputElem5.click()
    time.sleep(2)
    inputElem6 = browser.find_element_by_name('to')
    inputElem6.send_keys(address)
    inputElem7 = browser.find_element_by_id(':q6')
    inputElem7.send_keys(text)
    inputElem8 = browser.find_element_by_id(':or')
    inputElem8.click()

destination = input('Please give an address!\n')
text = input('What is the text!\n')
sendEmail(destination,text)
