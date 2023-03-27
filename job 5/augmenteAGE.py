class Animal:
    def __init__(self):
        self.age = 0
        self.prenom = ""

    def viellir(self):
        self.age += 1
        return self.age
    
    def nommer(self, prenom):
        self.prenom = prenom
        print("l'animal se nomme ", self.prenom)


animal1 = Animal()

print(animal1.viellir())
print(animal1.nommer("bibish"))
