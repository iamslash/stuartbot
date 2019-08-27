# -*- coding: utf-8 -*-

# references:
#  https://github.com/jrluu/Leetcode-Scraper/blob/master/leetcode_scraper.py

from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
import pprint, random


l_key = ['leetcode', u'릿코드', u'문제']
TIME_DELAY = 2

def probe(d_pkt):
    text = d_pkt['text']
    for key in l_key:
        if text.find(key) >= 0:
            return True
    return False

def handle(d_pkt):
    return pickone()

def makeDriver():
    options = webdriver.ChromeOptions()
    # options.binary_location = '/usr/local/bin/chromedriver'
    options.add_argument('headless')
    driver = webdriver.Chrome(chrome_options=options)
    driver.implicitly_wait(3)
    return driver

def printByTag(driver, tag):
    url_by_tag = 'https://leetcode.com/problemset/all/?topicSlugs={0}'.format(tag.lower())    

    print('requesting url: {0} ...'.format(url_by_tag))
    wait = WebDriverWait(driver, 10)
    driver.get(url_by_tag)

    # click freq button
    print('clicking...')
    btn_freq = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "reactable-th-frequency")))
    btn_freq.click()

    # process final html
    # l_el = driver.find_elements_by_xpath("//a[contains(@href, '/problems/')]")
    l_el  = driver.find_element_by_xpath('//*[@id="question-app"]/div/div[2]/div[2]/div[2]/table/tbody[1]')
    l_els = l_el.find_elements_by_xpath("//a[contains(@href, '/problems/')]")
    for el in l_els:
        print('[{0}]({1})'.format(el.text, el.get_attribute("href")))   

def clickFreq(driver):
    driver.get('https://leetcode.com/problemset/all')

    el   = driver.find_element_by_class_name(r'reactable-th-frequency')
    el.click()

def getTags(driver):
    driver.get('https://leetcode.com/problemset/all')
    
    l_el = driver.find_elements_by_xpath(r'//div/div/div/div[2]/div[1]/span')
    #l_el = driver.find_elements_by_class_name('filter-dropdown-menu-item')    
    # pprint.pprint(l_el)
    for el in l_el:
        el2 = el.find_element_by_tag_name('span')
        print(el2.text)

def pickone(difficulty='Medium'):
    # url_prob_desc = 'https://leetcode.com/problems/{0}/description/'
    url_all_medium = 'https://leetcode.com/problemset/all/?difficulty={0}'.format(difficulty)
    
    options = webdriver.ChromeOptions()
    # options.binary_location = '/usr/local/bin/chromedriver'
    options.add_argument('headless')
    driver = webdriver.Chrome(chrome_options=options)
    driver.implicitly_wait(3)
    driver.get(url_all_medium)
    # trigger user events
    el   = driver.find_element_by_xpath("//select/option[4]")
    el.click()

    # process final html
    l_el = driver.find_elements_by_xpath("//a[contains(@href, '/problems/')]")
    # for el in l_el:
    #     print('{0} : {1}'.format(el.text, el.get_attribute("href")))

    # random pick one
    el = random.choice(l_el)
    # return {'text' : el.text, 'link' : el.get_attribute("href")}
    #print(el.get_attribute("href"))
    link  = el.get_attribute("href")
    if link.find('/description') < 0:
        link += '/description/'
    return link

def sign_into_leetcode(driver):
    driver.implicitly_wait(TIME_DELAY)

    driver.get("https://leetcode.com/accounts/logout")

    valid_choice = False

    while (not valid_choice):
        valid_choice = True

        option = input("Type in method to login \n 1. Leetcode \n 2. Facebook \n 3. Google \n 4. Linkedin \n 5. Github \n")
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        if option == "1":
            driver.get("https://leetcode.com/accounts/login/")            
            driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div[2]/div/div/div/form/span[1]/input').send_keys(username)
            driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div[2]/div/div/div/form/span[2]/input').send_keys(password)
            driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div[2]/div/div/div/form/span[2]/input').send_keys(Keys.ENTER)
        elif option == '2':
            driver.get("https://leetcode.com/accounts/facebook/login/")
            driver.find_element_by_xpath('// *[ @ id = "email"]').send_keys(username)
            driver.find_element_by_xpath('//*[@id="pass"]').send_keys(password)
            driver.find_element_by_xpath('//*[@id="pass"]').send_keys(Keys.ENTER)
        elif option == '3':
            driver.get("https://leetcode.com/accounts/google/login/")
            driver.find_element_by_xpath('// *[ @ id = "Email"]').send_keys(username)
            driver.find_element_by_xpath('// *[ @ id = "Email"]').send_keys(Keys.ENTER)
            driver.find_element_by_xpath('//*[@id="Passwd"]').send_keys(password)
            driver.find_element_by_xpath('//*[@id="Passwd"]').send_keys(Keys.ENTER)
        elif option == '4':
            driver.get("https://leetcode.com/accounts/linkedin/login/")
            driver.find_element_by_name('session_key').send_keys(username)
            driver.find_element_by_name('session_password').send_keys(password)
            driver.find_element_by_name('session_password').send_keys(Keys.ENTER)
        elif option == '5':
            driver.get("https://leetcode.com/accounts/github/login/")
            driver.find_element_by_xpath('// *[ @ id = "login_field"]').send_keys(username)
            driver.find_element_by_xpath('//*[@id="password"]').send_keys(password)
            driver.find_element_by_xpath('//*[@id="password"]').send_keys(Keys.ENTER)
        else:
            valid_choice = False
            print("Invalid Choice. Please choose a number from 1 to 5 \n")

    driver.implicitly_wait(0)


def printTopInterviews(driver):
    # url_prob_desc = 'https://leetcode.com/problems/{0}/description/'
    url = 'https://leetcode.com/problemset/top-interview-questions/'

    driver.get(url)
    
    # click freq button
    print('clicking...')
    option_all = driver.find_element_by_xpath('//*[@id="question-app"]/div/div[2]/div[2]/div[2]/table/tbody[2]/tr/td/span/select/option[4]')
    option_all.click()    

    # process final html
    l_a = driver.find_elements_by_xpath("//a[contains(@href, '/problems/')]")
    for el_a in l_a:
        print('  - L | [{0}]({1})'.format(el_a.text, el_a.get_attribute("href")))

if __name__ == "__main__":
    driver = makeDriver()
    printTopInterviews(driver)
