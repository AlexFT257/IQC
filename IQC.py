import cv2
import numpy as np
from dom import DOM
import glob
import time
import shutil
import multiprocessing

# Función para procesar una lista de imágenes y escribir los resultados en un archivo
def process_images(images, output_file, sharpness_threshold, mean_intensity_threshold, std_intensity_threshold, local_contrast_threshold):
    # Iterar sobre cada imagen
    for image_path in images:
        # Cargar la imagen
        image = cv2.imread(image_path)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Inicializar DOM
        iqa = DOM()

        # Calcular la nitidez de la imagen
        sharpness = iqa.get_sharpness(image)

        # Promedio de intensidad
        mean_intensity = np.mean(gray)

        # Desviación estándar de intensidad
        std_intensity = np.std(gray)

        # Contraste local (utilizando el operador Laplaciano)
        laplacian = cv2.Laplacian(gray, cv2.CV_64F)
        local_contrast = np.mean(np.abs(laplacian))

        # Escribir los resultados en el archivo de salida si no cumple con los umbrales
        with open(output_file, 'a') as f:
            txt = image_path + '\n'
            if sharpness < sharpness_threshold:
                txt += 'Sharpness: ' + str(sharpness) + ' < ' + str(sharpness_threshold) + '\n'
            if mean_intensity < mean_intensity_threshold:
                txt += 'Mean intensity: ' + str(mean_intensity) + ' < ' + str(mean_intensity_threshold) + '\n'
            if mean_intensity < mean_intensity_threshold and std_intensity < std_intensity_threshold:
                txt += 'Standard deviation of intensity: ' + str(std_intensity) + ' < ' + str(std_intensity_threshold) + '\n'
            if local_contrast < local_contrast_threshold:
                txt += 'Local contrast: ' + str(local_contrast) + ' < ' + str(local_contrast_threshold) + '\n'
            if txt.find('<') != -1:
                f.write(txt + '\n')
        
        print("Image", image_path, "done")

# Función para procesar imágenes en paralelo
def process_images_in_parallel(images, output_file, sharpness_threshold, mean_intensity_threshold, std_intensity_threshold, local_contrast_threshold, num_threads):
    # Calcular la cantidad de imágenes por hilo
    images_per_thread = len(images) // num_threads

    # Crear y ejecutar los hilos
    processes = []
    for i in range(num_threads):
        start_index = i * images_per_thread
        end_index = (i + 1) * images_per_thread if i < num_threads - 1 else len(images)
        thread_images = images[start_index:end_index]
        p = multiprocessing.Process(target=process_images, args=(thread_images, output_file, sharpness_threshold, mean_intensity_threshold, std_intensity_threshold, local_contrast_threshold))
        processes.append(p)
        p.start()

    # Esperar a que todos los hilos terminen
    for p in processes:
        p.join()

if __name__ == "__main__":
    # umbrales
    sharpness_threshold = 0.6484085101990841
    mean_intensity_threshold = 55.568566032858456
    std_intensity_threshold = 57.56940301615317
    local_contrast_threshold = 4.925640653722427

    # medir el tiempo de ejecución
    start = time.time()

    # ruta de las imágenes
    path = r'D:\La nada dentro del todo\Codigos\Python\IQC\Dataset\train\images'
    # ruta del archivo de salida para las imágenes que no cumplen con los umbrales
    output_file = "result.txt"

    # lista de imágenes
    images = glob.glob(path + '/*.jpg')

    # cantidad de hilos
    num_threads = multiprocessing.cpu_count()

    # procesar las imágenes en paralelo
    process_images_in_parallel(images, output_file, sharpness_threshold, mean_intensity_threshold, std_intensity_threshold, local_contrast_threshold, num_threads)

    # medir el tiempo de ejecución
    end = time.time()

    # mostrar el tiempo de ejecución
    print("Execution time:", end - start, "seconds")
