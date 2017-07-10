import lxml
import html
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests
import time
import csv


def getName():
    with open("SAMPLE_DATA.csv","r") as f:
        name = [line.split(',')[0] for line in f]
    #print(name)
    return name

def getLine():
    with open("SAMPLE_DATA.csv","r") as f:
        line = [line.strip('\n') for line in f]
    #print(line)
    return line


def driver():
    url ='http://www.google.com'
    driver = webdriver.Firefox(executable_path = '/Users/TJ/Downloads/geckodriver')
    #time.sleep(5)
    driver.get(url)
    htmlSource = driver.page_source
    return driver


def googleCompany(driver, name):
    search = driver.find_element_by_name('q')
    search.send_keys(name)
    search.send_keys(Keys.RETURN)
    time.sleep(1)


def grabURL(driver):
    urls = []
    for k in range(0,5):
        results = driver.find_elements_by_css_selector('div.g')
        time.sleep(1)
        
        link = results[k].find_element_by_tag_name("a")
        time.sleep(1)
        
        href = link.get_attribute("href")
        urls.append(href)
    print(urls)
    return urls


def writeCSV(urls):
    #line = getLine()
    with open("output.csv", "w") as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        writer.writerow(urls)


def clear(name):
    search = driver.find_element_by_name('q')
    #length = len(search.get_attribute(name))
    search.send_keys(30 * Keys.BACKSPACE)


if __name__ == "__main__":
    all_urls = []
    companyName = getName()
    driver = driver()
    for name in companyName:
        time.sleep(2)
        googleCompany(driver, name)
        urls = grabURL(driver)
        time.sleep(2)
        all_urls.append(urls)
        print("***************"+ str(all_urls))
        clear(name)
    writeCSV(all_urls)

#driver.quit()