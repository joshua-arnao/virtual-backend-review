# Coleccion de datos: una variable que almacenas varios valores

# Listas (List) - Arreglos
name = ['Joshua', 'Josue', 'Jesus', 'Jesua']
mix = ['Joshua', 80, False, 15.8, [1, 2, 3]]

print(name[0])
print(name[-1])

# pop() -> Elimina el último elemento de la lista
result = name.pop()
print(result)

# append() -> Añade un elemento al final de la lista
name.append('Juan')

# del -> elimina el contenido de una posición de la lista pero no se puede almacenar en otra variable
del name[0]

# clear() -> Limpia una lista
name.clear()

print(mix[1:3])
print(mix[:2])
print(mix[2:])

month_sale = ['Enero', 'Marzo', 'Julio']
month = 'Septiembre'
month2 = 'Enero'

print(month in month_sale)
print(month2 in month_sale)

# EL not in indicara si el valor se encuentra en la lista
print(month not in month_sale)

section_a = ['Roxana', 'Juan']
section_b = ['Julieta', 'Martin']

print(section_a + section_b)
print(section_a * 2)

# Tuplas
# Es similar a la lista pero no se puede modificar lista: [], tupla:()
# mas de 2 valores separados por un "," se combierte en tupla
course = ('backend', 'frontend')
print(course)
print(course[0])

mix = (1, 2, 3, [4, 5, 6])
mix[3][0] = 'Hola'
print(mix)


print(2 in mix)

# len() => para ver la cantidad de elementos que conforman una lista o una tupla
print(len(mix))


# Conjuntos: Colección de datos desordenada, una vez creada no se puede acceder a las posiciones de sus elementos
states = {'Verano', 'Otonio', 'Primaver', 'Invierno'}

print(states)

# clases(los tipos de datos) > metodos (depende de la clase)

# Diccionarios: colección de datos desordenada pero cada elemento obedece a una llave definida
person = {'name': 'Joshua', 'lastname': 'Arnao', 'email': 'joshua@correo.com'}

# .get() => hace la busqueda y si no encuentra retorna un none o lo que se sete
print(person.get('apellidos', ' No esta'))
print(person.keys())
