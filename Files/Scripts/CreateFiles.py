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

def Category(Category):

    slots.append(Category)
    return slots


slots = ["Default"]
class Definition:

    def ExitGeneral(entrace):

        if entrace == "*":
            return True
        else:
            print("*"*20)
            print("Volveremos a ejecutar")
            print("*"*20, "\n")

    def CheckFile():
        if os.path.isfile("Data/dat.dat"):
            print("Archivo Encontrado")
        else:
            create()


    def CreateCategory(newCategory):
        Category(newCategory)

    ##crea una habilidad a nombre de una categoria

    def SlotOFHability(Nombre, Habilidad, descripción, Categoria):
        """ Crea un espacio para habilidad.\n
        :param Nombre El objeto a crear
        :param Habilidad Que es lo que hace el objeto
        :param descripción Descripción del objeto
        :param Categoria Objeto al cual pertenece.
        """
        name = {}

        ver = False
        lenght = len(slots)

        for i in range(lenght):
            print("h")


            if slots[i] == Categoria:
                print("h")
                name = {
                    "Nombre: " : Nombre,
                    "Habilidad: " : Habilidad,
                    "Descripción: " : descripción,
                    "Categoria: " : Categoria
                }
                return name
            else:
                ver = True

            if ver:
                this = Category(Categoria)
                this = slots.pop()
                print("no encontre la categoria")
                name = {
                    "Nombre: " : Nombre,
                    "Habilidad: " : Habilidad,
                    "Descripción: " : descripción,
                    "Categoria: " : this
                }
                return name




        return name


    def AddObjectTo(Category, name):

        Category = {
            str(Category) : name
        }

        return Category



