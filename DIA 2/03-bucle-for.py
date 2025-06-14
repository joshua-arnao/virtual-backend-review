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


