from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Sets up a Chrome browser.
def setup():
  browser = webdriver.Chrome(executable_path="./chromedriver.exe")
  browser.maximize_window()
  return browser

# Clicks an element on the page.
def click_el(actions, element):
  actions.move_to_element(element).click().perform()

def type_in_el(element, text):
  element.send_keys(text)

def enter(element):
  element.send_keys(Keys.ENTER)