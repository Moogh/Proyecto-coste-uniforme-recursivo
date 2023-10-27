from tkinter.simpledialog import askstring

class lector:

    def recibir(self, num, fichero):

        fila = 0
        linea = fichero.readline()

        salida = ""
        salida = salida + linea
        juego = []

        aux=[]

        while (linea != ""):
            aux = list(str(linea))
            juego.append(aux)
            fila+=1
            linea = fichero.readline()

            if (linea != ""):
                salida = salida + linea

        if (num == 1):
            return salida

        elif (num == 2):
            return juego