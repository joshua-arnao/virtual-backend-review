name = 'Joshua'


def greet():
    # global: indicaremos a la función que queremos utilizar una variable definida fuera de la misma
    global name
    name = name * 2
    print(name)


greet()
