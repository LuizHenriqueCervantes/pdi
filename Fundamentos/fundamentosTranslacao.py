from PIL import Image
import PIL.ImageOps
import glob

#Abrir imagem do diretório
files = glob.glob(r"C:\Users\hrick\Documents\VsCode\Python\PDI\Imagens\lena_gray_512.tif")

#Translação da imagem
for f in files:
    image = Image.open(f)
    inverted_image = PIL.ImageOps.invert(image)
    width, height = image.size
    shifted_image = Image.new("RGB", (width+35, height))
    shifted_image.paste(image, (35, 45))

    #Plotar a imagem
    shifted_image.show()
