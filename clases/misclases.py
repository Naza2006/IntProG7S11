class Estudiante():
    def__init__(self, nombre, apellidos, carrera, cif):
        self.first_name = nombre
        self.last_name = apellidos
        self.major = carrera
        self.cif = cif
        
    def__str__(self):
        return f"{self.cif} {self.first_nanme} {self.last_name} {self.major}"