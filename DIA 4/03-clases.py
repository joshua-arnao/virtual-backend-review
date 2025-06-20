# OOP: Porgramación orientada a objetos
# La programación debe estar creada en base a clases
# Toda parte del código debe de ser tratada como una plantilla
# Clases : Son plantillas para que puedan ser utilizdas varias veces sin la necesidad de modificar su forma en relación al objeto si no al reves
class Person:
    # Las variables creadas dentro de la clase pasan a llamarse atributos
    date_born = '2000-01-01'
    name = 'Joshua'
    state = 'Viudo'

    # Las acciones que puede tener una clase se definen como funciones
    # una función creada dentro de una clase pasa a llamarse metodo
    def great(self):
        # Self: en todos lo metodos de una clase siempre se deben declarar este primer argumento para referenciar a la misma instancia
        self.tell_name()
        self.date_born
        print('Hola como estan')

    def tell_name(self):
        print('digo el nombre')


# Copia de una clase
# Cuando una variable se crea a raiz de una clase pasa a llamarse instancia
# INtancia: es una copia en su totalidad de la clase
person1 = Person()
person2 = Person()

# Modificamos el valor oroginal del atributo a uno personalizados
person1.name = 'Joshua'
person2.name = 'Omaira'

print(person1.name)

# Sobre escribimos el valor predeterminado del atributo nombre a uno nuevo esto genera que todas las instancias ques aun tengan el atributo original cambien el valor ya que es un atributo estatidos
Person.name = 'Juan'
print(person1.name)

# Atributo estatico es un atributo que puede ser accedido sin la necesidad de crear una instancia
# Por defecti en python cualquier atributo creado a nivel de la clae es un atributo estatico
print(Person.name)
print(person2.name)
