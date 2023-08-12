print("Welcome To XYZ Library\n")

class Book():
    
    def __init__(self, title,author,year) :
        self.title = title
        self.author = author
        self.year = year

    def __str__(self) :
        return f"Judul: {self.title}, Penulis: {self.author}, Tahun: {self.year}\n"


class Library():
    def __init__(self,name) :
        self.name = name
        self.books = []

    def add_book(self,book):
        self.books.append(book)
        
    def remove_book(self,book):
        self.books.remove(book)
        print("daftar buku setelah dihapus")

    def display_books(self):
        print(f"daftar buku di perpustakaan {self.name}\n")
        for idx, book in enumerate(self.books,start=1) :
            print(f"{idx}. {book}")

        
perpustakaan = Library(" Perpustakaan XYZ")

book1 = Book("Pyhton For Beginners","Jhon Doe",2002)
book2 = Book("Intro to OOP","Jane Smith",2021)
book3 = Book("Data scine Basics","Michael Jhonson",2023)

perpustakaan.add_book(book2)
perpustakaan.add_book(book1)
perpustakaan.add_book(book3)
perpustakaan.display_books()
perpustakaan.remove_book(book2)
perpustakaan.display_books()

# perpustakaan.remove_book(book2)
