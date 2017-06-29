from lxml import html
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests
import time
import csv



def driver():
    url ='http://listings.findthecompany.com'
    driver = webdriver.Firefox(executable_path = '/Users/TJ/Downloads/geckodriver')
    #time.sleep(5)
    driver.get(url)
    htmlSource = driver.page_source
    return driver
    #print(driver.window_handles)

def findNigerianPrivate(driver):
    company= driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/div/div[3]/div/div[1]/div[4]/div[1]/div[2]/div/div[1]/div[2]/div/div/input[1]").click()
    time.sleep(1)
    company.send_keys('Nigerian')
    private= driver.find_element_by_class_name('i icon-angle-up')
    private.click()

""""
Goal: Use Selenium to retrieve company information from each page
"""
#def scrapeEachCompany():
#driver.find_element_by_xpath("").click

""""
Goal: Write information to csv file
"""
def writeCSV():
    with open("~/Desktop", "wb") as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        for line in data:
                writer.writerow(line)


if __name__ == "__main__":
    driver = driver()
    findNigerianPrivate(driver)
    time.sleep(5)
    driver.quit()