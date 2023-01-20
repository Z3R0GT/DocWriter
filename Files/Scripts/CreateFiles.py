##Esta tiene como función el crear archivos y asignarles valores
import os

def create():
    file = open("Data/dat.dat", "w")
    file.write("Primera línea" + os.linesep)
    file.write("Segunda línea")
    file.close()


##Crea un heroe con una descripción
def SlotOFHero(Nombre, descripción):
    nameHero = {
        "Nombre: " : Nombre,
        "Descripcion" : descripción
    }
    return nameHero

##crea una habilidad a nombre de una categoria
def SlotOFHability(Categoria, Nombre, Habilidad, descripción):

    name = {
        "Caterigoria: " : Categoria,
        "Nombre: " : Nombre,
        "Habilidad: " : Habilidad,
        "Descripción: " : descripción
    }

    return name

slots = [""]
class Definition:
    def CheckFile():
        if os.path.isfile("Data/dat.dat"):
            print("Archivo Encontrado")
        else:
            create()

    def CreateCategory(newCategory):

        slots.append(newCategory)

        for i in len(slots):
            print(slots[i])

    def AddObjectTo(Category, name):

        Category = {
            str(Category) : name
        }

        return Category



