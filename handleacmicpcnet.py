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
  l_a   = el_div.xpath('//ul/li/a')
  for el_a in l_a:
    if el_a is not None and el_a.text is not None:
      print('  - 백 | [{0}]({1})'.format(el_a.text.strip(), el_a.get('href').strip()))

  # req = requests.get(url)
  # html = req.text
  # soup = BeautifulSoup(html, 'html.parser')
  # my_titles = soup.select('div > div.col-md-8 > div.lecture-explain.gist-preview.markdown-table > ul:nth-child(14) > li:nth-child(1)')
  # print(my_titles)

def printTitles(url):
  response = urllib.request.urlopen(url)
  htmlparser = etree.HTMLParser()
  tree = etree.parse(response, htmlparser)
  # l = tree.xpath('//*[@id="wrapper"]/section[2]/div[2]/div/div[1]/div[3]/ul[1]/li[1]/a')
  #                '//*[@id="wrapper"]/section[2]/div[2]/div/div[1]/div[3]/ul[1]'
  #                '//*[@id="wrapper"]/section[2]/div[2]/div/div[1]/div[3]/ul[2]'
  el_div = tree.xpath('//*[@id="wrapper"]/section[2]/div[2]/div/div[1]/div[3]')[0]
  l_h4   = el_div.xpath('//h4')
  for el_h4 in l_h4:
    if el_h4 is not None:
      print('### {0}'.format(el_h4.text))

def printMd(url):
  printTitles(url)
  printLinks(url)

if __name__ == "__main__":
  printMd(r'https://code.plus/course/41')
  printMd(r'https://code.plus/course/42')
  printMd(r'https://code.plus/course/18')
  printMd(r'https://code.plus/course/17')  
  printMd(r'https://code.plus/course/16')
  printMd(r'https://code.plus/course/5')
  printMd(r'https://code.plus/course/6')
  printMd(r'https://code.plus/course/9')
  printMd(r'https://code.plus/course/10')
  