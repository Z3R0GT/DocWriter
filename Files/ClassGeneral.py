from Scripts.CreateFiles import *

##Importa eventos dependiendo de la funcióna llamar
from ChangedHistory import *

#Definition.CheckFile()



control = True
def GeneralProgress():
    select = input("\n ¿quieres crear un objeto o una categoria?")

    if select == "categoria":
        while True:
            category = str(input("Nombre de categoria"))
            cat = Definition.CreateCategory(category)

            vec = Definition.ExitGeneral(input("¿Quiere salir?\n R: "))

            if vec:
                break

    elif select == "objeto":
        while True:
            print("*"*20)
            print("Agrega un objeto")
            print("*"*20)

            object = str(input("¿Cual es nombre del objeto? \n R: "))
            hability = str(input("\n ¿Habilidad u efecto?\n R: "))
            desc = str(input("\n ¿Descripcion del objeto?\n R: "))
            category = str(input("\n ¿cual es la categoria a la que pertenece este objeto?\n R: "))

            pur = Definition.SlotOFHability(object,hability,desc,category)


            vec = Definition.ExitGeneral(input("¿Quiere salir?\n R: "))
            if vec:
                break
    elif select == "editar":

        pass

print("*"*10)
print("Crea una categoria y edita un objeto")
print("*"*10)

GeneralProgress()

ext = str(input("¿seguro que quieres salir?\n R: "))
if ext == "*":
    print("Programa finalizado")
else:

    GeneralProgress()
