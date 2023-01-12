#Libreria para calcular la complejidad
import big_o

def dato():
    """
    Funcion que permite ingresar los datos a nuestro arreglo

    Parametro
    -----------------------------------------------------------
    No tenemos ningun parametro

    Retorna
    -----------------------------------------------------------
    un dato:dato
    """
    while True:
        try:
            dato = int(input("Ingrese un Dato:\n"))
            if type(dato) == int:
                break
        except:
            print("No es un numero")
    return dato

def numDatos():
    """
    Funcion que permite devolver el numero de datos deseados

    Parametros
    ------------------------------------------------------------
    No necesita parametros

    Retorna
    ------------------------------------------------------------
    Numero de datos:numDat
    """
    #validacion de que sea un numero
    while True:
        #manejo de errores
        try:
            numDat = int(input("Ingrese el numero de  datos:\n"))
            if numDat>=0:
                break
        except:
            print("No es un numero")

    return numDat

def ingresoDatos(numDatos):
    """
    Funcion que  permite ingresar datos deseados por el usuario

    Parametro
    -------------------------------------------------------------------
    El numero de datos: numDatos

    Retorna
    ------------------------------------------------------------------
    un Arreglo de datos: datos
    """
    #arreglo de datos
    datos=[]
    #dato
    dat=0
    #recorrido desde 0 hasta en num datos
    for i in range(0,numDat):
        #ingreso de datos
        dat=dato()
        #agregamos al arreglo datos el dato
        datos.append(dat)
    #retornamos datos
    return datos

def noSeRepiteF(arreglo):
    """
    Funcion para buscar el elemento que no se repite

    Parametros
    -------------------------------------------------
    una Cadena: cadena

    Retorna
    ------------------------------------------------
    retorna un caracter no repetido: noSeRepite
    """
    noSeRepite=""
    #recorremos nuestra cadena
    for i in range(0,len(arreglo)):
        #Buscamos las veces que un elemento se repite con la funcion del los strings si es 1 para el for 
        if arreglo.count(arreglo[i])==1:
            #gurdamos la letra
             noSeRepite = arreglo[i]
             break
    #devolvemos el numero que no se repite
    return noSeRepite

if __name__ == "__main__":
    # declaracion de variables
    datos=[]
    numDat=0
    #ingreso de numero de datos que tendra el arreglo
    numDat=numDatos()
    #ingreso de datos
    datos=ingresoDatos(numDat)
    #buscamos el numero que no se repite
    numNoRepetido=noSeRepiteF(datos)
    #funcion lambda 
    datoO=lambda a: datos
    #calculo de complejidad
    best, other = big_o.big_o(noSeRepiteF,datoO)
    #Mostramos cual es el primer numero no repetido
    print("El primer numero que no se repite es {} ".format(numNoRepetido))
    #Mostramos su complejidad
    print("Su complejidad algoritmica es {}".format(best))

    

