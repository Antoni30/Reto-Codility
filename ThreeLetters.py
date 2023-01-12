#libreria para calcular la complejidad
import big_o
def ingreso():
    """
    Funcion que permite ingresar los valore deseados

    Parametros
    ----------------------------------------------------------
    ningun parametro

    Retorno
    ----------------------------------------------------------
    Variables A y B: A and B
    """
    # Validacion
    while True:
        #
        try:
            varA = int(input("Ingrese el numero de A que posee la cadena:\n"))
            varB = int(input("Ingreso el numero de B que posee la cadena:\n"))
            if varA > 0 and varB > 0:
                break
            else:
                print("Alguno de los datos es menor a 0")
        except:
            print("No es un numero alguna de los valores ingresados")
    # retorno de valores
    return varA, varB
def solucion(datos):
  """
  Funcion que devuelve la solucion del problema 

  Parametros
  -----------------------------------------------------------
  un arreglo con los datos

  Retorna 
  -----------------------------------------------------------
  Una cadena: cadenaSolucion
  """
  #declaramos los datos por separado
  [A,B]=datos
  #declaramos la cadena
  cadenaSolucion = ""
  #tamanio de cadena
  tamanio=A+B
  #compramos la condicon que A es > a B
  if A>B:
    #mientras exista numero de A y numero de B seguir haciendo
    while A > 0 or B > 0:
      #Si A > 0 y B > 0 hacemos
      if A > 0 and B > 0:
        #Si la cadena no es tiene dos letras seguidas agregar 
        if cadenaSolucion[-2:] != "aa":
          #Agregamos a la cadena
          cadenaSolucion += "a"
          #restamos el numero de A
          A -= 1
        else:
          #Agregamos a la cadena
          cadenaSolucion += "b"
          #restamos el numero de B
          B -= 1
      elif A > 0:
        #Agregamos a la cadena
        cadenaSolucion += "a"
        #restamos el numero de A
        A -= 1
      elif B > 0:
        #Agregamos a la cadena
        cadenaSolucion += "b"
        #restamos el numero de B
        B -= 1
  #condicion que se A es igual a B
  elif A==B:
    #recorremos hast que se cumpla el tamanio de la cadena
    for i in range(0,tamanio):
      #Comrprobamos si la pos es par o impar
      if i%2==0:
        #Agregamos a la cadena
        cadenaSolucion+='a'
      else:
        #Agregamos a la cadena
        cadenaSolucion+='b'
  #comprobamos si A es < que B
  elif A<B:
    #mientras exista numero de A y numero de B seguir haciendo
     while A > 0 or B > 0:
       #Si A > 0 y B > 0 hacemos
      if A > 0 and B > 0:
        #Si la cadena no es tiene dos letras seguidas agregar 
        if cadenaSolucion[-2:] != "bb":
          #Agregamos a la cadena
          cadenaSolucion += "b"
          B -= 1
        else:
          #Agregamos a la cadena
          cadenaSolucion += "a"
          A-= 1
      elif B > 0:
        #Agregamos a la cadena
        cadenaSolucion += "b"
        B-= 1
      elif A > 0:
        #Agregamos a la cadena
        cadenaSolucion += "a"
        A-= 1
  
  return cadenaSolucion


if __name__ == "__main__":
    # declaracion de variables
    varA = 0
    varB = 0
    datos=[]
    # ingreso de datos por el usuario
    [varA, varB] = ingreso()
    datos.append(varA)
    datos.append(varB)
    #calculo de complejidad
    dat = lambda a: datos
    best,other=big_o.big_o(solucion,dat)
    print("La cadena resultante es: {}".format(solucion(datos)))
    print("La complejidad es {}".format(best))
