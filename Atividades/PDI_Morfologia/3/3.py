import cv2
import numpy as np

# Carregue a imagem que você deseja processar
imagem_f = cv2.imread('noise_rectangle.png', 0)  # Substitua 'imagem_f.png' pelo caminho da sua imagem

# 1. Binarização da imagem
_, binarizada = cv2.threshold(imagem_f, 200, 255, cv2.THRESH_BINARY)

# 2. Identificação dos contornos
contornos, _ = cv2.findContours(binarizada, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# 3. Encontre o maior contorno (o retângulo branco) e recorte-o
maior_contorno = max(contornos, key=cv2.contourArea)
x, y, w, h = cv2.boundingRect(maior_contorno)
retangulo_branco = imagem_f[y:y + h, x:x + w]

# Exiba o retângulo branco
cv2.imshow('Retângulo Branco', retangulo_branco)
cv2.waitKey(0)
cv2.destroyAllWindows()
