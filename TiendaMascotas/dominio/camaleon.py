import uuid

class Camaleon:

    def __init__(self, nombre, raza, tamanio, precio, edad, color, tipoCola, *args, **kargs):
        self.nombre = nombre
        self.raza = raza
        self.tamanio = tamanio
        self.precio = precio
        self.edad = edad
        self.color = color
        self.tipoCola = tipoCola
        self.id = uuid.uuid4()
        
    def __str__(self):
        return f"{self.nombre}---{self.raza}---{self.tamanio}---{self.precio}---{self.edad}---" \
               f"{self.color}---{self.tipoCola}---{self.id}"
    
    def __repr__(self):
        return str(self.id)

    def cumpleCamaleon(self, especificacion):
        dict_camaleon = self.__dict__
        for k in especificacion.get_keys():
            if k not in dict_camaleon or dict_camaleon[k] != especificacion.get_value(k):
                return False
        return True