class Book():
    def __init__(self, title, author, year) :
        self.title = title
        self.author = author
        self.year = year


    def __str__(self) -> str:
         return f"Judul: {self.title}, Penulis: {self.author}, Tahun Terbit: {self.year}\n"


class library():
    def __init__(self,nama) :
        self.nama = nama
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def display_book(self):
        print(f"Manajemen Buku Perpustakaan {self.nama}\n")
        print(f"Daftar Buku")
        for idx, book in enumerate (self.books, start=1):
            print(f"{idx}. {book}")
      

  
def main(): 
      perpustakaan1 = library("sunan")
      book1 = Book("Harry Potter and the Philosopher\'s Stone","J.K Rowling",1997)
      book2 = Book("To Kill a Mockingbird","Harper Lee",1960)
      book3 = Book("The Great Gatsby","F. Scott Fitzgerald",1925)

      perpustakaan1.add_book(book1)
      perpustakaan1.add_book(book2)
      perpustakaan1.add_book(book3)

      perpustakaan1.display_book()

if __name__ == "__main__":
    main()


    