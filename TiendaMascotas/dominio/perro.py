import uuid

class Perro:

    def __init__(self, nombre, raza, tamanio, precio, edad, color, tipoPelo, *args, **kargs):
        self.nombre = nombre
        self.raza = raza
        self.tamanio = tamanio
        self.precio = precio
        self.edad = edad
        self.color = color
        self.tipoPelo = tipoPelo
        self.id = uuid.uuid4()

    def __str__(self):
        return f"{self.nombre}---{self.raza}---{self.tamanio}---{self.precio}---{self.edad}---" \
               f"{self.color}---{self.tipoPelo}---{self.id}"

    def __repr__(self):
        return str(self.id)

    def cumplePerro(self, especificacion):
        dict_perro = self.__dict__
        for k in especificacion.get_keys():
            if k not in dict_perro or dict_perro[k] != especificacion.get_value(k):
                return False
        return True