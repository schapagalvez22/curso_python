cadena1="hola soy samuel"
cadena2="Bienvenido Samuel"


resultado = cadena1.upper()  #convierte a mayusculas


resultado1 = cadena2.lower()  #convierte a minusculas
contar = cadena1.count("o")  #cuenta cuantas veces aparece la letra "o" en la cadena1   
contar_caracteres = len(cadena1)  #cuenta cuantos caracteres tiene la cadena1

#dame una lista de metodos de cadenas en python con su descripcion y un ejemplo de cada uno

metodos_cadenas = dir(cadena1)
print("Métodos de cadenas en Python:")
for metodo in metodos_cadenas:
    print(metodo)

print(resultado1)
print(contar)
print(contar_caracteres)
