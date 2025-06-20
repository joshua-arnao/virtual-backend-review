# Almacenará un bloque de código con su comportamiento y se ejecutará cuando sea llamado
def sum(number1, number2):
    """Función para sumar recibe 2 valores"""
    print("Se sumrá....")
    print(number1 + number2)


sum(5, 7)

# .__doc__ : Mandrá a llamar la función de una documentación si es que existe
print(sum.__doc__)

# Función
user = []


def register(name, email, phone):
    """Función que registra un usuario y lo guarda en una lista"""
    user.append({"name": name, "email": email, "phone": phone})

    return {"message": "Usuario registrado exitosamente", "user": user[0]}


result = register("Joshua", "joshua.arnao@icloud.com", "999888777")

print(result)

products = []


def register_products(name, price, state=True, store="Almacen del cercado"):
    products.append({"name": name, "price": price,
                    "state": state, "store": store})
    return "Producto agregado exitosamente"


register_products("Tomates", 4.5)
register_products("Apio", 1.4, False)
register_products("Cebolla", 5.3, True, "Almacen nuevo mercado")
# Otra forma de pasar parametros
register_products(store="Almacen de la costa",
                  name="pesacado tilapia", price=2.5)

print(products)


# *args:parametros ilimitados de una función
def students(*args):
    print(args)

    # if(len(args) and args[0]):
    #     print('Si hay el valor del puerto')


students("Joshua", 'Mario', 'Jean Carlo', 'Pablo ')
students('Roxana', 'Luis', 'Juan', 'Danny')

# **: nombre del parametro y su valor
# kwards -> Kewword argument


def intoProducts(**kwards):
    print(kwards)
    if (kwards.get('name')):
        print('El usuario quiere agregar un producto con el nombre')
    if (kwards.get('count')):
        print('El usuario quiere ingresar la cantidad del producto')


intoProducts(name='Manzana', price=2.4, state=True, country='Perú')
intoProducts(size='Grande', count=100, name='Pera de agua')

# Recursividad: usarla función dentro de la función


def gret_n_time(limit):
    if (limit == 0):
        return 'Llegue al limite'
    print('Saludar')
    return gret_n_time(limit-1)


result = gret_n_time(10)

print(result)

# Factorial


def factorial(limint):
    if (limint == 0):
        return 1
    return limint * factorial(limint-1)


result = factorial(5)
print(result)


# Operador ternarios
name = 'Maria'
city = 'Cuzco'
result = 'Me caso' if name == 'Cristina' and city == 'Piura' else 'Next'

print(result)


# Lambda funcion
# Funciones que puede tenr unn número inde terminado de argumentps pero solamene una expresión
def squre(number): return number ** 2
def get_igv(price): return price * 0.18


rpta = squre(4)
price_igv = get_igv(100)

print(rpta)
print(price_igv)
