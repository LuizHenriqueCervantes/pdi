import numpy as np
import matplotlib.pyplot as plt
import cv2

#Carregar a imagem di diretório
imagem = cv2.imread('biel.png', cv2.IMREAD_GRAYSCALE)

#Calcular o espectro de Fourier da imagem
espectro_fourier = np.fft.fft2(imagem)
espectro_fourier_centralizado = np.fft.fftshift(espectro_fourier)

#Dimensões da imagem
altura, largura = imagem.shape

#Criar grades de frequência para a aplicação dos filtros
x, y = np.meshgrid(np.arange(-largura/2, largura/2),
np.arange(-altura/2, altura/2))
raio = np.sqrt(x**2 + y**2)

#Definir frequência de corte para os filtros passa-altas
frequencia_corte = 40

#Filtro passa-alta ideal (inverso do passa-baixa ideal)

filtro_alta = (raio > frequencia_corte).astype(float)
# Filtro Butterworth passa-alta (inverso do passa-baixa Butterworth)
ordem_butterworth = 3
filtro_butterworth_alta = 1 - (1 / (1 + (raio / frequencia_corte)**(2 *
ordem_butterworth)))

#Filtro gaussiano passa-alta (inverso do passa-baixa gaussiano)
sigma = 40
filtro_gaussiano_alta = 1 - np.exp(-raio**2 / (2 * (sigma**2)))

#Aplicar os filtros ao espectro de Fourier
espectro_filtrado_alta = espectro_fourier_centralizado * filtro_alta
espectro_filtrado_butterworth_alta = espectro_fourier_centralizado * filtro_butterworth_alta
espectro_filtrado_gaussiano_alta = espectro_fourier_centralizado * filtro_gaussiano_alta

#Transformada inversa de Fourier para obter as imagens filtradas
imagem_filtrada_alta = np.abs(np.fft.ifft2(np.fft.ifftshift(espectro_filtrado_alta)))
imagem_filtrada_butterworth_alta = np.abs(np.fft.ifft2(np.fft.ifftshift(espectro_filtrado_butterworth_alta)))
imagem_filtrada_gaussiano_alta = np.abs(np.fft.ifft2(np.fft.ifftshift(espectro_filtrado_gaussiano_alta)))

#Exibir as imagens
plt.figure(figsize=(12, 12))

#Imagem original
plt.subplot(3, 4, 1)
plt.imshow(imagem, cmap='gray')
plt.title('Imagem Original')

#Espectro de Fourier
plt.subplot(3, 4, 2)
plt.imshow(np.log(np.abs(espectro_fourier_centralizado) + 1),
cmap='gray')
plt.title('Espectro de Fourier')

#Filtro Passa-Alta Ideal
plt.subplot(3, 4, 3)
plt.imshow(filtro_alta, cmap='gray')
plt.title('Filtro Passa-Alta Ideal')
plt.subplot(3, 4, 4)
plt.imshow(imagem_filtrada_alta, cmap='gray')
plt.title('Imagem após Filtro Passa-Alta Ideal')

#Filtro Butterworth Passa-Alta
plt.subplot(3, 4, 7)
plt.imshow(filtro_butterworth_alta, cmap='gray')
plt.title('Filtro Butterworth Passa-Alta')
plt.subplot(3, 4, 8)
plt.imshow(imagem_filtrada_butterworth_alta, cmap='gray')
plt.title('Imagem após Filtro Butterworth Passa-Alta')

#Filtro Gaussiano Passa-Alta
plt.subplot(3, 4, 11)
plt.imshow(filtro_gaussiano_alta, cmap='gray')
plt.title('Filtro Gaussiano Passa-Alta')
plt.subplot(3, 4, 12)
plt.imshow(imagem_filtrada_gaussiano_alta, cmap='gray')
plt.title('Imagem após Filtro Gaussiano Passa-Alta')
plt.tight_layout()
plt.show()