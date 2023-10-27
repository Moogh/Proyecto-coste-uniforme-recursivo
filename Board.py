# Librerias de Python
from tkinter import Label, messagebox
import threading
import time
from Amplitud import Amplitud


# Clases de otros archivos
from Meta import Meta
from Wall import Wall
from Amo import Amo
from Coraje import Coraje
from Gato import Gato

class Board:
    # espacio del tablero
    offset = 30
    space = 40

    w = 0
    h = 0
    #
    def __init__(self, root, recorrido, mapa):
        self.root_secundario = root
        self.recorrido = recorrido
        self.mapa = mapa
        self.initBoard(self.recorrido)


    def initBoard(self, camino):

        self.camino = camino
        self.initWorld()

    def initWorld(self):
        self.coraje = []
        self.walls = []
        self.meta = []
        self.amo = []
        self.gato = []
        x = 0
        y = 0
        
        for i in self.mapa:

            if (i == '\n'):
                y += self.space

                if (self.w < x):
                    self.w = x
                x = 0

            if (i == '#'):
                wall = Wall(x, y)
                self.walls.append(wall)
                x += self.space

            if (i == '%'):
                amo = Amo(x, y)
                self.amo.append(amo)
                x += self.space   

            if (i == '&'):
                gato = Gato(x, y)
                self.gato.append(gato)
                x += self.space  

            if (i == '@'):
                coraje = Coraje(x, y)
                self.coraje.append(coraje)
                x += self.space

            if (i == '$'):
                final = Meta(x, y)
                self.meta.append(final)
                x += self.space

            if (i == ' '):
                x += self.space

            self.h = y + 20
        self.buildWorld()

    #contruccion del mundo con los la interfaz
    def buildWorld(self):
        self.world = []
        self.world += self.walls
        self.world += self.coraje
        self.world += self.meta
        self.world += self.amo
        self.world += self.gato

        for i in self.world:
            if (isinstance(i, Wall)):

                img = Label(self.root_secundario, image=i.getImg())
                img.place(x=i.getX(), y=i.getY())
            

            elif (isinstance(i, Coraje)):
                self.posX = i.getX()
                self.posY = i.getY()
                self.inicio = i
                self.img2 = Label(self.root_secundario, image=i.getImg())
                self.img2.place(x=i.getX() + 4, y=i.getY() + 4)

            elif (isinstance(i, Meta)):
                img3 = Label(self.root_secundario, image=i.getImg())
                img3.place(x=i.getX() + 4, y=i.getY() + 4)

            elif (isinstance(i, Amo)):
                img4 = Label(self.root_secundario, image=i.getImg())
                img4.place(x=i.getX(), y=i.getY())

            elif (isinstance(i, Gato)):
                img5 = Label(self.root_secundario, image=i.getImg())
                img5.place(x=i.getX(), y=i.getY())



        busqueda = Amplitud()
        texto,mastexto,camino= busqueda.raiz(self.recorrido)
        self.recorrido = camino
        thread = threading.Thread(target=self.mostrarCamino)

        thread.start()

    def mostrarCamino(self):
        for i in self.recorrido:
            time.sleep(1)
            self.img2.destroy()
            self.img2 = Label(self.root_secundario,image=self.inicio.getImg())
            self.img2.place(x=(i.getY() * 40) + 4, y=(i.getX() * 40) + 4)

        messagebox.showinfo("Felicidades", "Encontró la meta!!!")
        self.root_secundario.destroy()
        
    def getBoardWidth(self):
        return self.w

    def getBoardHeight(self):
        return self.h
