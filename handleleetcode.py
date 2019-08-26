# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.support.ui import Select
import pprint, random

l_key = ['leetcode', u'릿코드', u'문제']

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
    driver.get(url_by_tag)
    # process final html
    # l_el = driver.find_elements_by_xpath("//a[contains(@href, '/problems/')]")
    l_el  = driver.find_element_by_xpath('//*[@id="question-app"]/div/div[2]/div[2]/div[2]/table/tbody[1]')
    l_els = l_el.find_elements_by_xpath("//a[contains(@href, '/problems/')]")
    for el in l_els:
        print('[{0}]({1})'.format(el.text, el.get_attribute("href")))   

def clickFreq(driver):
    el   = driver.find_element_by_xpath('//*[@id="question-app"]/div/div[2]/div[2]/div[2]/table/thead/tr/th[7]')
    el.click()

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

if __name__ == "__main__":
    # print(pickone())
    driver = makeDriver()
    clickFreq(driver)
    printByTag(driver, "array")