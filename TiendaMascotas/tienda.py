import os

from TiendaMascotas.dominio.inventario import Inventario
from TiendaMascotas.dominio.mascota import Mascota
from TiendaMascotas.dominio.perro import Perro
from TiendaMascotas.infraestructura.persistenciaMascota import PersistenciaMascota
from TiendaMascotas.infraestructura.persistenciaPerro import PersistenciaPerro
from TiendaMascotas.infraestructura.persistenciaGato import PersistenciaGato
from TiendaMascotas.infraestructura.persistenciaAve import PersistenciaAve
from TiendaMascotas.infraestructura.persistenciaCamaleon import PersistenciaCamaleon
from TiendaMascotas.infraestructura.persistenciaCuy import PersistenciaCuy
import random

inventario = Inventario()

if __name__ == '__main__':

    saverPerro = PersistenciaPerro()
    saverGato = PersistenciaGato()
    saverAve = PersistenciaAve()
    saverCamaleon = PersistenciaCamaleon()
    saverCuy = PersistenciaCuy()

    menuPrincipal = True
    subMenu = True
    while menuPrincipal:

        menuPrincipal = int(input("Eliga lo que quiera hacer en el menú: \n"
                                  "1. Agregar mascota \n"
                                  "2. Salir \n"
                                  "Por favor ingrese una opcion del menú: "))

        if menuPrincipal == 1:
            while subMenu:
                if subMenu == 1:
                    subMenu = int(input("Eliga el animal que desea agregar: \n"
                                        "1. Perro \n"
                                        "2. Gato \n"
                                        "3. Ave \n"
                                        "4. Camaleon \n"
                                        "5. Cuy \n"
                                        "6. Volver al menú principal "))

                    if subMenu == 1:
                        razas = ['Mestizos', 'Labrador_Retrievers', 'Pastor_Aleman', 'Beagles']
                        colores = {
                            'Mestizos': ['blanco', 'negro', 'cafe', 'manchado con blanco y negro'],
                            'Labrador_Retrievers': ['blanco', 'negro', 'cafe', 'mono'],
                            'Pastor_Aleman': ['cafe', 'negro', 'blanco', 'cafe con negro'],
                            'Beagles': ['mono con negro', 'blanco con mono', 'mono con negro y blanco']
                        }
                        nombres = ['Lufy', 'Polo', 'Garozo', 'Nieve']
                        tamanios = ['pequeño', 'mediano', 'grande']
                        precios = [50000, 80000, 150000, 500000, 35000, 5000000]
                        edades = [1, 2, 3]
                        tipo_Pelos = ['lizo', 'rizado', 'raso', 'semi largo']
                        cantidad_perros = random.randint(100, 1000)
                        raza = random.choice(razas)
                        color = random.choice(colores[raza])
                        nombre = random.choice(nombres)
                        tamanio = random.choice(tamanios)
                        precio = random.choice(precios)
                        edad = random.choice(edades)
                        tipo_Pelo = random.choice(tipo_Pelos)
                        g = Perro(nombre, raza, tamanio, precio, edad, color, tipo_Pelo)
                        inventario = Inventario()
                        inventario_json = Inventario()

                        menuGuardarPrimero = int(input("Eliga en que manera desea guardar: \n"
                                  "1. Agregar en save_json_perro \n"
                                  "2. Agregar en base de datos \n"
                                  "3. Volver al menú \n"
                                    "Por favor ingrese una opcion del menú: "))

                        if menuGuardarPrimero == 1:
                            PersistenciaPerro.save_json(g)
                            for file in os.listdir("./files"):
                                if '.json' in file:
                                    inventario_json.agregar_perro(PersistenciaPerro.load_json(file))
                            for g in inventario.perros:
                                PersistenciaPerro.save_json(g)
                                print("La mascota ha sido añadida con exito")
                                print(subMenu)

                        elif menuGuardarPrimero == 2:
                            saverPerro.guardar_perro(g)
                            print("La mascota ha sido añadida con exito")
                            print(subMenu)

                        elif menuGuardarPrimero == 3:
                            print(menuPrincipal)

                        else:
                            print("Por favor ingrese bien los numeros")
                            print(menuGuardarPrimero)

                elif subMenu == 6:
                    print(menuPrincipal)

        elif menuPrincipal == 2:
            print("Gracias por visitar la tienda!")