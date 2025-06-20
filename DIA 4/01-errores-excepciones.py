# Error: mala ejecución del código que hará que mi projecto ya no funcione
# locals()['__builtins__'] -> Me retornará del diccionario de locals() todos los errores definidos dentro de python
# dir -> Nos permite listar estos atributos como string para poder leerlos facilmente
# print(dir(locals()['__builtins__']))

try:
    value = int(input('Ingresa un número:'))
    print(value)

# ValueError: Entrará a este except cuando el error es de tipo TypeError
except ValueError:
    print('Error al convertir un string a un número')
except Exception as error:
    # except: captura el error causante impidiendo que el programa deje de funcionars
    print('Oops algo salio mal intwntalo nuevamente')
    print(error.args)

print('Yo finalizo correctamente')


while True:
    try:
        value = int(input('Ingresa un número'))
        break
    except:
        print('Valor incorrecto, solo pueden ser números')


try:
    result = 1/1
except:
    print('Hubo error')
else:
    # else en el caso de los try-except se ejecutara si nunca ingreso al except
    print('Yo soy else - la división se ejecuto sin problemas')
finally:
    # finally: si el try fue exitoso o no si ingrso a aldun except no
    print('Yo me ejecutare sin todo fue bien y fue mal')
