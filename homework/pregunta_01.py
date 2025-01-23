# pylint: disable=import-outside-toplevel
# pylint: disable=line-too-long
# flake8: noqa
"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""
import pandas as pd
import os
import zipfile

def pregunta_01():
    """
    La información requerida para este laboratio esta almacenada en el
    archivo "files/input.zip" ubicado en la carpeta raíz.
    Descomprima este archivo.

    Como resultado se creara la carpeta "input" en la raiz del
    repositorio, la cual contiene la siguiente estructura de archivos:


    ```
    train/
        negative/
            0000.txt
            0001.txt
            ...
        positive/
            0000.txt
            0001.txt
            ...
        neutral/
            0000.txt
            0001.txt
            ...
    test/
        negative/
            0000.txt
            0001.txt
            ...
        positive/
            0000.txt
            0001.txt
            ...
        neutral/
            0000.txt
            0001.txt
            ...
    ```

    A partir de esta informacion escriba el código que permita generar
    dos archivos llamados "train_dataset.csv" y "test_dataset.csv". Estos
    archivos deben estar ubicados en la carpeta "output" ubicada en la raiz
    del repositorio.

    Estos archivos deben tener la siguiente estructura:

    * phrase: Texto de la frase. hay una frase por cada archivo de texto.
    * sentiment: Sentimiento de la frase. Puede ser "positive", "negative"
      o "neutral". Este corresponde al nombre del directorio donde se
      encuentra ubicado el archivo.

    Cada archivo tendria una estructura similar a la siguiente:

    ```
    |    | phrase                                                                                                                                                                 | target   |
    |---:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
    |  0 | Cardona slowed her vehicle , turned around and returned to the intersection , where she called 911                                                                     | neutral  |
    |  1 | Market data and analytics are derived from primary and secondary research                                                                                              | neutral  |
    |  2 | Exel is headquartered in Mantyharju in Finland                                                                                                                         | neutral  |
    |  3 | Both operating profit and net sales for the three-month period increased , respectively from EUR16 .0 m and EUR139m , as compared to the corresponding quarter in 2006 | positive |
    |  4 | Tampere Science Parks is a Finnish company that owns , leases and builds office properties and it specialises in facilities for technology-oriented businesses         | neutral  |
    ```


    """
     # Ruta del archivo y descomprimir
    archivo_zip = 'files/input.zip'
    carpeta_extraccion = '.' 

    # Crear carpeta de extracción si no existe
    if not os.path.exists(carpeta_extraccion):
        os.makedirs(carpeta_extraccion)

    # Descomprimir el archivo zip
    with zipfile.ZipFile(archivo_zip, 'r') as archivo:
        archivo.extractall(carpeta_extraccion)

    carpeta_datos = 'input' 

    # Función para leer archivos y etiquetar
    def cargar_datos(directorio):
        registros = []
        # Recorrer las carpetas de sentimientos
        for etiqueta in ['negative', 'positive', 'neutral']:
            carpeta_etiqueta = os.path.join(directorio, etiqueta)
            for archivo_nombre in os.listdir(carpeta_etiqueta):
                ruta_archivo = os.path.join(carpeta_etiqueta, archivo_nombre)
                with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
                    contenido = archivo.read().strip()
                    registros.append({'phrase': contenido, 'target': etiqueta})
        return registros

    # Cargar los datos de entrenamiento y prueba
    datos_entrenamiento = cargar_datos(os.path.join(carpeta_datos, 'train'))
    datos_prueba = cargar_datos(os.path.join(carpeta_datos, 'test'))

    # Convertir los datos en DataFrames
    df_entrenamiento = pd.DataFrame(datos_entrenamiento)
    df_prueba = pd.DataFrame(datos_prueba)

    # Crear carpeta de salida si no existe
    carpeta_salida = 'files/output/'
    if not os.path.exists(carpeta_salida):
        os.makedirs(carpeta_salida)

    # Guardar los DataFrames en archivos CSV
    df_entrenamiento.to_csv(os.path.join(carpeta_salida, 'train_dataset.csv'), index=False)
    df_prueba.to_csv(os.path.join(carpeta_salida, 'test_dataset.csv'), index=False)


