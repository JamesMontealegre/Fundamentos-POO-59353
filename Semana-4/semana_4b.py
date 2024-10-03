class Author:
    def __init__(self, name):
        self.name = name
        self.books = []
    
    def __str__(self):
        return f"{self.name}"
    
    def add_book(self, book):
        self.books.append(book)
    
    def get_books(self):
        return self.books
    

class Book:
    def __init__(self, title: str, pages: int, author: Author):
        self.title = title
        self.pages = pages
        self.author = author

    def __repr__(self):
        return f"Book(title={self.title}, pages={self.pages}, author={self.author})"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def get_books(self):
        return self.books


# ------

def main():

    author_1 = Author('Gabriel')
    author_2 = Author('Neruda')

    book_1 = Book('Cien años de soledad', 493, author_1)
    book_2 = Book('El coronel no tiene quien le escriba', 703, author_1)
    book_3 = Book('La felicidad', 293, author_2)

    # print(author_1)

    author_1.add_book(book_1)
    author_1.add_book(book_2)
    author_2.add_book(book_3)

    books_author2 = author_2.get_books()

    library = Library()

    library.add_book(book_1)
    library.add_book(book_2)
    library.add_book(book_3)


    list_books = library.get_books()

    for book in list_books:
        print(book.author)


main()








# for book in books_author2:
#     print(book)

# print(author_1)


# print(author_1)
# print(book_1)