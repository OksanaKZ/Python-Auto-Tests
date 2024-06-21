# Задание: составные сообщения об ошибках

def test_input_text(expected_result, actual_result):
    assert actual_result == expected_result, f"expected {expected_result}, got {actual_result}"

# Задание: составные сообщения об ошибках и поиск подстроки

def test_substring(full_string, substring):
    assert substring in full_string, f"expected '{substring}' to be substring of '{full_string}'"

#Задание: оформляем тесты в стиле unittest 

import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link1 = "http://suninjuly.github.io/registration1.html"
link2 = "http://suninjuly.github.io/registration2.html"
text_expected = "Congratulations! You have successfully registered!"

class TestLinks(unittest.TestCase):
    
    def reg_form(self, lnk):
        browser = webdriver.Chrome()
        browser.get(lnk)
        browser.find_element(By.CSS_SELECTOR, ".first_block .first_class input").send_keys("Ivan")
        browser.find_element(By.CSS_SELECTOR, ".first_block .second_class input").send_keys("Petrov")
        browser.find_element(By.CSS_SELECTOR, ".first_block .third_class input").send_keys("abc@gmail.com")
        browser.find_element(By.CSS_SELECTOR, "button.btn").click()
        time.sleep(1)
        return browser.find_element(By.TAG_NAME, "h1").text

    def test_link1(self):
        self.assertEqual(self.reg_form(link1), text_expected, "Should be expected text")

    def test_link2(self):
        self.assertEqual(self.reg_form(link2), text_expected, "Should be expected text")

if __name__ == "__main__":
    unittest.main()

#вывод в консоль
FAILED (errors=1)
