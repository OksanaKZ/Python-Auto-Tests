# Автоматизация тестирования с помощью Selenium и Python

<details>
<summary>Виртуальное окружение</summary>
  
Активировать:  
```
selenium_env\Scripts\activate.bat
```
Деактивировать:  
```
deactivate.bat
```
</details>

<details>
<summary>Поиск элементов с помощью Selenium</summary>
  
+ find_element(By.ID, value) — поиск по уникальному атрибуту id элемента;
+ find_element(By.CSS_SELECTOR, value) — поиск элемента с помощью правил на основе CSS;
+ find_element(By.XPATH, value) — поиск с помощью языка запросов XPath;
+ find_element(By.NAME, value) — поиск по атрибуту name элемента;
+ find_element(By.TAG_NAME, value) — поиск элемента по названию тега элемента;
+ find_element(By.CLASS_NAME, value) — поиск по значению атрибута class;
+ find_element(By.LINK_TEXT, value) — поиск ссылки на странице по полному совпадению;
+ find_element(By.PARTIAL_LINK_TEXT, value) — поиск ссылки на странице, если текст селектора совпадает с любой частью текста ссылки.
</details>
