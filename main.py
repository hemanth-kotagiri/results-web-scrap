import time
import re
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
driver = webdriver.Firefox(
    executable_path=os.path.join(os.getcwd(), driver_file))


urls = {
    "1,1": "http://results.jntuh.ac.in/jsp/SearchResult.jsp?degree=btech&examCode=1323&etype=r16&type=grade16",
    "1,2": "http://results.jntuh.ac.in/jsp/SearchResult.jsp?degree=btech&examCode=1356&etype=r16&type=grade16",
    "2,1": "http://results.jntuh.ac.in/jsp/SearchResult.jsp?degree=btech&examCode=1391&etype=r17&type=grade17",
    "2,2": "http://results.jntuh.ac.in/jsp/SearchResult.jsp?degree=btech&examCode=1437&etype=r17&type=intgrade",
}

url = urls["1,1"]  # 2,2

driver.get(url)

# Getting the captcha value
captcha_val = driver.execute_script(
    "return document.getElementById('txtCaptcha').value")
# print(captcha_val)


hall_pass = "document.getElementById('htno').value = '{}'".format(num)
date_pass = "document.getElementById('datepicker').value = '{}'".format(bday)
pass_str = "document.getElementById('txtInput').value = '{}'".format(
    captcha_val)

# print(pass_str)


driver.execute_script(pass_str)
driver.execute_script(date_pass)
driver.execute_script(hall_pass)

submit_button_xpath = '//*[@id="myForm"]/div/table/tbody/tr[5]/td[3]/input'

submit = driver.find_element_by_xpath(submit_button_xpath)
# time.sleep(1)
submit.click()

# time.sleep(2)
# After submitting the form
next_url = driver.current_url

# print(next_url)

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

# Gathering the student information

results = []

for element in list(tables[1].tbody)[1:]:
    current_subject = []
    for table_row in element:
        for b in table_row:
            if type(b) != str:
                # table_row has 4 elements: subject code, name, grade, credits else
                # table_row has 7 elements: subject code, name, internal, external, total grade, credits
                current_subject.append(b.text)

    if not current_subject:
        continue

    subject_object = {}
    if current_subject and len(current_subject) == 4:
        subject_object["subject_code"] = current_subject[0]
        subject_object["subject_name"] = current_subject[1]
        subject_object["grade_earned"] = current_subject[2]
        subject_object["subject_credits"] = current_subject[3]
    else:
        subject_object["subject_code"] = current_subject[0]
        subject_object["subject_name"] = current_subject[1]
        subject_object["internal_marks"] = current_subject[2]
        subject_object["external_marks"] = current_subject[3]
        subject_object["total_marks"] = current_subject[4]
        subject_object["grade_earned"] = current_subject[5]
        subject_object["subject_credits"] = current_subject[6]

    results.append(subject_object)


for subject in results:
    for key, value in subject.items():
        print(key, " ", value)
