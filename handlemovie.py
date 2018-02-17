# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.support.ui import Select
import pprint, random

l_key = [u'영화']

def probe(d_pkt):
    text = d_pkt['text']
    for key in l_key:
        if text.find(key) >= 0:
            return True
    return False

def handle(d_pkt):
    url = 'https://torrentkim12.com/torrent_movie/torrent1.htm'
    
    options = webdriver.ChromeOptions()
    # options.binary_location = '/usr/local/bin/chromedriver'
    options.add_argument('headless')
    driver = webdriver.Chrome(chrome_options=options)
    driver.implicitly_wait(3)
    driver.get(url)

    # process final html
    r = ''
    l_el = driver.find_elements_by_xpath("//*[@id='bbs_latest_list']/table/tbody/tr/td[1]/a[contains(@href, '../torrent_movie/')]")
    l_el.extend(driver.find_elements_by_xpath("//*[@id='bbs_latest_list']/table/tbody/tr/td[2]/a[contains(@href, '../torrent_movie/')]"))
    for el in l_el:
        r += '{0} : {1}\n'.format(el.text, el.get_attribute("href"))
    return r

if __name__ == "__main__":
    print(handle({}))
