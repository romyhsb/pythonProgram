class Hero():
    # variabel static
    jumlah = 0
    def __init__(self, inputName, inputHealth, inputPower, inputArmor) :
        # instance variabel atau variabel object
        self.name = inputName
        self.health = inputHealth
        self.power = inputPower
        self.armor = inputArmor

    # membuat method object
    # object void, atau tanpa argument atau parameter
    def sayHay(self):
        print(f"saya adalah hero {self.name} ")

    # method denga parameter (disini akan menambah heatlh hero)\
    def upHealth(self,up):
        self.health += up
        print(f"darah saya sekarang berjumlah {self.health}")

    # method dengan return 
    # def plusHealth(self):
    #     return self.health
    
hero1 = Hero("miya",100,12,3)
hero1.sayHay()
hero1.upHealth(10)
