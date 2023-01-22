import time
from Scripts.CreateFiles import *

##Importa eventos dependiendo de la funcióna llamar
from ChangedHistory import *




def GeneralProgress():
    select = input("\n ¿Quieres crear un objeto o una categoria? \nR: ")

    if select == "categoria":
        while True:
            Definition.LabelNot(1)

            print("\n1- Objeto /// 2- Ambiente /// 3 - Personaje")
            des = input("Selecciona una opción de categoria \nR:")

            category = str(input("\nNombre de categoria \nR: "))
            cat = Definition.CreateCategory(category, des)

            #Definition.CheckFile(slots)

            vec = Definition.ExitGeneral(input("¿Quiere salir?\n R: "))
            if vec:
                select = ""
                GeneralProgress()

    elif select == "objeto":
        while True:
            Definition.LabelNot(2)

            object = str(input("\n¿Cual es nombre del objeto? \n R: "))
            hability = str(input("\n ¿Habilidad u efecto?\n R: "))
            desc = str(input("\n ¿Descripcion del objeto?\n R: "))
            category = str(input("\n ¿cual es la categoria a la que pertenece este objeto?\n R: "))

            pur = Definition.SlotOFHability(object, hability, desc, category, 1)
            print(pur)

            vec = Definition.ExitGeneral(input("¿Quiere salir?\n R: "))

            if vec:
                GeneralProgress()

    elif select == "editar":
        cer = Definition.SolicityInfo()

        vec = Definition.ExitGeneral(input("¿Quiere salir?\n R: "))
        if vec:
            GeneralProgress()
    elif select == "Ambiente":
        Definition.LabelNot(3)

        object = str(input("\n¿Cual es nombre del lugar? \n R: "))
        hability = str(input("\n ¿Cual es la historia?\n R: "))
        desc = str(input("\n ¿Como se ve?\n R: "))
        category = str(input("\n ¿cual es la categoria (nivel de importancia)?\n R: "))

        Definition.LabelNot(4)

        temp = input("Desea darle un nuevo tipo de zona al Ambiente/zona\nY/N: ")
        if temp == "Y" or temp == "y":
            Type = input("¿Como se llama tu Ambiente/zona")
            ver = Definition.SlotOFHability(object, hability, desc, category, 2, Type)
            print(ver)
        else:
            ver =Definition.SlotOFHability(object, hability, desc, category, 2)
            print(ver)

        vec = Definition.ExitGeneral(input("¿Quiere salir?\nR: "))
        if vec:
            GeneralProgress()
    elif select == "Personajes":
        pass






    elif select == "*":
        pass

    vec = Definition.ExitGeneral(input("\n¿Quiere salir del programa?\n R: "))
    if vec:
        GeneralProgress()
        Definition.ExitGeneral("no")
        time.sleep(5)

Definition.LabelNot(0)
GeneralProgress()
