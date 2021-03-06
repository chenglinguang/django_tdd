#!/usr/bin/env python3 

#-*-coding:utf-8-*-

from selenium import webdriver
import unittest

class NewVisitorTest(unittest):
    
    def setUp(self):
        self.browser=webdriver.Firefox()
    def tearDown(self):
        self.browser.quit()
        self.browser.implicitly_wait(3)
    def test_can_start_a_list_and_retrieve_it_later(self):
        self.browser.get('http://localhost:8000')
        self.assertIn('To-Do',self.browser.title)
        self.fail('Finish the test!')

if __name__=='__main__':
    unittest.main(warnings='ignore')



