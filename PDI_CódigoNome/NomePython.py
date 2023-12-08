import numpy as np
import matplotlib.pyplot as plt

colunas = 30
linhas = 15
image_matrix = np.zeros([linhas, colunas])
print(image_matrix.shape)

image_matrix[5,10:13] = 120
image_matrix[5:9,11] = 120
image_matrix[9:10,10] = 120
image_matrix[8,9] = 120

image_matrix[5,15:18] = 120
image_matrix[7,15:18] = 120
image_matrix[9,15:18] = 120
image_matrix[5:9,15] = 120

image_matrix[5,21:23] = 120
image_matrix[6:7,20] = 120
image_matrix[7,21] = 120
image_matrix[8,22] = 120
image_matrix[9,20:22] = 120

image_matrix[5:10,25] = 120
image_matrix[5,25:28] = 120
image_matrix[7,25:28] = 120



plt.imshow(image_matrix, cmap='gray')
plt.show()