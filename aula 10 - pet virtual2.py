class Pet:
    def __init__(self, nome):
        self.nome = nome
        self.fome = 50
        self.felicidade = 50

    def mostrar(self):
        print("\n🐶 Meu pet:", self.nome)
        print("Fome:", self.fome)
        print("Felicidade:", self.felicidade)

    def comer(self):
        self.fome = max(0, self.fome - 20)
        print(self.nome, "comeu!")

    def brincar(self):
        self.felicidade = min(100, self.felicidade + 20 )
        self.fome = min(100, self.fome + 10)
        print(self.nome, "está brincando!")

pet = Pet("Rex")

while True:
    print("\n=== MEU PET VIRTUAL ===")
    print("1 - Ver pet")
    print("2 - Dar comida")
    print("3 - Brincar")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        pet.mostrar()
    elif opcao == "2":
        pet.comer()
    elif opcao == "3":
        pet.brincar()
    elif opcao == "0":
        print("Até logo! Cuide bem do Rex!")
        break
    else:
        print("Opção inválida!")
