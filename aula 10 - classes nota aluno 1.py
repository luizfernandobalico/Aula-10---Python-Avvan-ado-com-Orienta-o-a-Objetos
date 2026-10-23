class Aluno:
    def __init__(self, nome, nota):
        self.nome = nome
        self.nota = nota

    def mostrar_dados(self):
        print("Nome:", self.nome)
        print("Nota:", self.nota)

    def verificar_nota(self):
        if self.nota >= 7:
            print("Aluno aprovado!")
        else:
            print("Aluno em recuperação!")

# Criando um objeto
aluno1 = Aluno("Carlos", 8)

# Chamando os métodos
aluno1.mostrar_dados()
aluno1.verificar_nota()