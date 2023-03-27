class Person: 
    def __init__(self):
        self.prenom = ""
        self.nom = ""

    def presenter(self, prenom, nom):
        print("bonjour je m'appel", prenom + nom)

person1 = Person()
person2 = Person()

person1.presenter("jhon", " doe")
person2.presenter("maya", "l'abeille")
