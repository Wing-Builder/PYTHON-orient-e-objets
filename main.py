# from People import People

# P = Poeple("Marc", 18, "Dammarie", 0,)

# # P.Achat("Tomates")

# print(P.Achat("Tomates"))

from PlayerRPG import PlayerRPG
from Potion import Potion

Hero = PlayerRPG("Mage")

Potion1 = Potion("Vie")
Potion2 = Potion("Force")
Potion3 = Potion("Defense")

Hero.inventaire.append("Potion1")
Hero.inventaire.append("Potion2")
Hero.inventaire.append("Potion3")

Hero.open_inventory()