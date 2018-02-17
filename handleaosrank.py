# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.support.ui import Select
import pprint, random

l_key = [u'구글플레이 순위']

def probe(d_pkt):
    text = d_pkt['text']
    for key in l_key:
        if text.find(key) >= 0:
            return True
    return False

def handle(d_pkt):
    url = 'http://www.gevolution.co.kr/rank/aos.asp'
    
    options = webdriver.ChromeOptions()
    # options.binary_location = '/usr/local/bin/chromedriver'
    options.add_argument('headless')
    driver = webdriver.Chrome(chrome_options=options)
    driver.implicitly_wait(3)
    driver.get(url)

    # process final html
    r = ''
    for i in range(5):        
        xp = "//*[@id='imgload']/table/tbody/tr[{0}]/td[4]/div/div/span[1]/a".format(i+1)
        el = driver.find_element_by_xpath(xp)
        r += '{0}. {1} : {2}\n'.format(i+1, el.text, el.get_attribute("href"))
    return r

if __name__ == "__main__":
    print(handle({}))
