import numpy as np
from numpy import asarray
from PIL import Image
from scipy import ndimage
 
def main():

    #Abrir imagem no diretorio
    image_in = Image.open(r"C:\Users\hrick\Documents\VsCode\Python\PDI\Imagens\lena_gray_512.tif")
    image_in.show()
    
    #Converter a imagem para um vertor NumPy   
    image_np = np.array(image_in)
    print(image_np.shape)

    #Operação de Zoom
    image_np_zoom = ndimage.zoom(image_np, (0.75, 0.75))
    print(image_np_zoom.shape)
    image_out = Image.fromarray(image_np_zoom)  
    image_out.show()

if __name__ == "__main__":
    main()
