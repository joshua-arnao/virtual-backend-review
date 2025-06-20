productId = input('Ingresa el id del producto:')
try:
    if (productId == '10'):
        raise Exception('El producto no existe en la base de datos')
    # expect si hubo error
except Exception as e:
    print('Oops allgo salio mal con el producto a buscar', e.args[0])
    # else si hubo error
else:
    print('El producto encontrado es: ...')

finally:
    print({'message': 'resultado final'})
print('yo soy el final del programa')
