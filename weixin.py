from selenium import webdriver
import time
import json
from pprint import pprint

post = {}

driver = webdriver.Chrome('./chromedriver')
driver.get('https://mp.weixin.qq.com/')
time.sleep(2)
driver.find_element_by_xpath("./*//input[@id='account']").clear()
driver.find_element_by_xpath("./*//input[@id='account']").send_keys('dingyuehao@email.com')
driver.find_element_by_xpath("./*//input[@id='pwd']").clear()
driver.find_element_by_xpath("./*//input[@id='pwd']").send_keys('password')

time.sleep(5)
driver.find_element_by_xpath("./*//a[@id='loginBt']").click()

time.sleep(15)
# driver.get('https://mp.weixin.qq.com/')
cookie_items = driver.get_cookies()
for cookie_item in cookie_items:
    post[cookie_item['name']] = cookie_item['value']
cookie_str = json.dumps(post)
with open('cookie.txt', 'w+') as f:
    f.write(cookie_str)
