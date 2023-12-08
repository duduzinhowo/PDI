import cv2
import numpy as np

# Carregue a imagem que você deseja processar
imagem = cv2.imread('Imagem2.png', 0)  # Certifique-se de substituir 'sua_imagem.png' pelo caminho da sua imagem

# Defina o kernel
kernel = np.array([[0, 1, 0],
                   [1, 1, 1],
                   [0, 1, 0]], dtype=np.uint8)

# Realize a operação de abertura
abertura = cv2.morphologyEx(imagem, cv2.MORPH_OPEN, kernel)

# Realize a operação de fechamento
fechamento = cv2.morphologyEx(imagem, cv2.MORPH_CLOSE, kernel)

# Exiba as imagens resultantes
cv2.imshow('Imagem Original', imagem)
cv2.imshow('Abertura', abertura)
cv2.imshow('Fechamento', fechamento)

cv2.waitKey(0)
cv2.destroyAllWindows()
