import numpy as np
import matplotlib.pyplot as plt

# Carregar imagem do diretório
imagem = plt.imread('periodic_noise.png')

#Calcular a transformada de Fourier
transformada_fourier = np.fft.fft2(imagem)

#Deslocar a frequencia zero
transformada_fourier_deslocada = np.fft.fftshift(transformada_fourier)

#Calculo do espectro de magnitude (magnitude da Transformada de Fourier)
espectro_magnitude = np.abs(transformada_fourier_deslocada)

#Crie uma figura com duas subtramas
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

#Plotar imagem original
ax1.imshow(imagem, cmap='gray')
ax1.set_title('Imagem Original')

#Plotar Fourier 
ax2.imshow(np.log(espectro_magnitude), cmap='gray')
ax2.set_title('Espectro de Magnitude da Transformada de Fourier')
plt.show()