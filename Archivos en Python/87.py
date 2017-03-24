def crearArchivo():
    archivo=open('datos.txt','w')
    archivo.close()

def escribirArchivo():
    archivo=open('datos.txt','a')
    archivo.write('Víctor Manuel\n')
    archivo.write('664561250')
    archivo.close()

def leerArchivo():
    archivo=open('datos.txt','r')
    linea=archivo.readline()
    while linea!="":
        print (linea)
        linea=archivo.readline()
    archivo.close()

leerArchivo()