class PlayerRPG:

    def __str__(self):
        return self.name

    def __init__(self, role):
        if role == "Guerrier":
            self.force = 10
            self.defense = 100
            self.points_de_vie = 100
        elif role == "Mage":
            self.force = 20
            self.defense = 150
            self.points_de_vie = 100

    def open_inventory(self):
        for item in self.inventaire:
            print(item)

    def drink_potion(self,type):
        for potion in self.inventaire:
            if potion.type == effect:
                potion.number_use -= 1
                if potion.type == "Soin":
                    self.pv += potion.power
                if potion.type == "Force":
                    self.force += potion.power
                if potion.effect == "Defence":
                    self.defence += potion.power
                if potion.utility_num == 0:
                    self.inventaire.remove(potion)

# def drink_potion(self,effect):
#         for potion in self.inventaire:
#             if potion.effect == effect:
#                 potion.number_use -= 1
#                 if potion.effect == "Soin":
#                     self.pv += potion.power
#                 if potion.effect == "Force":
#                     self.force += potion.power
#                 if potion.effect == "Defence":
#                     self.defence += potion.power
#                 if potion.number_use <= 0:
#                     self.inventaire.remove(potion)
#                 return 
