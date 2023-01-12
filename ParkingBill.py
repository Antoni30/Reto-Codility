#libreria para calcular la complejidad
import big_o
def calcularMulta(horasPrograma):
    """
    Funcion que calcula el costo de uso del parqueadero
   
    Parametro
    --------------------------------------------------
    horas ingresadas por el usuario : horasPrograma

    Retorna
    --------------------------------------------------
    el calculo el costo: cost
    """
    #sacamos los valores necesarios para el programa
    [entrada,salida]=horasPrograma
    #hacemos un split para divir hora y minutos
    arregloHoraE=entrada.split(':')
    arregloHoraS=salida.split(':')
    #transformaos a un entero tantos horas como los minutos
    horaE=int(arregloHoraE[0])
    minutosE=int(arregloHoraE[1])
    horaS=int(arregloHoraS[0])
    minutosS=int(arregloHoraS[1])
    #calculamos las horas que se estuvo en el parqueadero
    hora=horaS-horaE
    #si el minuto de salida el mayor o igual a minutos de entrada hacer
    if minutosS >= minutosE: 
        #restamos los minutos
        minutos = minutosS - minutosE
    else:
        #si minutos de salida es mayor que la entra resto 1 horas 
        hora -= 1
    if hora>0:
        cost=2+3+(hora-1)*4
    else:
        cost=0
    return cost

if __name__ == "__main__":
    # declaracion de variables
    horas=[]
    #ingreso de datos de Entrada por el usuario
    entrada = input("Ingrese la hora de entrada en el formato HH:MM:\n")
    #ingreso de datos de Salida por el usuario
    salida = input("Ingrese la hora de salida en el formato HH:MM:\n")
    #agregamos al arreglo Hora  la entrada al parkin
    horas.append(entrada)
    #agregamos al arreglo Hora  de salida al parkin
    horas.append(salida)
    #creacion de la funcion lamda
    datosL=lambda dat:horas
    #calculo de complejidad
    best, other=big_o.big_o(calcularMulta,datosL)
    #calculamos el costo
    costo=calcularMulta(horas)
    print("El costo es {}".format(costo))
    print("La complejidad es {}".format(best))