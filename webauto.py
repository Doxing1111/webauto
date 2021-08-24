'''
author: Joe
date: 2021/08/24
'''

from time import sleep
from selenium import webdriver
from selenium.webdriver.support.ui import Select

wd = webdriver.Chrome(r'C:\ChromeDriver\chromedriver.exe') # r 是防止字符轉義, 加上'r'就能保留原有的樣子

# ---------------------------------------------
# <以下舉例>
# a = r'\t1'
# print(a) # \t1
#
# b = '\t1'
# print(b) #    1 (\t = Tab鍵功能)
# ---------------------------------------------

wd.get('https://tw.yahoo.com/')
wd.maximize_window()
sleep(2)
element = wd.find_element_by_id('header-signin-link').click()
sleep(2)
element = wd.find_element_by_id('createacc').click()
sleep(2)
element = wd.find_element_by_name('firstName').send_keys('Mark')
sleep(2)
element = wd.find_element_by_name('lastName').send_keys('Huang')
sleep(2)
element = wd.find_element_by_name('yid').send_keys('deroseso')
sleep(2)
element = wd.find_element_by_name('password').send_keys('qqTest12345A')
sleep(2)
element = wd.find_element_by_name('phone').send_keys('0910001002')
sleep(2)
select = Select(wd.find_element_by_name('mm')) # 操作下拉式選單(Select)
select.select_by_value('8')
sleep(2)
element = wd.find_element_by_name('dd').send_keys(24)
sleep(2)
element = wd.find_element_by_name('yyyy').send_keys('1990')
sleep(2)
element = wd.find_element_by_name('freeformGender').send_keys('男')
sleep(2)
element = wd.find_element_by_name('signup').click()