import cv2
import numpy as np
#A linha de codigo abaixo é utilizada pra recurso do google Colab
from google.colab.patches import cv2_imshow

# Carrega a imagem colorida
imagem_colorida = cv2.imread("working.jpg")

# Verifique se a imagem foi carregada corretamente
if imagem_colorida is None:
    print("Erro ao carregar a imagem!")
    exit()

print(imagem_colorida.shape)  # Print the shape to confirm dimensions

# Converte a imagem colorida para tons de cinza
imagem_gray = cv2.cvtColor(imagem_colorida, cv2.COLOR_BGR2GRAY)

# Aplica o algoritmo de binarização
limiar = 127
_, imagem_binaria = cv2.threshold(imagem_gray, limiar, 255, cv2.THRESH_BINARY)

# Exibe as imagens
cv2_imshow(imagem_colorida)
cv2_imshow(imagem_binaria)
