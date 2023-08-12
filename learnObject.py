class Hero():
    # variabel static atau variabel classnya
    jumlah = 0

    def __init__(self,inputName, inputHealth, inputArmor):
        # ini merupakan variabel dari objectnya(hanya berpengaruh ke object yaitu hero1 dan seterusnya)
        self.name = inputName
        self.health = inputHealth
        self.armor = inputArmor

        Hero.jumlah += 1
        print(f"menambahkan hero baru dengan nama {self.name}")
        print(f"Hero ke {Hero.jumlah}")
        
# hero1 = Hero()  masih seperti prosedural programming belum seperti oop
# hero2 = Hero()

# hero1.name = "zilong"
# hero1.attackPower = 1500

# hero2.name = "martis"
# hero2.attackPower = 2000

# print(hero1)
# print(hero1.__dict__)
# print(hero2.__dict__)
# print(hero2.name)

# kalau oop seperti ini

hero1 = Hero("zilong",100,10)
hero2 = Hero("martis",200,13)
hero3 = Hero("miya",100,13)


#del hero1.name  untuk menghapus object dalam class

# print(hero1.__dict__)
