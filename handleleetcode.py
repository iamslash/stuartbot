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

def pickone(difficulty='Medium'):
    url_prob_desc = 'https://leetcode.com/problems/{0}/description/'
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
    return el.get_attribute("href")

if __name__ == "__main__":
    print(pickone())
