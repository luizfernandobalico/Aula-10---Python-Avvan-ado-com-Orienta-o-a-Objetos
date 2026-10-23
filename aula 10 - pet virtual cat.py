class Pet:
    def __init__(self, nome):
        self.nome = nome

    def brincar(self):
        print(self.nome, "está brincando!")

    def comer(self):
        print(self.nome, "está comendo!")

# Criando o pet
meu_pet = Pet("Grajola")

# Interagindo com o pet
print("Meu pet se chama", meu_pet.nome)
meu_pet.brincar()
meu_pet.comer()