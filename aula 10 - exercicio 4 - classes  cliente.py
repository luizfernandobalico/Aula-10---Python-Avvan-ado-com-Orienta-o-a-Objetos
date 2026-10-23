class Cliente:
    def __init__(self, nome, nota):
        self.nome = nome
        self.nota = nota

    def mostrar_dados(self):
        print("Nome:", self.nome)
        print("Nota:", self.nota)

    def verificar_nota(self):
        if self.nota >= 7:
            print("Cliente aprovado!")
        else:
            print("Cliente em consome razoavel!")

# Criando um objeto
cliente1 = Cliente("Ana Beatriz", 9)

# Chamando os métodos
cliente1.mostrar_dados()
cliente1.verificar_nota()