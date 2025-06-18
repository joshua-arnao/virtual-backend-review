notes = [10, 20, 16, 8, 6, 1]
for note in notes:
    print(note)

# range(min(start), max(stop), incremento/decremento([step]))

for number in range(10):
    print(number)
for number in range(1, 10):
    print(number)
for number in range(5, 10, 2):
    print(number)


# imprimer los 3 valores iniciales de notas

for nota in notes[:3]:
    print(nota)

for posicion in range(3):
    print(notes[posicion])

approveds = ['Joshua', 'Maria', 'Simon', 'Fatima']

for approved in approveds:
    if (approved == 'Joshua'):
        print('Joshua esta aprobado')
        break
else:
    print('No se encontro el alumno a buscar')

print('Termino de ejecutarse el for')



products = ['manzanas','peras','Tallarines','Tazas']
search = input('Ingresa el producto a buscar:')

for product in products:
    if product == search:
        print('El producto si esta en la tienda')
        break
else:
    print('No se econtro el producto')
