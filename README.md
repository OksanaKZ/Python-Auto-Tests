## Автоматизация тестирования с помощью Selenium и Python

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

<details>
<summary>Методы</summary>
  
Открыть веб-страницу в браузере
```
driver.get()
```
Закрыть текущее окно браузера  
```
browser.close()
```
Закрыть все окна, вкладки и процессы вебдрайвера, запущенные во время тестовой сессии
```
browser.quit()
```
Cнять/поставить галочку в элементе типа checkbox или выбрать опцию из группы radiobuttons 
```
option1 = browser.find_element(By.CSS_SELECTOR, "[value='python']")
option1.click()
```
Можно также отметить нужный пункт, выполнив метод click() на элементе label  
```
option1 = browser.find_element(By.CSS_SELECTOR, "[for='java']")
option1.click()
```
</details>

---


> Конструкция try/finally:  
> Даже если в коде внутри блока try произойдет какая-то ошибка, то код внутри блока finally выполнится в любом случае.


> Атрибут text:  
> Возвращает текст, который находится между открывающим и закрывающим тегами элемента. Например, .text для данного элемента \<div class="message">У вас новое сообщение\</div> вернёт строку: "У вас новое сообщение".

Для проверки ожидаемого результата используется инструкция **assert**, которая проверяет истинность утверждений: *assert True* не приводит к выводу дополнительных сообщений, а вот *assert False* вызовет исключение AssertionError. При вызове assert можно через запятую написать сообщение, которое будет выведено в случае ошибки проверки результата:
```
assert abs(-42) == -42, "Should be absolute value of a number"

Traceback (most recent call last):

  File "<stdin>", line 1, in <module>

AssertionError: Should be absolute value of a number
```

Для решения проблем и упрощения написания и запуска тестов существуют специальные фреймворки, которые называются **test runners** (тест-раннеры). Можно выделить три основных тестовых фреймворка для Python: *unittest*, *PyTest* и *nose*. Модуль unittest является встроенным инструментом Python — и это его большой плюс. PyTest и nose устанавливаются дополнительно, они позволяют получить расширенные возможности по сравнению с unittest.  
Общее правило для всех фреймворков: название тестового метода должно начинаться со слова "test_".  
Для unittest существуют собственные дополнительные правила:
+ Тесты обязательно должны находиться в специальном тестовом классе.
+ Вместо assert должны использоваться специальные assertion методы.  

<details>
<summary>Команды Pytest</summary>
  
py.test test_sample.py --collect-only # собирает информацию тестового набора  

py.test test_sample.py -v # выводит вербозные сообщения  

py.test -q test_sample.py # опустить вывод имени файла

python -m pytest -q test_sample.py # вызов pytest через python

py.test --markers # показать доступные маркеры  

py.test -k "TestClass, а не test_one" # запускать только тесты с именами, которые соответствуют "строковому выражению"  

py.test -x # останавливаться после первой неудачи

py.test --maxfail=2 # останавливаться после двух неудач

py.test --showlocals # показывать локальные переменные в трассировках  

py.test -l # (сокращение)

py.test --tb=long # информативное форматирование трассировки по умолчанию  

py.test --tb=native # форматирование стандартной библиотеки Python  

py.test --tb=short # более короткий формат возвратов к трассировке  

py.test --tb=line # только одна строка для каждого сбоя  

py.test --tb=no # отсутствие вывода трассировки  

py.test -x --pdb # при первом сбое сброс в PDB, затем завершение сеанса тестирования

py.test --durations=10 # список 10 самых медленных длительностей теста.

py.test --maxfail=2 -rf # выход после двух сбоев, сообщение о сбое.

py.test -n 4 # посылать тесты на несколько процессоров

py.test -m slowest # запускать тесты с декоратором @pytest.mark.slowest или slowest = pytest.mark.slowest; @slowest

py.test --traceconfig # выяснить, какие плагины py.test активны в вашем окружении.

py.test --instafail # если установлен pytest-instafail, показывать ошибки и сбои мгновенно, а не ждать окончания набора тестов.

</details>
