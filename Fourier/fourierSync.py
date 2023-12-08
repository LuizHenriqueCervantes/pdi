import numpy as np
import matplotlib.pyplot as plt

#Definir o tamanho da imagem
largura = 512
altura = 512

#Criar uma matriz de zeros para representar o fundo branco
imagem = np.zeros((altura, largura))

#Definir as coordenadas da figura
x_min = largura // 4
x_max = 3 * largura // 4
y_min = altura // 4
y_max = 3 * altura // 4

#Desenhar o quadrado na imagem com altura dada pela função sinc
for x in range(x_min, x_max):
    for y in range(y_min, y_max):
        distancia_x = (x - largura // 2) / (largura // 2)
        distancia_y = (y - altura // 2) / (altura // 2)
        sinc_value = np.sinc(distancia_x) * np.sinc(distancia_y)
        imagem[y, x] = sinc_value

#Plotar o resultado
plt.imshow(imagem, cmap='gray')
plt.title('Quadrado Simulando Função Sinc')
plt.axis('off') # Oculta os eixos
plt.show()