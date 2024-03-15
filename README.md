# Image Quality Checker

Image Quality Checker (IQC) es un script diseñado para verificar la calidad de las imágenes generadas por el proceso de aumento de datos. Su objetivo es garantizar que las imágenes generadas mantengan una calidad adecuada para no afectar el rendimiento del modelo.

El script se compone de dos partes:
- `GetBaseline.py`: Script para obtener el valor del umbral de calidad.
- `IQC.py`: Script para verificar la calidad de las imágenes.

**Nota:** El umbral obtenido con el script `GetBaseline.py` es un valor de referencia. Se recomienda revisar el reporte de calidad y ajustar el umbral si es necesario, para evitar falsos positivos.

## Modo de uso

1. Instalar las dependencias necesarias:
```bash
pip install -r requirements.txt
```
2. Seleccionar al menos las 10 peores imágenes generadas por el proceso de aumento de datos y copiarlas en una carpeta.
3. Abrir el script `GetBaseline.py` y modificar la variable `path` con la ruta de la carpeta que contiene las peores imágenes.
4. Correr el script `GetBaseline.py` para obtener el valor del umbral.
5. Abrir el script `IQC.py` y modificar la variable `path` con la ruta de la carpeta que contiene las imágenes del dataset y las variables de umbral obtenidas en el paso anterior.
6. Correr el script `IQC.py` para obtener el reporte de calidad de las imágenes.
7. Revisar el reporte y ajustar el umbral si es necesario.

## Reporte de calidad

El reporte de calidad es un .txt que se compone de dos partes:
- El path de las imágenes que no cumplen con el umbral de calidad.
- Los umbrales específicos que no se cumplieron.

## Recomenaciones

- Se recomienda eliminar la comprobación de contraste local si las imágenes generadas son en blanco y negro.
- Se recomienda modificar disminuir el umbral de nitidez si las fotos tienen blur en el fondo.

## Agradecimientos

El script hace uso del codigo de [Pydom](https://github.com/umang-singhal/pydom) para la estimacion de la nitidez.

