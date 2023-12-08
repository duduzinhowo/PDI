import cv2
import numpy as np

# Função para aplicar erosão e dilatação em uma imagem com um elemento estruturante específico
def apply_erosion_dilation(image, kernel):
    erosion = cv2.erode(image, kernel, iterations=1)
    dilation = cv2.dilate(image, kernel, iterations=1)
    return erosion, dilation

# Carregar a imagem 'fingerprint.tif'
image = cv2.imread('fingerprint.tif', cv2.IMREAD_GRAYSCALE)

# Verificar se a imagem foi carregada com sucesso
if image is None:
    print("Erro ao carregar a imagem. Verifique o caminho do arquivo.")
else:
    # Definir manualmente um elemento estruturante 3x3
    kernel = np.array([[0, 1, 0],
                       [1, 1, 1],
                       [0, 1, 0],
], dtype=np.uint8)
    # Aplicar erosão e dilatação à imagem com o elemento estruturante especificado
    eroded, dilated = apply_erosion_dilation(image, kernel)

    # Salvar as imagens resultantes ('fingerprint_eroded.tif' e 'fingerprint_dilated.tif')
    cv2.imwrite('fingerprinterosao1.tif', eroded)
    cv2.imwrite('fingerprintdilatacao1.tif', dilated)

    # Mostrar as imagens resultantes (opcional)
    cv2.imshow('Erosion', eroded)
    cv2.imshow('Dilation', dilated)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
