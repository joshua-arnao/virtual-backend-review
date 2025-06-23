# Escriba una función que le pida al usuario ingresar la altura y el ancho de un rectangulo y que lo dibuje usando *, ejemplo:
# altura = 5
# ancho = 4
# Resultado:
# ****
# ****
# ****
# ****
# dibujar_ rectangulo

# Para evitar el salto de línea en una impresión de pantalla print() podemos declarar un parametro end=''

# print('Hola', end='*')
# print('Estos son los ejercios')
# print('Estos', end='\n')


def dibujar_rectangulo():
    while True:
        try:
            altura = int(input('Ingresa la altura: '))
            ancho = int(input('Ingresa la ancho: '))

            if altura > 0 and ancho > 0:
                break
            else:
                print('Ambos valores deben ser mayores que cero. Intente nuevamente')
        except ValueError:
            print('Debe ingresar número enteros válidos. INtente nuevamente')

    for _ in range(altura):
        print('*' * ancho)


# dibujar_rectangulo()


# Esribir una función que nosotros le ingresemos el groso de un octogono y que lo dibuje:
# Ejemplo:
# Grosor: 5
#         *****
# .      *******
# .     *********
# .    ***********
# .   *************
# .   *************
# .   *************
# .   *************
# .   *************
# .    ***********
# .     *********
# .      *******
#         *****
# dibujar_octagono()


def dibujar_octogono():
    while True:
        try:
            grosor = int(input('Ingresar el gorosor del octgono: '))

            if grosor > 0:
                break
            else:
                print('El valor tiene que se mayor a 0, Intentelo otra vez')

        except ValueError:
            print('Debe ingresar número enteros válidos. INtente nuevamente')

    # Parte Superior
    for i in range(grosor):
        espacios = grosor - i - 1
        asteriscos = grosor + 2 * i
        print(' ' * espacios + '*' * asteriscos)

    # Parte media
    ancho_octogono = grosor + 2 * (grosor-1)
    for i in range(grosor-1):
        print('*' * ancho_octogono)

    # Parte inferior
    for i in reversed(range(grosor-1)):
        espacios = grosor - i - 1
        asteriscos = grosor + 2 * i
        print(' ' * espacios + '*' * asteriscos)


# dibujar_octogono()

# Ingresar un número entero y ese número debe de llear a 1 usando la serie de Collatz
# Si el número es par, se divide entre 2
# Si el número es impar, se múltiplica por 3 y se suma 1
# la serie termina cuando el número es 1
# Ejemplo
# 19 58 29 88 44 22 11 34 17 52 26 13 40 20 10 5 16 8 4 2 1
# serie_collatz()

def serie_collatz():
    try:
        numero = int(input("Ingrese un número entero positivo: "))
        if numero <= 0:
            print('Drbr ingresar un npumer mayor a cero.')
            return

        print('Serie de Collatz:')
        while numero != 1:
            print(numero, end=' ')
            if numero % 2 == 0:
                numero = numero // 2
            else:
                numero = 3 * numero + 1

        print(1)

    except ValueError:
        print("Entrada inválida. Por favor ingrese un número entero.")


serie_collatz()
