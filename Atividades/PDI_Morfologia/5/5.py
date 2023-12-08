import cv2
import numpy as np

# Carregue a imagem que você deseja processar
imagem = cv2.imread('rosto_perfil.png', 0)  # Substitua 'sua_imagem.png' pelo caminho da sua imagem

# 1. Binarização da imagem
_, binarizada = cv2.threshold(imagem, 200, 255, cv2.THRESH_BINARY)

# 2. Erosão para reduzir o objeto à borda
kernel = np.ones((3, 3), np.uint8)
contorno = cv2.erode(binarizada, kernel, iterations=1)

# 3. Subtração para obter apenas o contorno
contorno = cv2.subtract(binarizada, contorno)

# Exiba o contorno
cv2.imshow('Contorno da Imagem', contorno)
cv2.waitKey(0)
cv2.destroyAllWindows()
