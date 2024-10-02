class Author:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book: 'Book'):
        self.books.append(book)

    def get_books_(self):
        for book in self.books:
            print(book)

    def get_books__(self):
        return self.books

    def get_books(self):
        return f"Libros del autor={[book.title for book in self.books]}"

    def __str__(self):
        return f"Autor: {self.name}"

#________________________

class Book:
    def __init__(self, title: str, pages: int, author: Author):
        self.title = title
        self.pages = pages
        self.author = author

    def __str__(self):
        return f"Libro: {self.title}"

    


#________________________

class Library:
    def __init__(self):
        self.books = []




def print_list(array: list[Book]):
    for book in array:
        print(f"Libros asociados al author: {book.title} ")



author_1 = Author(name='Gabriel Garcia Márquez')
book_1 = Book('Cien años de soledad', 473, author_1)
author_1.add_book(book_1)



# print(author_1)
# print(book_1)
print_list(author_1.books)



#Llamado de atributos de clase

# print(author_1.get_books())
