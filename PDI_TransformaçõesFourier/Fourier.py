import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft2, ifft2, fftshift
from PIL import Image


# Insira o caminho da sua própria imagem
imagem_caminho = 'LEN_PERIODIC_NOISE.png'


# Carregar sua própria imagem
imagem = Image.open(imagem_caminho)
imagem = imagem.convert('L')  # Converter para escala de cinza, se necessário


# Converter a imagem em uma matriz NumPy
image = np.array(imagem)


# Calcula a Transformada de Fourier 2D
fourier_transform = fft2(image)


# Calcula a Transformada Inversa de Fourier
inverse_fourier_transform = ifft2(fourier_transform)


# Calcula o espectro e a fase
spectrum = np.abs(fftshift(fourier_transform))
phase = np.angle(fftshift(fourier_transform))


# Plotar a imagem original
plt.figure(figsize=(12, 5))
plt.subplot(231)
plt.title("Imagem Original")
plt.imshow(image, cmap='gray')


# Plotar o espectro em 2D
plt.subplot(232)
plt.title("Espectro 2D")
plt.imshow(np.log(spectrum + 1), cmap='gray')


# Plotar a fase
plt.subplot(233)
plt.title("Fase")
plt.imshow(phase, cmap='gray')


# Plotar a Transformada Inversa de Fourier
plt.subplot(234)
plt.title("Transformada Inversa de Fourier")
plt.imshow(np.real(inverse_fourier_transform), cmap='gray')


# Plotar o espectro em 3D
plt.figure(figsize=(8, 6))
ax = plt.axes(projection='3d')
ax.set_title("Espectro 3D")
x = np.linspace(-spectrum.shape[1] // 2, spectrum.shape[1] // 2 - 1, spectrum.shape[1])
y = np.linspace(-spectrum.shape[0] // 2, spectrum.shape[0] // 2 - 1, spectrum.shape[0])
X, Y = np.meshgrid(x, y)
ax.plot_surface(X, Y, np.log(spectrum + 1), cmap='viridis')
plt.show()