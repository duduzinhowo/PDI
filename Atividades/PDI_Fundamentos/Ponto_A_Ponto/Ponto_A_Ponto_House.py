#Exemplo de leitura e plot de imagens
#Lembrar de adicionar as bibiotecas: Numpy, Pillow, Matplotlib
import numpy as np
from PIL import Image # pillow
import matplotlib.pyplot as plt
def main():
img = Image.open('house.tif')
#img.show() # Plot image using Pillow
# converte image to numpy array
npImg = np.array(img)
#Calcular o negativo das imagens
npImg = 255-npImg
#Diminuir pela metade a intensidade dos pixels
npImg = npImg/2
#Incluir 4 quadrados brancos 10 x 10 pixels em cada canto das imagens
npImg[0:10,0:10] = 255
npImg[501:511,501:511] = 255
npImg[501:511,0:10] = 255
npImg[0:10,501:511] = 255
#Incluir 1 quadrado preto 15X15 no centro das imagens
npImg[249:264,249:264] = 0
#Converte numpy array to Image
imgNew = Image.fromarray(npImg)
#imgNew.show()
# Plot using matplotlib
fig, ax = plt.subplots(nrows=2, ncols=2)
ax[0,0].imshow(img, cmap='gray')
ax[0,0].set_title("Imagem original")
ax[0,1].imshow(imgNew, cmap='gray')
ax[0,1].set_title("Imagem modificada")
plt.show()
if __name__ == "__main__":
main()
