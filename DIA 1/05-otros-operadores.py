# COMPARISON OPERATORS
number1, number2 = 10, 20

# EQUAL TO
print(number1 == number2)

# MAYER THAN || MAYOR EQUAL TO
print(number1 > number2)
print(number1 >= number2)

# LESSER THAN || LESSER THAN EQUAL TO
print(number1 < number2)
print(number1 <= number2)

# DIFFERENCE
print(number1 != number2)

# LOGICS OPERATORS
print((10 > 5) and (10 < 20))
print((10 > 5) or (10 < 20))

# IDENTITY OPERATORS
vegetable = ['apio', 'lettuce', 'zapallo']
vegetable2 = vegetable
vegetable3 = ['apio', 'lettuce', 'zapallo']

# NOTA: Las coleccioes de datos son variables mutables (cuando cambian su contenido este se vera reflejado en todos las copias)
vegetable2[0] = 'perejil'
vegetable[1] = 'manzana'

print(vegetable2 is vegetable)
print(vegetable)
print(vegetable2)
print(vegetable3 is vegetable)


name = 'Joshua'
country = 'Perú'

print(name == 'Joshua' and (country == 'Perú' or country == 'Colombia'))
