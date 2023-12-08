import cv2
import numpy as np

# Carregue a imagem que você deseja processar
imagem_f = cv2.imread('text_gaps.png', 0)  # Substitua 'imagem_f.png' pelo caminho da sua imagem

# Defina o kernel para as operações de dilatação e abertura
kernel = np.ones((3, 3), np.uint8)

# 1. Dilatação para aumentar o tamanho do retângulo central
dilatacao = cv2.dilate(imagem_f, kernel, iterations=1)

# 2. Abertura para remover detalhes externos ao retângulo
abertura = cv2.morphologyEx(dilatacao, cv2.MORPH_OPEN, kernel)

# Exiba a imagem resultante
cv2.imshow('Dilatação + Abertura', abertura)
cv2.waitKey(0)
cv2.destroyAllWindows()