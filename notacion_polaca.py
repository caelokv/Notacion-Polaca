# DEFINNICIÓN DE FUNCIONES

def checar(caracter) : # Clasifica un carácter válido.

  if (caracter == "+" or 
      caracter == "-") : # Primer nivel de opradores.

    if caracter == "+" : # Suma
      tipo = "+"
      nivel = 1
      especial = 0

    else :
      tipo = "-" # Resta
      nivel = 1
      especial = 0

  elif (caracter == "*" or 
        caracter == "/") : # Tercer nivel de operadores.

    if caracter == "*" :
      tipo = "*" # Multiplicación
      nivel = 3
      especial = 1

    else :
      tipo = "/" # Divión
      nivel = 3
      especial = 0

  else :
    if (caracter == "(" or 
        caracter == ")") : # Lo que no es operador
      tipo = "()" # Paréntesis
      nivel = 4
      especial = 0

    elif caracter == " " :
      tipo = " " # Espacios
      nivel = 4
      especial = 0

    else :
      tipo = caracter # Números
      nivel = 0
      especial = 2

  return (tipo, nivel, especial) 
  # "tipo" tendrá el valor del carácter; 
  # "nivel" el nivel del operador; "especial" para los números y exponentes.
  # Niveles: 0 : Números; 1 : Suma y resta; 2 : Exponenciación;
  #         3 : Multiplicación y división; 4 : Paréntesis y espacios


def exponente(elementos) : # Junta los carácteres de un exponente.

  ecuacion = elementos[0] # La ecuación ingresada.
  iterador = elementos[1] # Dice la posición actual en la ecuación.

  # El primer y segundo carácter después de el actual :
  primero = checar(ecuacion[iterador + 1])
  segundo = checar(ecuacion[iterador + 2])

  if primero[0] == "*" : # Comprueba si ha dos ** juntos.

    if segundo[0] == " " : # Comprueba si el siguiente a ** es un espacio.
      tercero = checar(ecuacion[iterador + 3]) # El tercero siguiente.
      # Ordena los crácteres y le asigna su nivel:
      final = tercero[0] + "**"
      nivel = 2
      iterador = iterador + 3

    else : # Si no es seguido por un espacio,
      final = segundo[0] + "**" 
      # Ordena los crácteres y le asigna su nivel:
      nivel = 2
      iterador = iterador + 2

  else : # Si no encuentra un * después, no hará cambios.
    final = "*"
    nivel = 3

  return (final, nivel, iterador) 
  # Devuelve la expresión final, 
  # el nivel que del operador y el valor del iterdor "i".


def numero(elementos) : # Une los números de más de un dígito.

  ecuacion = elementos[0] # La ecuación ingresada.
  iterador = elementos[1] # Dice la posición actual en la ecuación.
  sigui = iterador +1 # La posición siguiente en la ecuación.

  actual = checar(ecuacion[iterador]) # Clasifica el carácter actual.
  num = actual[0] # Obtiene el caracter actual.

  w = 0 # Se usa para detener el while.

  # Mientras  el carácter siendo clasificado sea un número.
  while actual[2] == 2 and w == 0 :

    if sigui != len(ecuacion) : # Corrobora si hay más elementos después.
      iterador += 1 # Obtiene la calsificación del siguiente carácter.
      actual = checar(ecuacion[iterador])

      if actual[2] == 2 : # Si es un número:
        num = num + actual[0] # Añade al anterior el actual.

      else :
        num = num # Si no, lo deja como está.

    else :
      num = num # Si ya no hay más elementos después, no hace ningún cambio.
      w = 1

  iterador = iterador + 1

  return (num, iterador)
  # Devuelve el número obtenido, y la posición nueva en la ecuación.


def ordenar(tipo) : # Ordena en una lista los cracteres ya clasificados.

  caracter = tipo[0] # El carácter a ordenar y
  nivel = tipo[1]    # el nivel de este.  

  # Cuentan cuántos ya hay en la lista de:
  nu = tipo[2] # Suma y resta
  nd = tipo[3] # Exponenciación
  nt = tipo[4] # Multiplicación y división
  nm = tipo[5] # Números

  lista = tipo[6] # La lista a trabajar
  i = 0 # Iterador

  largo = len(lista) # Largo actual de la lista

  # Usa el nivel del carácter para ordenarlos.
  if nivel == 0 : # Números: -------

    if bool(lista) == False :
      # Si la lista está vacía, lo añade como primer elemento.
      lista.append(caracter) 
      nm += 1 # Actualiza el contador.

    else :
      # Si la lista no es vacía, retira los operadores.
      operet = [] # Guardará los operadores retirados.

      while i < largo - nu - nd - nt : # Retira los operadores.
        operet.append(lista.pop())
        i += 1

      lista.append(caracter) # Añade el carácter.
      lista = lista + operet # Devuelve los operadores a la lista.
      nm += 1 # Actualiza el contador.

  elif nivel == 1 : # Operadores + , - : -------

    if nd == 0 and nt == 0 :
      # Si no hay operadores de mayor jerarquía, se añade al final.
      lista.append(caracter)
      nu += 1 # Aumenta el contador

    else :
      # Si los hay, se sigue un proceso análogo al de los números.
      operet = []

      while i < largo - nd - nt :
        operet.append(lista.pop())
        i += 1

      lista.append(caracter)
      lista = lista + operet
      nu += 1

  else : # Para ordenar los caracteres restantes.

    if nivel == 2 : # Operador ** : -------

      if nt == 0 :
        # Si no hay operadores de mayor jerarquía se añade al final.
        lista.append(caracter)
        nd += 1 # Aumenta el contador

      else : 
        # Si los hay se sigue un proceso análogo a los anteriores.
        operet = []

        while i < largo - nu - nd - nm :
          operet.append(lista.pop())
          i += 1

        lista.append(caracter)
        lista = lista + operet
        nd += 1

    elif nivel == 3 : # Operadores * , / : -------
      # Al ser los de mayor jerarquía se añaden al final.
      lista.append(caracter)
      nt +=1

    else : # Paréntesis y espacios: -------
      # No hace ningún cambio.
      lista = lista

  return (lista, nu, nd, nt, nm)
  # Devuelve los valores actualizados de la lista y los contadores.



if __name__ == '__main__' :

  # DEFINNICIÓN DE VARIABLES

  # La ecuación de entrada :
  ecuacion = input("Por favor, escriba su ecuación: ")
  i = 0 # Un iterador para contar la posición en la ecuación.

  # Contadores para :
  nm = 0 # La cantidad de números.
  nu = 0 # la cantidad de + , - .
  nd = 0 # La cantidad de ** .
  nt = 0 # La cantidad de * , / .

  lista = [] # La lista final.
  resultado = "" # la ecuación en notación polaca inversa.
  archivo = open("pasos.txt", "w") # El archivo con los pasos.

  # PROGRAMA

  while i < len(ecuacion) :

    tipo = checar(ecuacion[i]) #  Obtiene la clasificación.

    if tipo[2] == 1 : # Exponentes.

      elementos = (ecuacion, i)
      exp = exponente(elementos) # Corobora si es un exponente.
      i = exp[2] # Actualiza el iterador.

      # Añade la información al txt.
      archivo.writelines("Ordenamos " + str(exp[0])
                         + " en su debida posición según su jerarquía que es " 
                         + "el nivel : " + str(exp[1]) + "\n")

      tipo = (exp[0], exp[1], nu, nd, nt, nm, lista)
      tipo = ordenar(tipo) # Ordena el caracter

      lista = tipo[0] # Actualiza la lista
      # Actualiza los contadores:
      nu, nd, nt, nm =  tipo[1], tipo[2], tipo[3], tipo[4]

    elif tipo[2] == 2 : # Números.

      elementos = (ecuacion, i)
      num = numero(elementos) # Corrobora números de más de un dígito.
      i = num[1] # Actualiza el iterador.

      # Añade la información al txt.
      archivo.writelines("Ordenamos " + str(num[0]) 
                         + " antes de los operadores" + "\n")

      tipo = (num[0], 0, nu, nd, nt, nm, lista)
      tipo = ordenar(tipo) # Ordena el caracter.

      lista = tipo[0] # Actualiza la lista.
      # Actualiza los contadores:
      nu, nd, nt, nm = tipo[1], tipo[2], tipo[3], tipo[4]

    else :

      # Añade la información al txt.
      archivo.writelines("Ordenamos " + str(tipo[0])
                         + " en su debida posición según su jerarquía que es " 
                         + "el nivel : " + str(tipo[1]) + "\n")

      tipo = (tipo[0], tipo[1], nu, nd, nt, nm, lista)
      tipo = ordenar(tipo) # Ordena el caracter.

      lista = tipo[0] # Actualiza la lista.
      # Actualiza los contadores:
      nu, nd, nt, nm = tipo[1], tipo[2], tipo[3], tipo[4]

    i += 1 # Actualia el iterador.


  # Acomoda e imprime el resultado final.

  for itefor in range(len(lista)) :
    resultado = resultado + lista[itefor] + " "

  print("La ecuación en forma Notación Polaca Inversa es : " + resultado)
  print("Puede checar los paso que se siguieron en : pasos.txt")
