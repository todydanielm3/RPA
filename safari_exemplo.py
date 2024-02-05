# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os

# path to selenium server standalone jar, downloaded here:
# http://docs.seleniumhq.org/download/
# or a direct url:
# http://selenium-release.storage.googleapis.com/2.41/selenium-server-standalone-2.41.0.jar
os.environ["SELENIUM_SERVER_JAR"] = "selenium-server-standalone-2.41.0.jar"
# note: I've put this jar file in the same folder as this python file

browser = webdriver.Safari()

# makes the browser wait if it can't find an element
browser.implicitly_wait(10)

browser.get("http://google.com/")

search_box = browser.find_element_by_name("q")
search_button = browser.find_element_by_name("btnK")

browser.find_element("name", "q")
#search_input = browser.find_element_by_css_selector("#gbqfq")
#search_input.send_keys("python SELENIUM_SERVER_JAR turn logging off")
#search_input.send_keys(Keys.RETURN)

raw_input("Press Enter to close...")

browser.quit()

search_box.send_keys("Python")
search_button.click()

# Tira um print da p¿ina e salva em um arquivo
time.sleep(5) # Aguarda 5 segundos
driver.save_screenshot("screenshot.png")
