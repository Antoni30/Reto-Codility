#Libreria para calcular la complejidad
import big_o
def ingresarCadena():
    """
    Funcion que permite ingresar una cadena

    Parametro
    -------------------------------------------
    nigun parametro

    Retorna
    -------------------------------------------
    una cadena:cadena o -1
    """
    #ingreso de una cadena
    cadena=input("Ingrese una cadena:\n")
    #comrpobamos si la cadena tiene un index de retorno 
    if len(cadena)%2==0:
        #si no lo tiene retornamos un -1
        return -1
    #retornamos la cadena
    return cadena
def solucion(cadena):
    """
    Funcion que permite encontrar el index de donde el reversible la cadena

    Parametro
    --------------------------------------------------------------------------
    necesitamos la cadena:cadena

    Retorna
    --------------------------------------------------------------------------
    Index desde donde la cadena es reversible
    """
    #comprobamos que no sea un -1
    if cadena!=-1:
        #declaramos el index a regresar
        index=0
        #pocision final 
        atras=len(cadena)-1
        #contados de letras repetidas
        cont=0
        #recorremos la cadena
        for i in range(0,len(cadena)):
            #si cumple que la posicion final  y  la inicial son iguales contamos 
            if cadena[i]==cadena[atras-i] and (atras-i)>i:
                #contador en aumento
                cont+=1
        #si el contados es el mismo significa que son iguales de ambos lados
        if cont==((len(cadena)-1))/2:
            #index deseado
            index=(((len(cadena)-1))/2)
            #retornamos el index
            return index
        #caso contrario retornamos un -1
        else:
            return -1
    #caso contrario retornamos el mismo -1
    else:
        return -1


if __name__ =="__main__":
    #declaramos las variables
    cadena=""
    #ingreso de cadena
    cadena=ingresarCadena()
    #creamos  nuestra funcion lambda
    cadenaL=lambda l:cadena
    #calculo de complejidad
    best, other=big_o.big_o(solucion,cadenaL)
    #index deseado
    index=int(solucion(cadena))
    #mostramos el index
    print("El index es {}".format(index))
    #mostramos su complejidad
    print("Su complejidad algoritmica es {}".format(best))

