import numpy as np
import matplotlib.pyplot as plt
colunas = 28
linhas = 10
image_matrix = np.zeros([linhas, colunas])
print(image_matrix.shape)
#Coluna L
image_matrix[1:8,4] = 255
#Linha L
image_matrix[7,4:8] = 255

#Coluna1 H
image_matrix[1:8,9] = 255
#Coluna2 H
image_matrix[1:8,12] = 255
#Linha H
image_matrix[4,9:13] = 255

#Coluna1 B
image_matrix[1:8,14] = 255
#Linha1 B
image_matrix[1,14:17] = 255
#Linha2 B
image_matrix[4,14:17] = 255
#Linha3 B
image_matrix[7,14:17] = 255
#Curva1 B
image_matrix[2:4,17] = 255
#Curva2 B
image_matrix[5:7,17] = 255

#Coluna C
image_matrix[2:7,19] = 255
#Linha2 C
image_matrix[1,20:22] = 255
#Linha2 C
image_matrix[7,20:22] = 255
#Curva1 C
image_matrix[2,22] = 255
#Curva2 C
image_matrix[6,22] = 255

plt.imshow(image_matrix, cmap='gray')
plt.show()