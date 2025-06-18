number = 0

while number < 10:
    # pass -> sirve para indicar que no se ha definido una lógica

    print(number)
    number += 1
else:
    print("el while termino bien")


# En relación a los siguientes npumeros indicar cuatos son pares y cuantos son impares
numbers = [1, 5, 16, 28, 234, 67, 29]

even_count = 0
odd_count = 0

for x in numbers:
    if x % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print(f"Números pares: {even_count}")
print(f"Números impares: {odd_count}")

position = 0
even_count = 0
odd_count = 0

while position < len(numbers):
    if numbers[position] % 2 ==0:
        even_count += 1
    else: 
        odd_count += 1
    position += 1

print(f"Números pares: {even_count}")
print(f"Números impares: {odd_count}")
