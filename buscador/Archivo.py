from abc import ABC, abstractmethod

class Archivo(ABC):

    '''
        Clase abstracta que me representa un archivo del cual heredan sus tipos
    '''

    def __init__(self, ruta: str, nombre: str):
        self.nombre = nombre
        self.ruta = ruta

    #* Método que me lee el archivo y me devuelve su contenido
    def _leerArchivo(self) -> str:
        with open(f'{self.ruta}/{self.nombre}', 'r') as archivo:
            return archivo.read()

    def __str__(self) -> str:
        return f'Archivo: {self.ruta}/{self.nombre}'