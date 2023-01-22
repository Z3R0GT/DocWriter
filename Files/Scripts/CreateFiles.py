##Esta tiene como función el crear archivos y asignarles valores
import os

#Clase general donde se guarda
Matrix = []
#ObjectSlot - espacio para objetos
ObjectSlot = []
#EnvioSlot - espacio para ambiente
EnvioSlot = ["Ciudad", "Paisaje", "Pueblo"]
#npcSlot - espacio para personaje
npcSlot = []

def create(Matrix, check):
    """
    Crea un archivo, comprueba si existe el archivo "check"
    matrix sera el arreglo de datos a guardar
    :param Matrix:
    :param check:
    :return:
    """
    if check:
        file = open("Data/dat.dat", "w")
        file.close()
    elif not check:
        file = open("Data/dat.dat", "w")
        file.write(Matrix)
        file.close()

def Category(name, obj, env, npc):
    """
    Crea una categoria con "name" y la
    agrega a matrix

    :param obj:
    :param env:
    :param npc:
    :param name:
    :return:
    """

    #Agregan objetos
    if obj:
        ObjectSlot.append(name)

    if env:
        EnvioSlot.append(name)

    if npc:
        npcSlot.append(name)

    #Verifica si debe o no agregar un objeto
    if len(ObjectSlot) == 1:
        Matrix.append(ObjectSlot)

    if len(EnvioSlot) == 1:
        Matrix.append(EnvioSlot)

    if len(npcSlot) == 1:
        Matrix.append(npcSlot)

def SearchCategory(Category, Objects, Type):
    """
    buscara la categoria (Category), y agrega el objeto
    alado de esta.

    1 - Objetos \n
    2 - Ambiante \n
    3 - Personaje
    :param Type:
    :param Category:
    :param Objects:
    :return:
    """

    if Type == 1:
        for i in range(len(ObjectSlot)):
            if ObjectSlot[i] == Category:
                ObjectSlot.insert(i + 1, Objects)
    elif Type == 2:
        for i in range(len(EnvioSlot)):
            if EnvioSlot[i] == Category:
                EnvioSlot.insert(i + 1, Objects)
    elif Type == 3:
        for i in range(len(npcSlot)):
            if npcSlot[i] == Category:
                npcSlot.insert(i + 1, Objects)

class Definition:
    """
    Tiene como proposito el escribir variables, imprimir casos
    revisar si el archivo "dat.dat" existe y por ultimo
    guardar los datos, mas no puede re-escribirlos
    """
    def LabelNot(case):
        """
        "case" sea el numero \n
        0 - Menu \n
        1 - Categorias \n
        2 - Objetos \n
        3 - Ambiente general \n
        4 - Personaje
        :param case:
        :return:
        """
        lab = print("*"*20)

        if case == 0:
            lab
            print("Crea una categoria y edita un objeto")
        elif case == 1:
            lab
            print("Creador de categorias")

        elif case == 2:
            lab
            print("Creador de objetos")

        elif case == 3:
            lab
            print("Creador de Ambientes")
        elif case == 4:
            lab
            print("Recuerda que por default tiene: Ciudad")
        elif case == 5:
            lab
            print("Creador de Personaje")


    def ExitGeneral(entrace):
        """
        Recibe una entrada "*" para salir, retornara True para confirmar la salida

        :param entrace:
        :return:
        """
        if entrace == "*":
            return True
        else:
            print("*" * 20)
            print("Volveremos a ejecutar")
            print("*" * 20, "\n")

    def CheckFile(Matrix):
        """
        Revisara si archivo esta en el destino, sino, lo creara

        :param Matrix:
        :return:
        """
        if os.path.isfile("Data/dat.dat"):
            create(Matrix, False)
        else:
            create(Matrix, True)

    def CreateCategory(newCategory, type):
        """
        Crea una categoria. \n
        1 - Objeto. \n
        2 - Ambiente. \n
        3 - Personaje

        :param type:
        :param newCategory:
        :return:
        """

        if type == "1" or type == "Objeto":
            Category(newCategory,True, False, False)
        elif type == 2 or type == "Ambiente":
            Category(newCategory,False,True,False)
        elif type == 3 or type == "Personaje":
            Category(newCategory,False,False,True)

    ##crea una habilidad a nombre de una categoria

    def SlotOFHability(Nombre, Habilidad, descripción, Categoria, Type, TypeEnv="Ciudad"):
        """Crea un espacio dentro del array "slots". \n

        1 - Objeto\n
        2 - Ambiente\n
        3 - Personaje\n
        El "TypeEnv" tiene como Default Ciudad, Paisaje, Pueblo
        
        :param TypeEnv: 
        :param Type:
        :param Habilidad:
        :param descripción:
        :param Categoria:
        :return:
        """

        if Type == 1:
            lenght = len(ObjectSlot)
            for i in range(lenght):
                if ObjectSlot[i] == Categoria:
                    Objects = {
                        "Nombre ": Nombre,
                        "Habilidad ": Habilidad,
                        "Descripción ": descripción,
                        "Categoria ": Categoria
                    }
                    SearchCategory(Categoria, Objects, 0)
                    return Objects

            ver = True
            if ver:
                Category(Categoria, True, False, False)
                print("Su categoria no fue encontrada, \nhe creado una nueva ")
                Objects = {
                    "Nombre ": Nombre,
                    "Habilidad ": Habilidad,
                    "Descripción ": descripción,
                    "Categoria ": Categoria
                }
                SearchCategory(Categoria, Objects, 1)
                return Objects

        elif Type == 2:
            lenght = len(EnvioSlot)

            for i in range(lenght):
                if EnvioSlot[i] == Categoria:
                    ENV = {
                        TypeEnv:Nombre,
                        "Descripcion ":descripción,
                        "Historia:":Habilidad,
                        str("Categoria del " + TypeEnv):Categoria
                    }
                    SearchCategory(Categoria,ENV,2)
                    return ENV
            ver = True

            if ver:
                Category(Categoria,False,True,False)
                print("Su categoria no fue encontrada, \nhe creado una nueva ")
                ENV = {
                    TypeEnv:Nombre,
                    "Descripción ": descripción,
                    "Historia":Habilidad,
                    str("Categoria del "+ TypeEnv):Categoria
                }
                SearchCategory(Categoria,ENV,2)
                return ENV

        elif Type == 3:
            lenght = len(npcSlot)
            for i in range(lenght):
                if npcSlot[i] == Categoria:
                    NPC = {
                        "Nombre":Nombre,
                        "Descripción":descripción,
                        "Historia":Habilidad,
                        "Tipo de Actuación":Categoria
                    }
                    SearchCategory(Categoria,NPC,3)
                    return NPC

            ver = True
            if ver:
                Category(Categoria,False,False,True)
                print("Su categoria no fue encontrada, \nhe creado una nueva ")
                NPC = {
                    "Nombre":Nombre,
                    "Descripción":descripción,
                    "Historia":Habilidad,
                    "Tipo de Actuación":Categoria
                }
                SearchCategory(Categoria,False,False,True)
                return NPC

    def SolicityInfo():
        print(Matrix)
        pass
