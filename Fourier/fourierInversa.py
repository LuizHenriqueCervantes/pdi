import numpy as np
import matplotlib.pyplot as plt

#Carregar imagem do diretório
imagem = plt.imread('periodic_noise.png')

#Calcular a Transformada de Fourier 
transformada_fourier = np.fft.fft2(imagem)

#Deslocar a frequência zero para o centro
transformada_fourier_deslocada = np.fft.fftshift(transformada_fourier)

#Calcular o espectro de magnitude de Fourier
espectro_magnitude = np.abs(transformada_fourier_deslocada)

#Calcular a transformada inversa de Fourier
imagem_reconstruida = np.fft.ifft2(np.fft.ifftshift(transformada_fourier_deslocada))

#Normalizar a imagem
imagem_reconstruida = np.abs(imagem_reconstruida)

#Criar figura com três subtramas
fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(18, 6))

#Plotar as imagens
ax1.imshow(imagem, cmap='gray')
ax1.set_title('Imagem Original')
ax2.imshow(np.log(espectro_magnitude), cmap='gray')
ax2.set_title('Espectro de Magnitude da Transformada de Fourier')
ax3.imshow(imagem_reconstruida, cmap='gray')
ax3.set_title('Imagem Reconstruída')
plt.show()