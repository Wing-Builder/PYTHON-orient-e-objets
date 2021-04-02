class People:

    def __init__(self,name,age,ville,enfants):
        self.name = name
        self.age = age
        self.ville = ville
        self.enfants = enfants
        self.liste_achats = []

    def __str__(self):
        return self.name

    def Achat(self, list_items):
        self.liste_achats.append(list_items)