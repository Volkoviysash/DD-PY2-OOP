BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]


# TODO написать класс Book
class Book:
    """ Класс, описывающий объект Книга, который будет использоваться для книг, которые хранятся в библиотеке. """
    def __init__(self, id_: int, name: str, pages: int):
        self.id = id_
        self.name = name
        self.pages = pages


# TODO написать класс Library
class Library:
    """
    Класс, описывающий модель библиотеки
    """
    def __init__(self, books: list = None) -> None:
        if books is None:
            books = []
        self.books = books

    def get_next_book_id(self) -> int:
        """"
        Метод возвращает id для добавления новой книги.
        Если книги нет - возвращается 1,
        Если есть, то возвращается id последней книги, увеличенный на 1

        :return: id для новой книги
        """
        if len(self.books) < 1:
            return 1
        else:
            return len(self.books) + 1

    def get_index_by_book_id(self, id_: int):
        """
        Метод возвращает индекс книги в списке

        :raise ValueError: Если книги с запрашиваемым id не существует

        :return: Индекс книги
        """
        for index, book in enumerate(self.books):
            if id_ == index + 1:
                return index
        raise ValueError("Книги с запрашиваемым id не существует")


if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1
