class Product():
    def __init__(self,name, price, stock):
      self.name = name
      self.price = price
      self.stock = stock

    def __str__(self) :
       return f"nama: {self.name}, harga: {self.price}, Stok: {self.stock}"


class Store():
  def __init__(self, name) :
    self.name = name
    self.products = []

  def add_product(self, product):
     self.products.append(product)

  def remove_product(self,product):
     self.products.remove(product)

  def display_product(self):
     print(f"Selamat Datang di Toko {self.name}\n")
     print(f"Daftar produk di toko {self.name}\n ")
     for id, product in enumerate (self.products,start=1):
        print(f"{id}. {product}")

      
def main():
    toko = Store("XYZ")

    Product1 = Product("Baju",100000,10)
    product2 = Product("Celana",150000,5)
    product3 = Product("Sepatu",300000,3)

    toko.add_product(Product1)
    toko.add_product(product2)
    toko.add_product(product3)
    toko.display_product()

    print(f"\nhapus {product3.name} dari toko")
    toko.remove_product(product3)
    toko.display_product()

if __name__ == "__main__":
    main()


