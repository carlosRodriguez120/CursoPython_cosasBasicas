# text = "este es el texto de carlos"
# resultado = text.split(" ")
# print(resultado)
# a = "aprender"
# b = "python"
# c = "es"
# d = "genial"
#
# e = " ".join([a, b, c, d])
# print(e)
# print(type(e))
#
#
# print(e.find("es"))
#
#
# print(e.replace("es","era"))
#
# h="hola"
# print(h.center(100,"."))

# frase = "Especialmente en las comunicaciones electrónicas, la escritura enteramente en mayúsculas equivale a gritar."
# print((frase.upper()))
#
# lista_palabras = ["La","legibilidad","cuenta."]
# frase = frase.join([lista_palabras])
# print(frase)

# n1 = "kari"
# n2 = "hi"
#
# print(n1 * 10)
# poema = """
# hola
# amigo
# como
# estas
# """
#
# print(poema.center(100,"."))
#
# text="""Tierra mojada
# mis recuerdos de viaje,
# entre las lluvias"""
#
# print("agua" in text)
#
# palabra ="electroencefalografista"
# print(len(palabra))


# listas--------------------------------------------------------------

# miLista=["g","b","o","d","c","a"]
# print(type(miLista))
# print(len(miLista))
# print(miLista[3])
# miLista.append("e")
# miLista.pop(4)
# print(miLista)
# miLista.sort()
# print(miLista)
#
# medios_transporte = ["avión", "auto", "barco", "bicicleta"]
# medios_transporte.append("motocicleta")
# print(medios_transporte)

# diccionarios---------------------------------------------------------

# diccionario = {"c1":"valor de c1" , "c2":"valor de c2", "c3":"valor de c3"}
# print((diccionario["c2"]))
#
# print(diccionario)
# print(diccionario.values())
# print(diccionario.keys())
# print(diccionario.items())
#
# mi_dic = {"nombre": "Karen", "apellido":"Jurgens","edad":"35","ocupacion":"Periodista"}
# print(mi_dic.values())


# tuplas------------------------------------------------------------------

# tupla=(1,2,3,4,(5,6,4,3,4,5,3),65,6,3)
# print(tupla[4].index(4))

# sets-------------------------------------------------------------------
# miSet = set([1, 4, 3, (1, 2, 3), 5, 6])
# miSet.add(0)
# print(type(miSet))
# print(len(miSet))
#
# set2 = {5, 7, 8, 9, 6}
# s3 = miSet.union(set2)
# print(s3)
# miSet.remove((1,2,3))
# print(miSet)
# sorteo = s3.pop()
# print(sorteo)

# boleanos----------------------------------------------------------------------

# var1=True
# var2=False
#
# print(type(var1))
# print(type(var2))

# num = 5<2+3         <--------- crea un boleano de forma indirecta
# print(type(num))
# print(num)

# num = 5==2+3
# print(type(num))
# print(num)


# num = bool(5>6)
# print(type(num))
# print(num)

# list = [1,2,3,4,5,6,7]
# control = 5 in list
# print(type(control))
# print(control)

"""
-------------------------------------------------------------------------------------------------------------------------
proyecto analizador de texto
en python

"""
#
# texto=str(input("Por favor ingrese su texto"))
# letra1=input("ingrese la primer letra a buscar")
# letra2=input("ingrese la segunda letra a buscar")
# letra3=input("ingrese la tercera letra a buscar")
#
# texto = texto.lower()
#
# letra1 = letra1.lower()
# letra2 = letra2.lower()
# letra3 = letra3.lower()
#
#
#
# print(f"la letra {letra1} aparece {texto.count(letra1)} veces en  el texto")
# print(f"la letra {letra2} aparece {texto.count(letra2)} veces en  el texto")
# print(f"la letra {letra3} aparece {texto.count(letra3)} veces en  el texto")
#
# result = len(texto.split())
# print(f"el texto tiene {result} palabras")
#
# print(f"la primer letra del texto es {texto[0]}")
# print(f"la ultima letra del texto es {texto[-1]}")
#
# lista =texto.split()
# print(texto.split())
#
#
# print(lista[::-1])
# print((" ").join(lista[::-1]))
#
# print("python" in texto)

# operadores logicos-----------------------------------------------------------------------------------------------------
# num1 = 36
# num2 = 17
# mi_bool  = num1>=num2
#
# and
# or
# not

# estructuras  de control if ----------------------------------------------------------------------------------------------

# num1 = input("Ingresa un número:")
# num2 = input("Ingresa otro número:")
#
# f"{num1} es mayor que {num2}"
# "num2 es mayor que num1"
# "num1 y num2 son iguales"
#
# if num2 < num1:
#     print(f"{num1} es mayor que {num2}")
# elif num1 < num2:
#     print(f"{num2} es mayor que {num1}")
# else:
#     print(f"{num1} y {num2} son iguales")

# for-----------------------------------------------------------------------------------
# lista = ["1", "2", "3", "4", "6", "7",]
#
# for letra in lista:
#     print(f"letra {letra} y va en el espacio {lista.index(letra)}")


# lista = ["andres", "pablo","juan","pedro","laura","andres"]
# for nombre in lista:
#     if nombre.startswith("p"):
#         print(nombre)
#
#
# lista2 = [1,2,3,4,5,6,7]
# valor = 0
#
# for n in lista2:
#     valor=valor+n
#
# print(valor)


# arreglo = [[1,2,3,4,5],[1,2,3,4,5],[5,4,3,2,1]]
# for a,b,c,d,e in arreglo:
#     print(a)
#     print(b)
#     print(c)
#     print(d)
#     print(e)

# alumnos_clase = ["María", "José", "Carlos", "Martina", "Isabel", "Tomás", "Daniela"]
# for nombre in alumnos_clase:
#     print(f"Hola {nombre}")


# lista_numeros = [1, 5, 8, 7, 6, 8, 2, 5, 2, 6, 4, 8, 5, 9, 8, 3, 5, 4, 2, 5, 6, 4]
# suma_numeros = 0
#
# for n in lista_numeros:
#     suma_numeros = suma_numeros + n
#
# print(suma_numeros)

# lista_numeros = [1, 5, 8, 7, 6, 8, 2, 5, 2, 6, 4, 8, 5, 9, 8, 3, 5, 4, 2, 5, 6, 4]
# suma_pares = 0
# suma_impares = 0
#
# for n in lista_numeros:
#     if n % 2 == 0:
#         suma_pares = suma_pares + n
#     else:
#         suma_impares = suma_impares + n
#
# print(f"numeros pares{suma_pares}")
# print(f"numeros pares{suma_impares}")

# for -------------------------------------------------------------------------------------
#
# moneda = 5
# while moneda >=0:
#     print(f"tengo {moneda} monedas")
#     moneda -= 1
# else:
#     print("bye")
#

# range-----------------------------------------------------------------------------------
# lista = list(range(2,101,2))
# print(lista)

# enumerate-------------------------------------------------------------------------------
# lista = ["a", "b", "c", "d", "e"]
# for index, n in enumerate(lista):
#     print(index, n)
#
# lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]
#
# for n in lista_nombres:
#     if n.startswith("M"):
#         print(lista_nombres.index(n))

# funcion zip------------------------------------------------------------------------------------------------
# lista_nombres = ["Marcos", "Laura", "Mónica"]
# edades = [23,43,31,34,5345,54,43,4]
# ciudades= ["colombia","andres","miguel"]
# combinacion = list(zip(lista_nombres,edades,ciudades))
# print(type(combinacion))
# print(combinacion)
#
# for n,e,c in combinacion:
#     print(f"{n} tiene {e} y vive en {c}")

# capitales = ["Berlín", "Tokio", "París", "Helsinki", "Ottawa", "Canberra"]
# paises = ["Alemania", "Japón", "Francia", "Finlandia", "Canadá", "Australia"]
# combinacion = list(zip(capitales, paises))
#
# for c, p in combinacion:
#     print(f"La capital de {p} es {c}")

# min y max ---------------------------------------------------------------------------------------------------
# numeros = [12,3,34,4,54,5,6,6,6,4,4,54,4356,345,3,45]
# print(min(numeros))
# print(max(numeros))
#
#
# nombre=["Carlos","endres","juan"]
# for n in nombre:
#     print(min(n.lower()))

# diccionario_edades = {"Carlos":55, "María":42, "Mabel":78, "José":44, "Lucas":24, "Rocío":35, "Sebastián":19, "Catalina":2,"Darío":49}
# edad_minima = min(diccionario_edades.values())
# print(edad_minima)
#
# ultimo_nombre = max(diccionario_edades.keys())
# print(ultimo_nombre)

# RANDOM----------------------------------------------------------------------------------------------------------------------------------------------------------------

# from random import *

# aleatorio = randint(0, 50)
# aleatorioFloat = uniform(0, 50)
# print(aleatorio)
# print(round(aleatorioFloat, 4))  # round para limitar el numero de decimales a 4
#
# print(round(random(),1))  # un numero decimal entre 0 y 1
#
#
# lista = ["azul", "amarillo", "rojo", "negro"]
# print(choice(lista))   #aleatorio de listas DE STRING

# numeros = list(range(5,50,5))
# print(numeros)
# shuffle(numeros)    #MEZCLA LAS LISTAS
# print(numeros)
# numeros.sort()
# print(numeros)

# nombres = ["Carlos", "Julia", "Nicole", "Laura", "Mailen"]
# sorteo=choice(nombres)
# print(sorteo)

# comprension de listas-----------------------------------------------------------------------------------------------------------------------------------------------
# palabra = "python"
#
#
#
# numeros = [num for num in range(0,21,2)]
# print(numeros)
#
# letras = [letra for letra in palabra]
# print(letras)

# valores = [1, 2, 3, 4, 5, 6, 9.5]
# valores_pares = [ n for n in valores if (n%2==0)]
# print(valores_pares)

# temperatura_fahrenheit = [32, 212, 275]
# celsius = [(t-32)*5/9 for t in temperatura_fahrenheit ]
# print(celsius)


# from random import *
#
# nombre = str(input("por favor ingresa TU NOMBRE"))
#
# print(f"Bienvenido {nombre} tienes 8 intentos para adivinar un numero entre 1 y 100")
# intentos = 8
#
# numero = randint(0, 101)
# print(numero)
#
# while intentos > 0:
#     usuario = int(input("ingresa el numero"))
#     if numero == usuario:
#         print("haz asertado")
#         print("felicidades")
#         break
#     elif usuario > 100 or usuario < 0:
#         print("elije un numero que este en rango")
#
#     elif numero > usuario:
#         print("debes elegir un numero mayor")
#     elif numero < usuario:
#         print("elige un numero menor")
#
#     intentos -= 1
#     print(f"te quedan {intentos}")
#
# print("haz perdido")

