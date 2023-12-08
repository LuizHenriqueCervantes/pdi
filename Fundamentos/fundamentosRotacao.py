from PIL import Image

#Ler a imagem do diretório
im = Image.open(r"C:\Users\hrick\Documents\VsCode\Python\PDI\Imagens\lena_gray_512.tif")

#Definir os graus de rotação
angulo45 = 45
angulo90 = 90
angulo100 = 100

#Aplicar a rotação nas imagens
out45 = im.rotate(angulo45)
out90 = im.rotate(angulo90)
out100 = im.rotate(angulo100)

#plotar as imagens
im.show()
out45.show()
out90.show()
out100.show()