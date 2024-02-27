import os
from buscador.TXT import TXT
from buscador.CSV import CSV
from buscador.JSON import JSON
from buscador.XML import XML

class Carpeta:

    '''
    Clase que representa una carpeta en el sistema de archivos.
    Atributos:
    - ruta: string
    - archivos: list
    '''

    def __init__(self, ruta: str):
        self.ruta = ruta
        self.archivos = []

    #* Método que me permite buscar los archivos existentes en la ruta de la carpeta y si cumplen con el formato los agrega a la lista
    def __obtenerArchivos(self) -> None:
        archivos = []
        try:
            archivos = os.listdir(self.ruta)
            if len(archivos) == 0:
                print(f"No hay archivos de texto en la carpeta {self.ruta}")
                return
            
            for nombreArchivo in archivos:
                extension = nombreArchivo.split('.')[-1]

                if extension == 'txt':
                    file = TXT(self.ruta, nombreArchivo)
                    self.archivos.append(file)
                
                elif extension == 'csv':
                    file = CSV(self.ruta, nombreArchivo)
                    self.archivos.append(file)

                elif extension == 'json':
                    file = JSON(self.ruta, nombreArchivo)
                    self.archivos.append(file)

                elif extension == 'xml':
                    file = XML(self.ruta, nombreArchivo)
                    self.archivos.append(file)
                else:
                    print(f"El archivo {nombreArchivo} no es un archivo de texto, csv, json o xml")
        
        except OSError as e:
            print(f"No se pudo acceder a la ruta {self.ruta}, no se encuentra.")
            exit()
        return archivos

    ''' Método que me permite buscar una palabra en los archivos de la carpeta 
        params:
            - palabra: string
    '''
    def buscar(self, palabra):
        self.__obtenerArchivos()

        if len(self.archivos) == 0:
            return f"No hay archivos en la carpeta {self.ruta}"

        resultados = 0
        for archivo in self.archivos:
            resultado = archivo.buscarPalabra(palabra)
            print(f"- Archivo {archivo.nombre}: se encontró '{palabra}' {resultado} veces")
            resultados += resultado

        return f"- La palabra {palabra} se encontró {resultados} veces en la carpeta {self.ruta}"
    def __str__(self):
        return f'Carpeta: {self.ruta}'
