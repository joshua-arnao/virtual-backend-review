# Extraer infomración de la clase Padre

# DRY: Don't Repeat Yoursel
class User:
    def __init__(self, name, lastname, mail):
        self.name = name
        self. lastname = lastname
        self.mail = mail

    def greeting(self):
        return 'Hola soy {}'.format(self.name)


class Student(User):
    def __init__(self, name, lastname, mail, parents):
        # super() llama la clase de la cual estamos haciendo herencia, ademas solo sirve para acceder a los metodos  de la clase que estamos heredando
        super().__init__(name, lastname, mail)
        self.parents = parents

    def info(self):
        return {
            'name': self.name,
            'lastname': self.lastname,
            'patents': self.parents,
            'greeting': super().greeting()
        }


studentJoshua = Student('Joshua', 'Arnao', 'joshua.arnao@correo.com',
                        [{'name': 'Wilme', 'lastname': 'Arnao'}, {'name': 'Yuly', 'lastname': 'Canessa'}])

print(studentJoshua.info())
