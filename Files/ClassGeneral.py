import time
from os import system
from Scripts.CreateFiles import *

##Importa eventos dependiendo de la funcióna llamar
from ChangedHistory import *



#
def GeneralProgress():
    print("*"*42)
    print("*               Menú de inicio           *\n"
          "*               DocWriter 1.0            *\n"
          "* --Herramienta simple basada en texto --*\n"
          "*       de escritores para escritores    *\n"
          "*                                        *\n"
          "*Elige cual quieres crear:               *\n"
          "*- categoria                             *\n"
          "*- objeto                                *\n"
          "*- Ambiente                              *\n"
          "*- Personaje                             *")
    print("*"*42)
    time.sleep(5)
    select = input("\n ¿Quieres crear? \nR: ")

    if select == "categoria":
        while True:
            Definition.LabelNot(1)

            print("\n1- Objeto /// 2- Ambiente /// 3 - Personaje")
            des = input("Selecciona una opción de categoria \nR:")

            time.sleep(4)

            category = str(input("\nNombre de categoria \nR: "))
            cat = Definition.CreateCategory(category, des)

            time.sleep(4)
            vec = Definition.ExitGeneral(input("¿Quiere salir?\n R: "))
            if vec:
                system("cls")
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

            time.sleep(5)

            vec = Definition.ExitGeneral(input("¿Quiere salir?\n R: "))

            if vec:
                system("cls")
                GeneralProgress()

    elif select == "editar":
        cer = Definition.SolicityInfo()

        vec = Definition.ExitGeneral(input("¿Quiere salir?\n R: "))
        if vec:
            system("cls")
            GeneralProgress()
    elif select == "Ambiente":
        Definition.LabelNot(3)

        time.sleep(3)

        object = str(input("\n¿Cual es nombre del lugar? \n R: "))
        hability = str(input("\n ¿Cual es la historia?\n R: "))
        desc = str(input("\n ¿Como se ve?\n R: "))
        category = str(input("\n ¿cual es la categoria (nivel de importancia)?\n R: "))

        time.sleep(4)
        Definition.LabelNot(4)
        time.sleep(2)

        temp = input("Desea darle un nuevo tipo de zona al Ambiente/zona\nY/N: ")
        if temp == "Y" or temp == "y":
            Type = input("¿Como se llama tu Ambiente/zona")
            ver = Definition.SlotOFHability(object, hability, desc, category, 2, Type)

            print(ver)
        else:
            ver =Definition.SlotOFHability(object, hability, desc, category, 2)
            print(ver)

        time.sleep(4)

        vec = Definition.ExitGeneral(input("¿Quiere salir?\nR: "))
        if vec:
            system("cls")
            GeneralProgress()
    elif select == "Personajes":
        Definition.LabelNot(4)

        time.sleep(3)

        object = str(input("\n¿Cual es nombre del personaje? \n R: "))
        hability = str(input("\n ¿Cual es su historia?\n R: "))
        desc = str(input("\n ¿Como se ve?\n R: "))
        category = str(input("\n ¿cual es el nivel de importancia?\n R: "))

        time.sleep(4)
        ver = Definition.SlotOFHability(object,hability,desc,category,3)
        print(ver)

        time.sleep(4)
        vec = Definition.ExitGeneral(input("¿Quiere salir?\nR: "))
        if vec:
            system("cls")
            GeneralProgress()
    elif select == "*":
        pass
    vec = Definition.ExitGeneral(input("\n¿Quiere salir del programa?\n R: "))
    if vec:
        system("cls")
        Definition.LabelNot(6)
        time.sleep(5)
    else:
        system("cls")
        GeneralProgress()


Definition.LabelNot(0)
GeneralProgress()
