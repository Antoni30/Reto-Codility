#Libreria para calcular la complejidad
import big_o

def ingresar():
    """
    Funcion que permite el ingreso de datos de usuario

    Parametro
    -----------------------------------------------------
    Ningun Parametro

    Retorna
    ---------------------------------------------------------
    numero postivo : N
    """
    while True:
        #manejo de errorres
        try:
            #Ingreso de datos pos usuario
            N=int(input("Ingreso un entero positivo:\n"))
            #validacion para que N sea un entero positivo
            if N>0:
                #el bucle para
                break
            else:
                #informa que el numero no es mayor
                print("El dato no es un numero positivo")
        except:
            print("El dato ingresado no es un numero ")
    return N
        
def solucion(N):
    """
    Funcion que permite encontrar el maximo exponente

    Parametro
    -----------------------------------------------------------
    Numero entero positivo:N

    Retorna
    -----------------------------------------------------------
    el valor del  maximo exponente:k
    """
    #declaracion de k
    k=0
    #mientras no se cumpla la condicion de salida repetimos
    while True:
        #si la resta del numero es par hacer
        if (N/(2**k))%2==0:
            #Incrementamos mi exponente
            k+=1
        else:
            break
    #retornamos el exponente
    return k

if __name__=="__main__":
    #declaramos variables
    N=0
    k=0
    #Ingreso de datos
    N=ingresar()
    #funcion de Lambda
    Nlamnda= lambda n: N
    #calculo de complejidad
    best, other = big_o.big_o(solucion,Nlamnda)
    #el exponente mayor
    k=solucion(N)
    #mostramos el exponente
    print("El mayor exponente es {}".format(k))
    #mostramos la complejidad
    print("Su complejidad es {}".format(best))

