# -*- coding: utf-8 -*-

# references:
#  https://beomi.github.io/gb-crawling/posts/2017-01-20-HowToMakeWebCrawler.html
#  https://stackoverflow.com/questions/11465555/can-we-use-xpath-with-beautifulsoup

import time
import pprint, random
import requests
import json
import os

import urllib
from lxml import etree
from bs4 import BeautifulSoup

l_key = ['acmicpc', u'백준온라인']
TIME_DELAY = 2

def probe(d_pkt):
  text = d_pkt['text']
  for key in l_key:
    if text.find(key) >= 0:
      return True
  return False

def handle(d_pkt):
  return pickone()

def pickone():
  return ''

def printLinks(url):
  response = urllib.request.urlopen(url)
  htmlparser = etree.HTMLParser()
  tree = etree.parse(response, htmlparser)
  # l = tree.xpath('//*[@id="wrapper"]/section[2]/div[2]/div/div[1]/div[3]/ul[1]/li[1]/a')
  #                '//*[@id="wrapper"]/section[2]/div[2]/div/div[1]/div[3]/ul[1]'
  #                '//*[@id="wrapper"]/section[2]/div[2]/div/div[1]/div[3]/ul[2]'
  el_div = tree.xpath('//*[@id="wrapper"]/section[2]/div[2]/div/div[1]/div[3]')[0]
  l_ch   = el_div.getchildren()
  for el_ch in l_ch:
    if el_ch is None:
      continue
    if el_ch.tag == 'h4':
      print('## {0}'.format(el_ch.text))
      print('')
    elif el_ch.tag == 'ul':
      l_a   = el_ch.xpath('//li/a')
      for el_a in l_a:
        if el_a is not None and el_a.text is not None:
          print('  * 백 | [{0}]({1})'.format(el_a.text.strip(), el_a.get('href').strip()))
      print('')

if __name__ == "__main__":
  printLinks(r'https://code.plus/course/41')
  printLinks(r'https://code.plus/course/42')
  printLinks(r'https://code.plus/course/18')
  printLinks(r'https://code.plus/course/17')  
  printLinks(r'https://code.plus/course/16')
  printLinks(r'https://code.plus/course/5')
  printLinks(r'https://code.plus/course/6')
  printLinks(r'https://code.plus/course/9')
  printLinks(r'https://code.plus/course/10')
  