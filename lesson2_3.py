import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import math
browser = webdriver.Chrome()
link = "http://suninjuly.github.io/alert_accept.html"
browser.get(link)

browser.find_element(By.XPATH, "/html/body/form/div/div/button").click()
confirm = browser.switch_to.alert
confirm.accept()

x_element = browser.find_element(By.CSS_SELECTOR, '#input_value')
x = x_element.text
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

y = calc(x)
browser.find_element(By.ID, "answer").send_keys(y)

browser.find_element(By.XPATH, "/html/body/form/div/div/button").click()
print(y)