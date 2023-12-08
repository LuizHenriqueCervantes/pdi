import cv2
import numpy as np

#Receber a imagem
img = cv2.imread(r'C:\Users\hrick\Documents\VsCode\Python\PDI\Atividades\Intensidade\fractured_spine.jpg')

#Tentar 4 valores diferentes
for gamma in [0.1, 0.5, 1.2, 2.2]:
	
	#Aplicar correção gama
	gama_corrigido = np.array(255*(img / 255) ** gamma, dtype='uint8')

	#Salvar imagens editadas
	cv2.imwrite('gamma_transformed' + str(gamma) + '.jpg', gama_corrigido)