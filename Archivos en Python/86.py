def crearArchivo():
    archivo=open('datos.txt','w')
    archivo.close()

def escribirArchivo():
    archivo=open('datos.txt','a')
    archivo.write('Víctor Manuel\n')
    archivo.write('664561250')
    archivo.close()

escribirArchivo()