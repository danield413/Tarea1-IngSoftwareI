from buscador.Carpeta import Carpeta

def main():
    
    #* PRUEBAS

    #* prueba 1
    carpeta = Carpeta('./pruebas')
    print(carpeta.buscar('arar'))

    print('-------------------------------------------------------------------')

    #* prueba 2
    carpeta2 = Carpeta('./pruebas2')
    print(carpeta2.buscar('foto'))

    print('-------------------------------------------------------------------')

    #* prueba 3
    carpeta3 = Carpeta('./pruebas3')
    print(carpeta3.buscar('ejemplo'))

if __name__ == "__main__":
    main()

