from Scripts.CreateFiles import *

##Importa eventos dependiendo de la funcióna llamar
from ChangedHistory import *

#Definition.CheckFile()

print("*"*10)
print("Crea una categoria y edita un objeto")
print("*"*10)


select = input("\n ¿quieres crear un objeto o una categoria?")

if select == "categoria":
    while True:
        category = str(input("Nombre de categoria"))

        put = Definition.CreateCategory(category)

        exit = input("¿quieres salir?")

        if exit == 0:
            pass
        else:
            break
elif select == "objeto":
    while True:
        print("*"*20)
        print("Agrega un objeto")
        print("*"*20)

        object = str(input("¿Cual es nombre del objeto? \n R: "))

        hability = str(input("\n ¿Habilidad u efecto?\n R: "))

        desc = str(input("\n ¿Descripcion del objeto?\n R: "))

        category = str(input("\n ¿cual es la categoria a la que pertenece este objeto?"))

        put = Definition.SlotOFHability(object,hability,desc,category)
        print(put)
        break