# Membuat Calculator sederhana

print('Selamat Datang di Kalkulator Sederhana')
def tambah():
            number1 = input("masukkan angka pertama = ")
            number2 = input("masukkan angka kedua = ")
            result = int(number1) + int(number2)
            print(f"hasil penjumlahan dari {number1} + {number2} = {result}")
            return result
def kurang():
            number1 = input("masukkan angka pertama = ")
            number2 = input("masukkan angka kedua = ")
            result = int(number1) - int(number2)
            print(f"hasil penjumlahan dari {number1} - {number2} = {result}")
            return result


def calculator():
    operations =input("Silahkan pilih orperasi matematika (+/-) ")
    if operations == "+":
            tambah()
    elif operations == "-":
            kurang()
        
        
calculator()
