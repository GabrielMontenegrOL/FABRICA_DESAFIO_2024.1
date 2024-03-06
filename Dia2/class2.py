class Animal:
    def __init__(self, nome, etnia, porte, idade):
        self.nome = nome
        self.etnia = etnia
        self.porte = porte
        self.idade = idade

class Dog(Animal):
    def som(self):
        return "AUUUUUUU"
    
    def ExibirInfoAnimais(self):
        print(self.nome, self.etnia, self.porte, self.idade)
    
class Cat(Animal):
    def som(self):
        return "Miau"
    
    def ExibirInfoAnimais(self):
        print(self.nome, self.etnia, self.porte, self.idade)

dog1 = Dog("Safira", "Pincher", "Supremo", "999")
cat1 = Cat("Katy", "Default", "normal", "3 anos")

print(dog1.som())
print(cat1.som())
cat1.ExibirInfoAnimais()
dog1.ExibirInfoAnimais()
