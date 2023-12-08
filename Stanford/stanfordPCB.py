import cv2
import numpy as np

#Carregar as imagens a serem comparadas
placa_sem_defeito = cv2.imread('pcbCroppedTranslated.png')
placa_com_defeito =cv2.imread('pcbCroppedTranslatedDefected.png')

#Condicional para a comparação
if placa_sem_defeito.shape == placa_com_defeito.shape:

    diferenca = cv2.absdiff(placa_sem_defeito, placa_com_defeito)
    diferenca_em_escala_de_cinza = cv2.cvtColor(diferenca,cv2.COLOR_BGR2GRAY)
    _, thresholded = cv2.threshold(diferenca_em_escala_de_cinza, 30, 255, cv2.THRESH_BINARY)
    contornos, _ = cv2.findContours(thresholded, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    #plotar as imagens
    resultado = cv2.drawContours(placa_com_defeito.copy(), contornos, -1, (0, 0, 255), 2)
    cv2.imshow('Resultado', resultado)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

#Erro caso as imagens sejam diferentes
else:
    print("As imagens têm dimensões diferentes.")