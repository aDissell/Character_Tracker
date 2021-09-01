class Character:
    def __init__(self, name = "Default", hp = 10, ac = 10, stren = 10, dex = 10, con = 10, wis = 10, intel = 10, chari = 10):
        self.name = name
        self.hp = hp
        self.ac = ac
        self.stren = stren
        self.dex = dex
        self.con = con
        self.wis = wis
        self.intel = intel
        self.chari = chari

    def my_name(self):
        print(self.name)

    def display_name(self):
        print("Name : " + self.name)
    
    def my_hp(self):
        print("HP : " + str(self.hp))

    def my_ac(self):
        print("AC : " + str(self.ac))
    
    def my_stren(self):
        print("Str : " + str(self.stren))
    
    def my_dex(self):
        print("Dex : " + str(self.dex))

    def my_con(self):
        print("Con : " + str(self.con))
    
    def my_wis(self):
        print("Wis : " + str(self.wis))
    
    def my_intel(self):
        print("Int : " + str(self.intel))
    
    def my_chari(self):
        print("Cha : " + str(self.chari))

    def show_stats(self):
        self.display_name()
        self.my_hp()
        self.my_ac()
        self.my_stren()
        self.my_dex()
        self.my_con()
        self.my_wis()
        self.my_intel()
        self.my_chari()
        print('')