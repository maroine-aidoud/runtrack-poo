
class Rectangle:
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur

    def get_longueur(self):
        return self.__longueur

    def set_longueur(self, longueur):
        self.__longueur = longueur

    def get_largeur(self):
        return self.__largeur

    def set_largeur(self, largeur):
        self.__largeur = largeur

# création d'un rectangle avec longueur 10 et largeur 5
mon_rectangle = Rectangle(10, 5)

# modification des valeurs de longueur et de largeur
mon_rectangle.set_longueur(15)
mon_rectangle.set_largeur(8)

# affichage des valeurs modifiées
print("Longueur :", mon_rectangle.get_longueur())
print("Largeur :", mon_rectangle.get_largeur())