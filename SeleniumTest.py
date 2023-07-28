# coding = utf-8
import sys
import time

from Cython.Plex import Actions
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

url = 'http://192.168.1.120:32785/login'
user_name = "fyfei1470"
password = "abcd1234*"

class SeleniumTest:
    browser = None

    def login(self):
        option = webdriver.ChromeOptions()
        option.add_argument('disable-infobars')
        option.binary_location = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
        self.browser = webdriver.Chrome(chrome_options=option)
        self.browser.get(url='http://192.168.1.120:32785/login')
        time.sleep(1)
        username = self.browser.find_elements_by_class_name("el-input__inner")
        submit = self.browser.find_elements_by_class_name("button-login")
        actions = ActionChains(self.browser);
        actions.send_keys_to_element(username[0], user_name)
        actions.send_keys_to_element(username[1], password)
        actions.click(submit[0])
        actions.perform()

    def openMenu(self):
        self.browser.get("http://192.168.1.120:32785/ad-scrap#/bfsbdj/index")

    def query(self):
        filter1 = self.browser.find_element_by_xpath("//input[@placeholder='审批级别']")
        actions = ActionChains(self.browser);
        actions.click(filter1)
        actions.perform()
        time.sleep(1)
        filter_value = self.browser.find_elements_by_class_name("el-select-dropdown__item")[1]
        actions1 = ActionChains(self.browser);
        actions1.click(filter_value)
        actions1.perform()

if __name__ == "__main__":
    sel = SeleniumTest()
    sel.login()
    time.sleep(1)
    sel.openMenu()
    time.sleep(4)
    sel.query()
    #time.sleep(5)
    #browser.close()
    #sys.exit(0)
