#!/usr/bin/env python3 

#-*-coding:utf-8-*-

from selenium import webdriver

browser=webdriver.FireFox()

browser.get('http://localhost:8000')

assert 'Django' in browser.title

