import time
import os
import requests
import urllib3
from bs4 import BeautifulSoup
from selenium import webdriver
import platform


# num = input("Enter your hallticker number: ").upper()
# bday = input("Enter your birthday: ")
num = "185U1A0565"
bday = "2001-04-03"

driver_file = "geckodriver" if platform.system() == "Linux" else "geckodriver.exe"
driver = webdriver.Firefox(executable_path=os.path.join(os.getcwd(),driver_file))


# url = 'http://results.jntuh.ac.in/jsp/SearchResult.jsp?degree=btech&examCode=1437&etype=r17&type=intgrade' # 2, 2
url = 'http://results.jntuh.ac.in/jsp/SearchResult.jsp?degree=btech&examCode=1391&etype=r17&type=grade17' # 2, 1

driver.get(url)

# Getting the captcha value
captcha_val = driver.execute_script("return document.getElementById('txtCaptcha').value")
#print(captcha_val)


hall_pass = "document.getElementById('htno').value = '{}'".format(num)
date_pass = "document.getElementById('datepicker').value = '{}'".format(bday)
pass_str = "document.getElementById('txtInput').value = '{}'".format(captcha_val)

#print(pass_str)


driver.execute_script(pass_str)
driver.execute_script(date_pass)
driver.execute_script(hall_pass)

submit_button_xpath = '//*[@id="myForm"]/div/table/tbody/tr[5]/td[3]/input'

submit = driver.find_element_by_xpath(submit_button_xpath)
time.sleep(1)
submit.click()

time.sleep(2)
# After submitting the form
next_url = driver.current_url

#print(next_url)

sel_html = driver.execute_script("return document.documentElement.outerHTML")

# print(sel_html)
sel_soup = BeautifulSoup(sel_html, 'html.parser')

result = (sel_soup.prettify())

subjects = []
grades = []
name = ""

tables = sel_soup.find_all('table')

""" tables[0] consists the information regarding the student """
""" tables[1] consists the subject code, subject name, grade and credits"""

# print(len(tables))

# for i in range(len(tables) - 1):
    # if i == 1: continue
    # print(tables[i].find_all_next('tr'))
    # break






# name = driver.find_element_by_xpath('/html/body/form/table[1]/tbody/tr[1]/td[4]/b')

# elements = name.find_elements_by_tag_name("b")
# print(elements)
# print(elements.get_attribule('value'))
# for ele in elements:
    # print(ele.get_attribute('value'))


# print(next_url)

# print(requests.get(next_url).text)

#web_soup = BeautifulSoup(requests.get(next_url).text, 'html.parser')

# print(web_soup.prettify())










# import sys
# from PyQt4.QtGui import QApplication
# from PyQt4.QtCore import QUrl
# from PyQt4.QtWebKit import QWebPage
# import bs4 as bs
# import urllib.request

# class Client(QWebPage):

    # def __init__(self, url):
        # self.app = QApplication(sys.argv)
        # QWebPage.__init__(self)
        # self.loadFinished.connect(self.on_page_load)
        # self.mainFrame().load(QUrl(url))
        # self.app.exec_()

    # def on_page_load(self):
        # self.app.quit()

                                                            

# url = 'http://202.63.105.184/results/jsp/SearchResult.jsp?degree=btech&examCode=1391&etype=r17&type=grade17'

# url2 = 'https://pythonprogramming.net/parsememcparseface/'

# client_resp = Client(url)

# source = client_resp.mainFrame().toHtml()

# soup = BeautifulSoup(source, 'lxml')

# # js_test = soup.find('p', class_='jstest')
# # print(js_test.text)

# # print(soup.prettify())

# # for tag in soup.find_all('input'):
    # # print(tag)

# input_tag = soup.find('input', id="txtCaptcha")

# # given_tag = soup.find('input', id="txtInput")
# print(input_tag)

# print(input_tag.value)

# print(given_tag.value)

