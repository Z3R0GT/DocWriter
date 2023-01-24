##Registrara los cambios hechos por el
# usuario por medio de "EVENTOS"
import datetime, os

def CreateHystorialFile(dat):
    fecha_actual = datetime.datetime.now().date()

    with open(f"Scripts/Data/{fecha_actual}.dat", "a") as file:
        file.write(str(dat) + os.linesep)

class NotifyEvents:
    """
    Creara eventos y los guardara en un archivo para luego \n
    se leido en caso que el usuario lo desea, sea el caso de output
    """

    def EventInput(event=int, types=str):
        """
        Recive un event tipo int que determina el tag \n
        "type" seria la acción realizada

        :param event:
        :param types:
        :return:
        """
        eventTyper = ["a", "Creación de objeto", "Adjuntado de objeto", "Creado Personaje",
                      "Creado Ambiente", "Creado nuevo tag",
                      "Solicitud de información",
                      "Archivo Guardado", "Se cierra la sesión"
                      ]


        timeNow = datetime.datetime.now().time()

        dat = [timeNow, eventTyper[event], types]
        CreateHystorialFile(dat)
