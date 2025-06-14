# IF -ELSE
# age = int(input('Ingresa tu edad:'))
# if (age > 18):
#     print('Bienvenido')
# elif age > 15:
#     print('Secundaria')
# else:
#     print('La peronsa es menor de edad')


salary = int(input('Ingrese su salario'))

if (salary > 500):
    print('No recibe bono Yanapay')
elif (salary >= 250 and salary <= 500):
    print('Recibe bono Yanapay')
elif (salary < 250):
    print('Recibe bono yanapay + Bono')
