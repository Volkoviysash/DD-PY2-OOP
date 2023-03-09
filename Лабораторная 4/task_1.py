import doctest

 class BasePhone:
     """Класс описывает базовую модель телефона"""
     def __init__(self, phone_number: str) -> None:
         """
         Создание и подготовка к работе объекта "мобильный телефон"
         :param _phone_number: Номер телефона

         :raise AttributeError - если номер телефона невалидный

         Примеры:
         >>> base_phone = BasePhone("+79512345678")
         """
         if BasePhone.is_phone_number_valid(phone_number):
             self._phone_number = phone_number
         else:
             raise AttributeError("Неверный формат номера!")

     def __str__(self) -> str:
         return f'Телефон с номером {self.phone_number}'

     def __repr__(self) -> str:
         return f'{self.__class__.__name__}({self.phone_number})'

     @staticmethod
     def is_phone_number_valid(phone_number: str, minimal_length: int = 6) -> bool:
         """
         Метод проверяет, валидность номера телефона
         :param phone_number: Номер телефона
         :param minimal_length (optional): Минимальная длина номера телефона, может варьироваться, по умолчанию 6 символов

         :return True - Если номер валидный, иначе False
         """
         if not isinstance(phone_number, str):
             return False
         if len(phone_number) <= minimal_length:
             return False
         return True

     @property
     def phone_number(self) -> str:
         return self._phone_number

     def call(self, output_number: str) -> None:
         """
         Метод позволяет совершить вызов на номер
         :output_number: Номер телефона на который будет совершен вызов

         :raise ValueError: Если номер телефона, на который совершается звонок совпадает с текущим номером телефона
         """
         if output_number == self.phone_number:
             raise ValueError('Нельзя позвонить самому себе!')
         if not BasePhone.is_phone_number_valid(output_number):
             raise ValueError('Нельзя позвонить на этот номер!')
         return f'Вызывается абонент с номером {output_number}.'

     def ring(self) -> str:
         """
         Метод срабатывает, когда происходит входящий вызов
         """
         return 'Дзынь-Дзынь! Вам звонят'

        
 class MobilePhone(BasePhone):
     """Класс описывает модель мобильного телефона"""
     def __init__(self, phone_number: str, model: str) -> None:
         """
         Создание и подготовка к работе объекта "мобильный телефон"
         :phone_number: Номер телефона
         :param model: Номер модели телефона
         """
         super().__init__(phone_number)
         self._model = model

     def __str__(self) -> str:
         return f'Мобильный телефон - {self.model} с номером {self.phone_number}'

     def __repr__(self) -> str:
         return f'{self.__class__.__name__}(phone_number={self.phone_number!r}, phone_model={self.model!r})'

     @property
     def model(self) -> str:
         """Модель устанавливается один раз и в дальнейшем не может быть изменена"""
         return self._model

     @property
     def phone_number(self) -> None:
         return self._phone_number

     @phone_number.setter
     def phone_number(self, new_phone_number: str) -> str:
         """У мобильного телефона есть функция замены симкарты и соответственно изменение номера"""
         if BasePhone.is_phone_number_valid(new_phone_number):
             self._phone_number = new_phone_number
         else:
             raise AttributeError("Неверный формат номера телефона")   

     def ring(self, input_number: str) -> str:
         """Метод входящего вызова, так как мобильный телефон может определить номер, с которого звонят"""
         return f'Дзынь-дзынь! Вам звонят с номера {input_number}'
        
        
 class HomePhone(BasePhone):
     """Класс описывате модель домашнего телефона"""
     def __init__(self, phone_number: str, region: str) -> None:
         """
         Создание и подготовка к работе объекта "домашний телефон"
         :param _region: Регион, в котором может работать телефон, настраивается оператором связи и может быть изменен
         :param phone_number: Номер телефона
         """
         super().__init__(phone_number)
         self._region = region

     def __str__(self) -> str:
         return f'Домашний телефон с номером {self.phone_number}, регион {self._region}'

     def __repr__(self) -> str:
         return f'{self.__class__.__name__}(phone_number={self.phone_number!r}, region={self._region!r})'

     @property
     def region(self) -> str:
         """getter для аттрибута region"""
         return self._region

     @region.setter
     def region(self, new_region: str) -> None:
         """setter для аттрибута region, который настраивается оператором связи и может быть изменен"""
         if not isinstance(new_region, str):
             raise AttributeError("Регион должен быть типа string")
         self._region = new_region

   
if __name__ == '__main__':
   doctest.testmod()
   base_phone = BasePhone('+11111111')
   mobile_phone = MobilePhone(phone_number='+22222222', model="Iphone 13")
     home_phone = HomePhone(phone_number='+22222222', region="Moskow")
