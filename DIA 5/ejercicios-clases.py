# Crear una clase Persona en al cual se guarden su nombre, fecha_nacimiento_nacionalidad_ dni, además también una clase Alumno y una clase Docente en al cual el alumno a diferencia del docente tenga unas erie de cursos matriculados y el docente por su parte tenga un número del seguro social y suc uenta de la CTS. En la se a lo visto en herencia codificaar las clases y ademas ver si hay algún atributo o metodo que deba ser privado

class Persona:
    def __init__(self, name, birthdate, dni):
        self.name = name
        self.birthdate = birthdate
        self.dni = dni


class Alumno(Persona):
    def __init__(self, name, birthdate, dni, cursos_matriculados):
        super().__init__(name, birthdate, dni)
        self.cursos_matriculados = cursos_matriculados


class Docente(Persona):
    def __init__(self, name, birthdate, dni, numero_social, cts):
        super().__init__(name, birthdate, dni)
        self.__numero_social = numero_social
        self.__cts = cts
