import cv2
import numpy as np
# Inicialize o objeto do vídeo a partir de um arquivo de vídeo ou uma câmera
video = cv2.VideoCapture('output.avi') # Substitua 'seu_video.mp4' pelo caminho do seu vídeo
# Inicialize o objeto para o modelo de fundo
background_subtractor = cv2.createBackgroundSubtractorMOG2()
while True:
# Leia o próximo frame do vídeo
    ret, frame = video.read()
    if not ret:
    break # Encerra o loop quando o vídeo terminar
# Aplique a subtração de fundo no frame atual
foreground_mask = background_subtractor.apply(frame)
# Aplique uma operação de limiarização para destacar as áreas de movimento
_, thresh = cv2.threshold(foreground_mask, 128, 255, cv2.THRESH_BINARY)
# Encontre os contornos das áreas destacadas
contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
# Desenhe retângulos ao redor das áreas de movimento no frame original
for contour in contours:
if cv2.contourArea(contour) > 200: # Ajuste o valor do limiar conforme necessário
x, y, w, h = cv2.boundingRect(contour)
cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
# Exiba o frame com as áreas de movimento destacadas
cv2.imshow('Detecção de Movimento', frame)
# Encerra o loop quando a tecla 'q' for pressionada
if cv2.waitKey(20) & 0xFF == ord('q'):
break
# Libere o objeto de vídeo e feche a janela
video.release()
cv2.destroyAllWindows()