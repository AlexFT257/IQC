import cv2
import numpy as np
import glob
from dom import DOM

# inicializar DOM
iqa = DOM()

# ruta de las peores imágenes
path = r'D:\La nada dentro del todo\Codigos\Python\IQC\Worst'

# lista de imágenes
images = glob.glob(path + '/*.jpg')

# cantidad de imágenesz
n = len(images)

# inicializar vectores
sharpness = np.zeros(n)
mean_intensity = np.zeros(n)
std_intensity = np.zeros(n)
local_contrast = np.zeros(n)

# recorrer las imágenes
for i in range(n):
    # Cargar la imagen
    image = cv2.imread(images[i]) # 640x640
    # Convertir la imagen a escala de grises
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # calcular la nitidez de la imagen
    sharpness[i] = iqa.get_sharpness(image)

    # Promedio de intensidad
    mean_intensity[i] = np.mean(gray)

    # Desviación estándar de intensidad
    std_intensity[i] = np.std(gray)

    # Contraste local (utilizando el operador Laplaciano)
    laplacian = cv2.Laplacian(gray, cv2.CV_64F)
    local_contrast[i] = np.mean(np.abs(laplacian))

# mostrar los resultados
print('Sharpness:', cv2.sumElems(sharpness)[0] / n)
print('Mean intensity:', cv2.sumElems(mean_intensity)[0] / n)
print('Standard deviation of intensity:', cv2.sumElems(std_intensity)[0] / n)
print('Local contrast:', cv2.sumElems(local_contrast)[0] / n)

print("Max values:")
print('Sharpness:', np.max(sharpness))
print('Mean intensity:', np.max(mean_intensity))
print('Standard deviation of intensity:', np.max(std_intensity))
print('Local contrast:', np.max(local_contrast))
