from selenium.webdriver import ActionChains
import time
from lib import setup, click_el

def execute():
  browser = setup()
  browser.get("https://zachbaird.me")

  # Wait for the browser to load the page.
  time.sleep(2)

  actions = ActionChains(browser)

  theme_switch = browser.find_element_by_id('input-25')
  click_el(actions, theme_switch)
  time.sleep(2)
  browser.close()