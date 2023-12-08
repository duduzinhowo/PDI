import cv2
import numpy as np
import matplotlib.pyplot as plt
# Carregue a imagem da placa sem defeito e a imagem da placa com defeito
placa_sem_defeito = cv2.imread('pcb.png', cv2.IMREAD_GRAYSCALE)
placa_com_defeito = cv2.imread('pcb2.png', cv2.IMREAD_GRAYSCALE)
# Verifique se as imagens têm o mesmo tamanho
if placa_sem_defeito.shape == placa_com_defeito.shape:
# Subtrai as duas imagens para encontrar defeitos
    diferenca = cv2.absdiff(placa_sem_defeito, placa_com_defeito)
# Aplique um limiar para destacar os defeitos
limite = 30
_, imagem_limiarizada = cv2.threshold(diferenca, limite, 255,
cv2.THRESH_BINARY)
# Encontre os contornos dos defeitos na imagem limiarizada
contornos, _ = cv2.findContours(imagem_limiarizada, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
# Crie uma cópia colorida da placa com defeito para destacar os defeitos em vermelho 
placa_com_defeito_colorida = cv2.cvtColor(placa_com_defeito, cv2.COLOR_GRAY2BGR)
# Desenhe os contornos dos defeitos na cópia colorida
cv2.drawContours(placa_com_defeito_colorida, contornos, -1, (0, 0, 255), 2)
# Exiba as imagens original, diferença e placa com defeito destacando os defeitos
plt.figure(figsize=(12, 4))
plt.subplot(131)
plt.title("Placa Sem Defeito")
plt.imshow(placa_sem_defeito, cmap='gray')
plt.subplot(132)
plt.title("Diferença")
plt.imshow(imagem_limiarizada, cmap='gray')
plt.subplot(133)
plt.title("Placa com Defeito (Destacando Defeitos)")
plt.imshow(cv2.cvtColor(placa_com_defeito_colorida,
cv2.COLOR_BGR2RGB))
plt.show()
else:
print("As imagens têm tamanhos diferentes. Verifique suas imagens.")
