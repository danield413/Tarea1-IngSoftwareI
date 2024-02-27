
from buscador.Archivo import Archivo
import re

class TXT(Archivo):
    
    def __init__(self, ruta: str, nombre: str):
        super().__init__(ruta, nombre)

    #Metodo para buscar una palabra en un archivo de texto
    # parametro palabra: palabra a buscar
    def buscarPalabra(self, palabra: str) -> int:
        texto = self._leerArchivo()
        # Se usa una expresion regular para buscar la palabra en el texto base
        ocurrencias = re.findall(r'\b' + re.escape(palabra) + r'\b', texto)
        return len(ocurrencias)
   