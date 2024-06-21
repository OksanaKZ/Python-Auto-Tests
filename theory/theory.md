<details>
<summary>Code Style</summary>

### Отступы:  
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

### Известные принципы написания кода DRY (Don't repeat yourself) и KISS (Keep it simple, stupid). 

* Пишите максимально простой код везде, где это возможно.
* Не используйте переусложненных конструкций без большой необходимости (поменьше лямбда-выражений, map и разной другой магии). Если кусок кода можно заменить конструкцией более простой для понимания — замените.
* Пишите максимально линейный код, где это возможно, это проще для восприятия.
* Избегайте большой вложенности блоков кода, такие конструкции тяжело читать.
* Если можно вынести повторяющуюся логику куда-то, выносите, не повторяйтесь.
* По возможности пишите явный код вместо неявного. Чем меньше магии "под капотом", тем лучше.
</details>

<details>

<summary>ООП</summary>

### Базовые принципы ООП  
* Абстракция — отделение концепции от ее экземпляра;
* Полиморфизм — реализация задач одной и той же идеи разными способами;
* Наследование — способность объекта или класса базироваться на другом объекте или классе. Это главный механизм для повторного использования кода. Наследственное отношение классов четко определяет их иерархию;
* Инкапсуляция — размещение одного объекта или класса внутри другого для разграничения доступа к ним.

### Главное:  
* Инкапсулируйте все, что может изменяться;
* Уделяйте больше внимания интерфейсам, а не их реализациям;
* Каждый класс в вашем приложении должен иметь только одно назначение;
* Классы — это их поведение и функциональность.

### Используйте следующее вместе с наследованием
* Делегация — перепоручение задачи от внешнего объекта внутреннему;
* Композиция — включение объектом-контейнером объекта-содержимого и управление его поведением; последний не может существовать вне первого;
* Агрегация — включение объектом-контейнером ссылки на объект-содержимое; при уничтожении первого последний продолжает существование.

### Не повторяйся (Don’t repeat yourself — DRY)
Избегайте повторного написания кода, вынося в абстракции часто используемые задачи и данные. Каждая часть вашего кода или информации должна находиться в единственном числе в единственном доступном месте. Это один из принципов читаемого кода.

### Принцип единственной обязанности
Для каждого класса должно быть определено единственное назначение. Все ресурсы, необходимые для его осуществления, должны быть инкапсулированы в этот класс и подчинены только этой задаче.

### Принцип открытости/закрытости
Программные сущности должны быть открыты для расширения, но закрыты для изменений.

### Принцип подстановки Барбары Лисков
Методы, использующие некий тип, должны иметь возможность использовать его подтипы, не зная об этом.

### Принцип разделения интерфейсов
Предпочтительнее разделять интерфейсы на более мелкие тематические, чтобы реализующие их классы не были вынуждены определять методы, которые непосредственно в них не используются.

### Принцип инверсии зависимостей
Система должна конструироваться на основе абстракций “сверху вниз”: не абстракции должны формироваться на основе деталей, а детали должны формироваться на основе абстракций.

</details>