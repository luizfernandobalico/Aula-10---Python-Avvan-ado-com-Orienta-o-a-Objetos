class Vendedor:
    def __init__(self, nome, nota):
        self.nome = nome
        self.nota = nota

    def mostrar_dados(self):
        print("Nome:", self.nome)
        print("Nota:", self.nota)

    def verificar_nota(self):
        if self.nota >= 7:
            print("Vendedor aprovado!")
        else:
            print("Vendedor em experiência!")

# Criando um objeto
aluno1 = Vendedor("Celso", 9)

# Chamando os métodos
aluno1.mostrar_dados()
aluno1.verificar_nota()