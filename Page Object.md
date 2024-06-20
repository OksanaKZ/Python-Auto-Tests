<details>
<summary>Code Style</summary>

  Отступы:  
```
# тест вне класса: отступа нет
def test_student_can_see_lesson_name_in_lesson_in_course_after_joining(self, driver):
    # все строки внутри теста с отступом
    page = CoursePromoPage(url=self.course.url, driver=driver)
    page.open()


class TestLessonNameInCourseForTeacher():
    @pytest.mark.regression
    # тест внутри класса, нужен дополнительный отступ
    def test_teacher_can_see_lesson_name_in_lesson_in_course(self, driver):
        # еще один отступ для каждой строки, и так с любым уровнем вложенности
        page = LessonPlayerPage(url=self.lesson_url, driver=driver)
        page.open()
        try:
            # плюс один отступ на каждый уровень вложенности
            dangerous_function()
        except:
            close_something()
```

Функции пишутся через_нижнее_подчеркивание:
```
def test_guest_can_see_lesson_name_in_lesson_without_course(self, driver):
```
Классы пишут с помощью CamelCase:
```
class TestLessonNameWithoutCourseForGuest():
```
Константы пишут в стиле UPPERCASE:
```
MAIN_PAGE = "/catalog"
```
</details>

<details>

<summary>ООП</summary>

### Главное:  
* Инкапсулируйте все, что может изменяться;
* Уделяйте больше внимания интерфейсам, а не их реализациям;
* Каждый класс в вашем приложении должен иметь только одно назначение;
* Классы — это их поведение и функциональность.

### Базовые принципы ООП  
* Абстракция — отделение концепции от ее экземпляра;
* Полиморфизм — реализация задач одной и той же идеи разными способами;
* Наследование — способность объекта или класса базироваться на другом объекте или классе. Это главный механизм для повторного использования кода. Наследственное отношение классов четко определяет их иерархию;
* Инкапсуляция — размещение одного объекта или класса внутри другого для разграничения доступа к ним.
</details>
