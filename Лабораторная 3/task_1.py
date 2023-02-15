class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    @property
    def name(self):
        return self._name

    @property
    def author(self):
        return self._author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    """ Бумажная книга - дочерний класс книги. """
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self._pages = pages

    @property
    def pages(self):
        return self._pages

    @pages.setter
    def pages(self, new_pages):
        if not isinstance(new_pages, int):
            raise AttributeError("Number of pages should be an integer")
        if new_pages <= 0:
            raise AttributeError("Number of pages should be a positive number")
        self._pages = new_pages

    def __str__(self):
        return f"Бумажная книга {self.name}. Автор {self.author}. Количество страниц {self.pages}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self.pages!r})"


class AudioBook(Book):
    """ Аудио книга - дочерний класс книги. """
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        
        self._duration = duration

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, new_duration):
        if (not isinstance(new_duration, float)) and (not isinstance(new_duration, int)):
            raise AttributeError("Duration should be float or integer")
        if new_duration <= 0:
            raise AttributeError("Duration should be a positive number")
        self._duration = new_duration

    def __str__(self) -> str:
        return f"Аудио книга {self.name}. Автор {self.author}, Длительность {self.duration}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, duration={self.duration!r})"


if __name__ == "__main__":
    book = Book(name="Преступление и наказание", author="Ф.М. Достоевский")
    print(book)
    print(repr(book))
    print()

    paper_book = PaperBook(name="Преступление и наказание", author="Ф.М. Достоевский", pages=672)
    print(paper_book)
    print(repr(paper_book))
    print()

    audio_book = AudioBook(name="Преступление и наказание", author="Ф.М. Достоевский", duration=742.4)
    print(audio_book)
    print(repr(audio_book))
    print()
