
from buscador.Archivo import Archivo
import re 
class JSON(Archivo):
    
    def __init__(self, ruta: str, nombre: str):
        super().__init__(ruta, nombre)
   
    # Metodo para buscar una palabra en un archivo JSON
    # parametro palabra: palabra a buscar
    def buscarPalabra(self, palabra: str) -> int:
        texto = self._leerArchivo()
        texto = texto.replace(',', ' ')
        texto = texto.replace('"', '')
        texto = texto.replace('\n', ' ')
        texto = texto.replace('{', ' ')
        texto = texto.replace('}', ' ')
        texto = texto.replace(':', ' ')
        texto = texto.replace('[', ' ')
        texto = texto.replace(']', ' ')
        # Se usa una expresion regular para buscar la palabra en el texto base
        ocurrencias = re.findall(r'\b' + re.escape(palabra) + r'\b', texto)
        return len(ocurrencias)
   