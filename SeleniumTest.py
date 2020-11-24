# coding = utf-8
import sys
import time
from selenium import webdriver
from selenium.webdriver import ActionChains

if __name__ == "__main__":
    option = webdriver.ChromeOptions()
    option.add_argument('disable-infobars')
    option.binary_location = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
    browser = webdriver.Chrome(chrome_options=option,executable_path=r"C:\Users\fcm\Downloads\chromedriver_win32 (1)\chromedriver.exe")
    browser.get(url='http://127.0.0.1:9000/ywfz/cqswzcty/ndtyjhbz/index.jsp')
    username = browser.find_element_by_id('username')
    password = browser.find_element_by_id('password')
    submitButton = browser.find_element_by_id('submitButton')
    action = ActionChains(browser)
    action.send_keys_to_element(username, "chenyan2523")
    action.send_keys_to_element(password, "1")
    action.click(submitButton)
    action.perform()
    time.sleep(5)
    browser.get(url="http://127.0.0.1:9000/ywfz/cqswzcty/ndtyjhbz/index.jsp")
    time.sleep(5)
    #browser.close()
    sys.exit(0)
