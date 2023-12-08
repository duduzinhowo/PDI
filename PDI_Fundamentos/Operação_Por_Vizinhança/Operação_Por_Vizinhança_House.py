import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
def main():
image_pillow = Image.open('house.tif')
f_image_nd = np.array(image_pillow)
g_image_nd = np.zeros(f_image_nd.shape)
p_image_nd = np.zeros(f_image_nd.shape)
# Operação por vizinhaça
l = f_image_nd.shape[0]
c = f_image_nd.shape[1]
k = 3 #kernel size
for x in range(k, l-k):
for y in range(k, c-k):
s_xy = f_image_nd[x-k:x+k+1, y-k:y+k+1]
g_image_nd[x,y] = np.mean(s_xy).astype(int)
p_image_nd[x,y] = np.median(s_xy).astype(int)
#Criando colunas para plotagem
fig = plt.figure()
plt1 = plt.subplot(1,3,1)
plt2 = plt.subplot(1,3,2)
plt3 = plt.subplot(1,3,3)
plt1.title.set_text('Original')
plt1.imshow(f_image_nd, cmap='gray')
plt2.title.set_text('Média')
plt2.imshow(g_image_nd, cmap='gray', vmin=0, vmax=255)
plt3.title.set_text('Mediana')
plt3.imshow(p_image_nd, cmap='gray', vmin=0, vmax=255)
plt.show()
if __name__ == "__main__":
main()