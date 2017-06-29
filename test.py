from lxml import html
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import requests
import time
url ='file:///Users/TJ/Desktop/web.html'
driver = webdriver.Firefox(executable_path = '/Users/TJ/Downloads/geckodriver')
#time.sleep(5)

driver.get(url)
#htmlSource = driver.page_source
time.sleep(1)

content = driver.find_element_by_class_name('content')
print(content)
