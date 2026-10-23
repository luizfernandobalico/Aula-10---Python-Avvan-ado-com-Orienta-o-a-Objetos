import matplotlib.pyplot as plt

dia = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta"]
vendas = [100, 90, 130, 150, 90]

#plt.bar(dia, vendas)

plt.title("Gráfico de Vendas")
plt.xlabel("Dia")
plt.ylabel("Vendas")
plt.plot(dia, vendas)

plt.show()