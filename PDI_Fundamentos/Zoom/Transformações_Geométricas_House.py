#TRANSFORMAÇÕES GEOMÉTRICAS
import numpy as np
from numpy import asarray
from PIL import Image
from scipy import ndimage
def main():
#Selecionar imagem
image_in = Image.open('house.tif')
image_in.show()
#Conversão imagem array
image_np = np.array(image_in)
print(image_np.shape)
#Zoom
image_np_zoom = ndimage.zoom(image_np, (2.5, 2.5))
print(image_np_zoom.shape)
image_out = Image.fromarray(image_np_zoom)
image_out.show()
if __name__ == "__main__":
main()