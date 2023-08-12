class Transaction():
    def __init__(self, transaction_type, amount, description) :
        self.transaction_type = transaction_type
        self.amount = amount
        self.description = description

    def __str__(self) -> str:
        return f"Jenis: {self.transaction_type}, Jumlah: {self.amount}, Keterangan: {self.description}"
    

class Account(Transaction):
    def __init__(self, owner) :
        self.owner = owner
        self.balance = 0
        self.transactions = []

    def deposit(self, transaction):
        if transaction.transaction_type == "Pendapatan" or "pendapatan":
            self.balance += transaction.amount
            self.transactions.append(transaction)
        else :
            print("Transaksi hanya bisa dilakukan untuk Pendapatan")

    def withdraw(self, transaction):
        if transaction.transaction_type == "Pengeluaran" or "pengeluaran":
            if transaction.amount <= self.balance:
                self.balance -= transaction.amount
                self.transactions.append(transaction)
            else:
                print("saldo tidak cukup")
        else:
            print("transaksi windraw hanya bisa dilakukan untuk pengeluaran")

    def display_transactions(self):
        print(f"Selamat Datang Di Manajemen Keuangan!")
        print("Daftar Transaksi")
        for idx, transaction in enumerate(self.transactions, start=1):
            print(f"{idx}. {transaction}\n")
        print(f"Saldo akun: {self.balance}")

def main():
    pemilik = Account("Romi")

    transaksi1 = Transaction("Pendapatan",500000,"Pendapatan Bulan Juli")
    transaksi2 = Transaction("Pengeluaran",150000,"Belanja Bulanan")
    transaksi3 = Transaction("pendapatan",100000,"Bonus Kerja")


    pemilik.deposit(transaksi1)
    pemilik.withdraw(transaksi2)
    pemilik.deposit(transaksi3)
    
    pemilik.display_transactions()


if __name__ == "__main__":
    main()

        