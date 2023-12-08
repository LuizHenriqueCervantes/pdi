import cv2
import numpy as np
import matplotlib.pyplot as plt

#Receber a imagem
imagem = cv2.imread(r'C:\Users\hrick\Documents\VsCode\Python\PDI\Atividades\Intensidade\fractured_spine.jpg')

# Aplicar o método de transformação logarítmica
imagem_log = 150 * (np.log(imagem + 1))
imagem_log = np.array(imagem_log, dtype=np.uint8)

# Exibir ambas as imagens
plt.imshow(imagem)
plt.show()
plt.imshow(imagem_log)
plt.show()