import numpy as np
import cv2
import matplotlib.pyplot as plt

#Calcular e exibir o espectro de Fourier para amplitudes
def plot_amplitude_spectrum(image):
    fft_image = np.fft.fft2(image)
    amplitude_spectrum = np.abs(fft_image)
    plt.imshow(np.log1p(amplitude_spectrum), cmap='gray')
    plt.title('Espectro de Fourier (Amplitudes)')
    plt.colorbar()
    plt.show()

#Calcular e exibir o espectro de Fourier para fases
def plot_phase_spectrum(image):
    fft_image = np.fft.fft2(image)
    phase_spectrum = np.angle(fft_image)
    plt.imshow(phase_spectrum, cmap='gray')
    plt.title('Espectro de Fourier (Fases)')
    plt.colorbar()
    plt.show()

#Calcular e exibir o espectro de Fourier centralizado
def plot_shifted_amplitude_spectrum(image):
    fft_image = np.fft.fft2(image)
    fft_shifted = np.fft.fftshift(fft_image)
    amplitude_spectrum_shifted = np.abs(fft_shifted)
    plt.imshow(np.log1p(amplitude_spectrum_shifted), cmap='gray')
    plt.title('Espectro de Fourier Centralizado (Amplitudes)')
    plt.colorbar()
    plt.show()

#Criar um quadrado branco sobre fundo preto
image = np.zeros((512, 512), dtype=np.uint8)
cv2.rectangle(image, (100, 100), (412, 412), 255, -1)
plt.imshow(image, cmap='gray')
plt.title('Imagem Original')
plt.show()

#Espectro de Fourier para amplitudes
plot_amplitude_spectrum(image)

#Calcular e visualizar o espectro de Fourier para fases
plot_phase_spectrum(image)

#Obter e visualizar o espectro de Fourier centralizado
plot_shifted_amplitude_spectrum(image)

#Aplicar uma rotação de 40º no quadrado
angle = 40
rotated_image = cv2.warpAffine(image, cv2.getRotationMatrix2D((256,
256), angle, 1), (512, 512))
plt.imshow(rotated_image, cmap='gray')
plt.title('Imagem Rotacionada')
plt.show()
plot_amplitude_spectrum(rotated_image)
plot_phase_spectrum(rotated_image)
plot_shifted_amplitude_spectrum(rotated_image)

#Aplicar uma translação nos eixos x e y no quadrado
translation_x = 50
translation_y = 30
translated_image = np.roll(image, (translation_x, translation_y),
axis=(1, 0))
plt.imshow(translated_image, cmap='gray')
plt.title('Imagem Transladada')
plt.show()
plot_amplitude_spectrum(translated_image)
plot_phase_spectrum(translated_image)
plot_shifted_amplitude_spectrum(translated_image)

#Aplicar zoom na imagem
zoomed_image = cv2.resize(image, (256, 256))
plt.imshow(zoomed_image, cmap='gray')
plt.title('Imagem Ampliada/Reduzida')
plt.show()
plot_amplitude_spectrum(zoomed_image)
plot_phase_spectrum(zoomed_image)
plot_shifted_amplitude_spectrum(zoomed_image)
