import numpy as np
from PIL import Image # pillow
import matplotlib.pyplot as plt

def main():
    img = Image.open('Images/lena_gray_512.tif')

    #converte image para vetor numpy    
    npImg = np.array(img)

    #converter a imagem pra negativo
    npImg = 255-npImg

    #diminui pela metade a intensidade
    npImg = npImg/2

    #colocar quatro quadrados brancos de 10x10
    npImg[0:10,0:10] = 255
    npImg[501:511,501:511] = 255
    npImg[501:511,0:10] = 255
    npImg[0:10,501:511] = 255

    #incluir um quadrado preto no centro 15x15
    npImg[249:264,249:264] = 0

    # converte numpy array to Image
    imgNew = Image.fromarray(npImg)

    # Plot using matplotlib
    fig, ax = plt.subplots(nrows=2, ncols=2)
    ax[0,0].imshow(img, cmap='gray')
    ax[0,0].set_title("Imagem original")
    ax[0,1].imshow(imgNew, cmap='gray')    
    ax[0,1].set_title("Imagem filtrada")
    plt.show()  


if __name__ == "__main__":
    main()