from selenium.webdriver import ActionChains
import time
from lib import setup, click_el, type_in_el, enter

def execute():
  first_user = setup()
  second_user = setup()

  first_user.get('https://bairdchat.azurewebsites.net')
  second_user.get('https://bairdchat.azurewebsites.net')
  actions1 = ActionChains(first_user)
  actions2 = ActionChains(second_user)

  time.sleep(2)

  first_name_input = first_user.find_element_by_id('userInput')
  second_name_input = second_user.find_element_by_id('userInput')

  first_connect = first_user.find_element_by_id('connection-form-btn')
  second_connect = second_user.find_element_by_id('connection-form-btn')

  type_in_el(first_name_input, "John Doe")
  type_in_el(second_name_input, "Moto Moto")

  time.sleep(4)

  click_el(actions1, first_connect)
  click_el(actions2, second_connect)

  time.sleep(2)

  first_message_input = first_user.find_element_by_id('messageInput')
  second_message_input = second_user.find_element_by_id('messageInput')

  type_in_el(first_message_input, "Howdy!")
  type_in_el(second_message_input, "You as big as you plumpy!")

  enter(first_message_input)
  enter(second_message_input)

  time.sleep(3)

  first_user.close()
  second_user.close()