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

#boleanos----------------------------------------------------------------------

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

texto=str(input("Por favor ingrese su texto"))
letra1=input("ingrese la primer letra a buscar")
letra2=input("ingrese la segunda letra a buscar")
letra3=input("ingrese la tercera letra a buscar")

texto = texto.lower()

letra1 = letra1.lower()
letra2 = letra2.lower()
letra3 = letra3.lower()



print(f"la letra {letra1} aparece {texto.count(letra1)} veces en  el texto")
print(f"la letra {letra2} aparece {texto.count(letra2)} veces en  el texto")
print(f"la letra {letra3} aparece {texto.count(letra3)} veces en  el texto")

result = len(texto.split())
print(f"el texto tiene {result} palabras")

print(f"la primer letra del texto es {texto[0]}")
print(f"la ultima letra del texto es {texto[-1]}")

lista =texto.split()
print(texto.split())


print(lista[::-1])
print((" ").join(lista[::-1]))

print("python" in texto)