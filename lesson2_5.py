
from selenium import webdriver
from selenium.webdriver.common.by import By
import math
browser = webdriver.Chrome()
link = "http://suninjuly.github.io/redirect_accept.html"
browser.get(link)



browser.find_element(By.XPATH, "/html/body/form/div/div/button").click()

new_window = browser.window_handles[1]
browser.switch_to.window(new_window)
x_element = browser.find_element(By.CSS_SELECTOR, '#input_value')
x = x_element.text
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

y = calc(x)
browser.find_element(By.ID, "answer").send_keys(y)

browser.find_element(By.XPATH, "/html/body/form/div/div/button").click()
print(y)