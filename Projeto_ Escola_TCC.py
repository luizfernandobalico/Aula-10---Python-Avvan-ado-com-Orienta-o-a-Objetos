# Imagem da escola 
import cv2 # Imagem da escola 

# Abrir a imagem
imagem = cv2.imread("foto 6.jpg")

# Verificar se a imagem foi encontrada
if imagem is None:
    print("Imagem não encontrada!")
else:
    print("Imagem carregada com sucesso!")

    # Mostrar a imagem
    cv2.imshow("Minha Imagem", imagem)

    # Esperar uma tecla
    cv2.waitKey(0)

    # Fechar a janela
    cv2.destroyAllWindows()
     # Final da Imagem da escola

     # Alunos e Grafico

import matplotlib.pyplot as plt

nomes = []
notas = []

for i in range(4):
    nome = input("Digite o nome do aluno: ")
    nota = float(input("Digite a nota do aluno: "))

    nomes.append(nome)
    notas.append(nota)

plt.plot(nomes, notas, marker="o")
plt.title("Notas dos Alunos")
plt.xlabel("Nomes dos Alunos")
plt.ylabel("Notas")
plt.ylim(0, 10)
plt.grid(True)
plt.show()

# Gráfico final 

# CAM ativada

import cv2

camera = cv2.VideoCapture(0)

while True:
    ret, frame = camera.read()

    if ret:
        cv2.imshow("Webcam Aberta", frame)

    if cv2.waitKey(1) == 27:
        break

camera.release()
cv2.destroyAllWindows()

# Cam desativada