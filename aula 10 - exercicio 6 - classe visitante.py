class Visitante:
    def __init__(self, nome, produto, preco, quantidade):
        self.nome = nome
        self.produto = produto
        self.preco = preco
        self.quantidade = quantidade

    def calcular_venda(self):
        return self.preco * self.quantidade

    def mostrar_dados(self):
        print("\n--- Dados do Vendedor ---")
        print("Nome:", self.nome)
        print("Produto:", self.produto)
        print("Preço: R$", self.preco)
        print("Quantidade:", self.quantidade)
        print("Total da venda: R$", self.calcular_venda())


# Criando um objeto da classe
vendedor1 = Visitante("Andre", "Notebook", 2500, 2)

# Mostrando os dados
vendedor1.mostrar_dados()
