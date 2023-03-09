import doctest


class Phone:
    """
    Документация на класс
    Класс описывает модель телефона
    """
    def __init__(self, brand: str, model: str):
        """
        Создание и подготовка к работе объекта "телефон"

        :param brand: Название бренда, выпустившего телефон
        :param model: Номер модели телефона

        Примеры:
        >>> iphone13pro = Phone("Apple", "Iphone 13 PRO")
        """
        if not isinstance(brand, str):
            raise TypeError("Название бренда должно быть типа str")
        self.brand = brand

        if not isinstance(model, str):
            raise TypeError("Название модели должно быть типа str")
        self.model = model

        self.phone_number = None

    def install_app(self, app_name: str) -> bool:
        """
        Метод устанавливает приложение на телефон.
        :param: app_name: Название приложения, которое необходимо установить
        :raise TypeError: Если название приложения не является строкой

        :return: Успешность выполнения действия: true - если приложение установлено, в ином случае false

        Примеры:
        >>> iphone13pro = Phone("Apple", "Iphone 13 PRO")
        >>> iphone13pro.install_app("Microsoft Teams")
        """
        ...

    def init_phone_number(self, phone_number: int) -> bool:
        """
        Метод добавляет сим карту в телефон и активирует возможность совершать вызовы.

        :param: phone_number: Номер телефона абонента, которому нужно позвонить

        :return: Успешность выполнения действия: true - если сим-карта установлена, в ином случае false
        """
        ...

    def call(self, target_phone_number) -> None:
        """
        Метод совершает звонок другому человеку.
        :param target_phone_number: Номер телефона собеседника

        :raise TypeError: Если номер телефона не является целым числом,
        :raise ValueError: Если номер телефона не соответсвует формату,
        то возвращается ошибка.

        Пример:
        >>> iphone13pro = Phone("Apple", "Iphone 13 PRO")
        >>> iphone13pro.call(8951234567)
        """
        ...


class Student:
    """
    Документация на класс
    Класс описывает модель студента
    """
    def __init__(self, full_name: str, university: str, course: int):
        """
        Создание и подготовка к работе объекта "студент"

        :param full_name: Полное ФИО студента
        :param university: Название учебного заведения
        :param course: Номер курса

        Примеры:
        >>> student_Petrov = Student("Петров Алексей Алексеевич", "Политех", 3)  # инициализация экземпляра класса
        """
        if not isinstance(full_name, str):
            raise TypeError("Имя должно быть типа str")
        self.name = full_name

        if not isinstance(university, str):
            raise TypeError("Название университета должно быть типа str")
        self.university: university

        if not isinstance(course, int):
            raise TypeError("Номер курса должен быть типа int")
        if course <= 0:
            raise ValueError("Номер курса должен быть положительным числом")
        self.course = course

    def pass_exam(self, exam: str) -> int:
        """
        Метод предполагает сдачу экзамена студентом
        :param exam: название экзамена который сдает студент

        :return: Оценка за экзамен
        Примеры:
        >>> student_Petrov = Student("Петров Алексей Алексеевич", "Политех", 3)
        >>> student_Petrov.pass_exam("История")
        """
        ...

    def switch_course(self) -> None:
        """
        Метод обновляет номер курса по итогам учебного года
        Номер курса может увеличиться на единицу в случае успешной сдачи всех экзаменов
        или не измениться в случае если хотябы 1 экзамен не был сдан на положительную оценку
        """
        ...

    def graduation(self) -> None:
        """
        Метод предполагает завершение обучения студентом и лишения его статуса студента
        """
        ...


class Gun:
    """
    Документация на класс
    Класс описывает модель пистолета
    """
    def __init__(self, model: str, number_of_bullets: int):
        """
       Создание и подготовка к работе объекта "пистолет"
       :param model: Полное название модели пистолета
       :param number_of_bullets: Количество патронов в магазине

       Примеры:
       >>> makarov = Gun("Пистолет Макарова 56-А-125", 8)  # инициализация экземпляра класса
       """
        if not isinstance(model, str):
            raise TypeError("Название модели должно быть типа str")
        self.model = model

        if not isinstance(number_of_bullets, int):
            raise TypeError("Название модели должно быть типа int")
        self.number_of_bullets = number_of_bullets

        self.is_loaded = False  # изначально пистолет незаряжен
        self.fuse_position = False # Положение предохранителя

    def reload(self) -> None:
        """
        Метод перезаряжает пистолет, если он не заряжен и не делает ничего, если пистолет уже заряжен
        Примеры:
        >>> makarov = Gun("Пистолет Макарова 56-А-125", 8)
        >>> makarov.reload()
        """
        ...

    def shoot(self) -> bool:
        """
        Метод производит выстрел с пистолета

        :return: Успешность совершения действия: true если выстрел был произведен и false, если нет

        Пример:
        >>> makarov = Gun("Пистолет Макарова 56-А-125", 8)
        >>> makarov.shoot()
        """
        ...

    def put_on_fuse(self) -> None:
        """
        Метод ставит пистолет на предохранитель, блокируя возможность выстрела
        Меняет значение атрибута экземпляра класса fuse_position

        Пример:
        >>> makarov = Gun("Пистолет Макарова 56-А-125", 8)
        >>> makarov.put_on_fuse()
        """
        ...


if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    doctest.testmod()
