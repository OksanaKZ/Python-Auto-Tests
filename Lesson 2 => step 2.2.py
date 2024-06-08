#Задание: работа с выпадающим списком

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time 

link = "https://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    a = browser.find_element(By.ID, "num1")
    a = int(a.text)
    b = browser.find_element(By.ID, "num2")
    b = int(b.text)
    y = str(a + b)

    select = Select(browser.find_element(By.ID, "dropdown"))
    select.select_by_value(y)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    time.sleep(30)
    browser.quit()

#Задание на execute_script

from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "https://SunInJuly.github.io/execute_script.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.ID, "input_value")
    x = int(x_element.text)
    y = calc(x)
    
    input1 = browser.find_element(By.ID, "answer")
    browser.execute_script("return arguments[0].scrollIntoView(true);", input1)
    input1.send_keys(y)

    option1 = browser.find_element(By.ID, "robotCheckbox")
    option1.click()

    option2 = browser.find_element(By.ID, "robotsRule")
    option2.click()

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    time.sleep(30)
    browser.quit()

#Задание: загрузка файла

from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
import os

link = "https://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.NAME, "firstname")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.NAME, "lastname")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.NAME, "email")
    input3.send_keys("Smolensk")

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')  
    element = browser.find_element(By.ID, "file")
    element.send_keys(file_path)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    time.sleep(30)
    browser.quit()
