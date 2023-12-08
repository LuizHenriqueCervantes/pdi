import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

#Carregar a imagem do diretório
imagem = plt.imread('periodic_noise.png')

#Calcualar a Transformada de Fourier 2D da imagem
transformada_fourier = np.fft.fft2(imagem)

#Descolar a frequência zero para o centro da imagem
transformada_fourier_deslocada = np.fft.fftshift(transformada_fourier)

#Calcular o espectro de magnitude (magnitude da Transformada de Fourier)
espectro_magnitude = np.abs(transformada_fourier_deslocada)

#Criar uma grade de coordenadas para o espectro 3D
coord_x = np.arange(-imagem.shape[1] // 2, imagem.shape[1] // 2)
coord_y = np.arange(-imagem.shape[0] // 2, imagem.shape[0] // 2)
coord_x, coord_y = np.meshgrid(coord_x, coord_y)

#Criar uma figura com duas subtramas
fig = plt.figure(figsize=(15, 6))

#Plot
ax1 = fig.add_subplot(121)
ax1.imshow(imagem, cmap='gray')
ax1.set_title('Imagem Original')
ax2 = fig.add_subplot(122, projection='3d')
ax2.plot_surface(coord_x, coord_y, np.log(espectro_magnitude),
cmap='viridis')
ax2.set_xlabel('Frequência Horizontal')
ax2.set_ylabel('Frequência Vertical')
ax2.set_zlabel('Log(Espectro de Magnitude)')
ax2.view_init(elev=20, azim=30)
plt.show()