from Scripts.CreateFiles import *

##Importa eventos dependiendo de la funcióna llamar
from ChangedHistory import *

#Definition.CheckFile()

print("*"*10)
print("Crea una categoria")
print("*"*10)

category = str(input("Nombre de categoria"))

va2r = Definition.CreateCategory(category)

print(va2r)