##Esta tiene como función el crear archivos y asignarles valores
import os

def create():
    file = open("Data/dat.dat", "w")
    file.write("Primera línea" + os.linesep)
    file.write("Segunda línea")
    file.close()

def types():


    pass

class Definition:
    def GeneralClass():

        if os.path.isfile("Data/dat.dat"):
            print("Archivo Encontrado")
        else:
            create()

    GeneralClass()