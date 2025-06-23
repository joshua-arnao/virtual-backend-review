class Animal:
    # Atrubitos estaticos ↓
    # name = ''
    # gender = ''
    # paws = 0

    # Metodos
    # Constructor: Este metodo se llamara cuando crreemos una nueva instancia de la clase
    # Self: apunta a la misma instancia con todos sus valores y a todos sus atributos dentro de esa misma instancia
    def __init__(self, name, gender, numb_paws):
        self.name = name
        self.gender = gender
        self.paws = numb_paws

    def description(self):
        return 'Yo soy un {}, soy {}, y tengo {} patas'. format(self.name, self.gender, self.paws)


foca = Animal('Foca', 'M', 2)
caballo = Animal('Caballo', 'M', 4)
gato = Animal('Gato', 'F', 4)

print(foca.description())
