# ENcapsulamiento: Es declarar tipos de accesibiidad a los atributos y metodos
class Product:
    def __init__(self, name, price):
        # Existen 3 tipos de accesibilidad a los atibutos y metodos de una clase:
        # Public -> Cualquier instancia puede acceder(desde la misma clase como en su instancia)
        self.name = name
        self.price = price
        # Privada -> No se pude acceder a el fuera de la clase
        # un atributoes privado cuando no es necesaria la interacción con un agente externo
        self.__revenue = self.price * 0.30
        # self.__benefits = True if self.price > 500 else False
        # protegido protected: metodo privado puede ser accedido desde dentro de la clase

    def show_info(self):
        return {
            'name': self.name,
            'precio': self.price,
            'revenue': self.__revenue,
            'igv': '{:.3f}'.format(self.__calculate_igv()),
            # 'benefits': self.__benefits
        }

    def grow_revenue(self):
        self.__revenue = self.__revenue * 1.10

    def __calculate_igv(self):
        result = self.price * 0.18

        return result


cepillo = Product('Cepillo dental', 3.8)

# atributo público que puede ser accedido desde la clase y desde su intancia
cepillo.name

# Atributo provado solamente puede ser accedido dentro de la misma clase
cepillo.__revenue = 100
print(cepillo.show_info())

cepillo.grow_revenue()
print(cepillo.show_info())
