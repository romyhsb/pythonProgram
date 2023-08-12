class calculator():
    def __init__(self, num1, num2) :
        self.num1 = num1
        self.num2 = num2

    def add(self):
        hasil = self.num1 + self.num2
        return print(f"Hasil penjumlahan {self.num1} + {self.num2} = {hasil} ")
    
    def subtract(self):
        hasil = self.num1 -self.num2
        return print(f"Hasil pengurangan {self.num1} - {self.num2} = {hasil}")
    
    def multiply(self):
        hasil = self.num1 * self.num2
        return print(f"hasil perkalian {self.num1} * {self.num2} = {hasil}")
    
    def divide(self):
        if self.num2 != 0 :
            hasil = self.num1  / self.num2
            return print(f"Hasil pembagian {self.num1} / {self.num2} = {hasil}")
        else :
            print("Terjadi Kesalahan")
            
def main():    
    number = calculator(10,5)
    number2 = calculator(10,0)
    number.add()
    number.subtract()
    number.multiply()
    number.divide()
    number2.divide()

if __name__ == "__main__":
    main()