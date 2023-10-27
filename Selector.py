# Librerias de Python
from tkinter import Label, Frame, Button, Tk, scrolledtext, ttk, messagebox, LabelFrame, Toplevel
import tkinter
from PIL import ImageTk
from os import listdir
from os.path import isfile, join
# Clases de otros archivos
from lector import lector
from Amplitud import Amplitud
from Costo import Costo
from Board import Board


font = 'Segoe UI'
background = 'gray8'
blanco = 'white'
c_boton = 'darkorchid4'


# clase GUIINICIO 

class GUIinicio:

    def __init__(self):
        self.root_inicio = Tk()
        self.root_inicio.title("Recorridos IA")
        self.root_inicio.geometry("732x510")
        self.root_inicio.resizable(0,0)
        self.root_inicio.iconbitmap("Images/ia.ico")
        self.root_inicio.config(cursor='top_left_arrow')
#833
        # imagen de fondo
        self.bg = ImageTk.PhotoImage(file="Images/fondo.png")
        Label(self.root_inicio, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)

        #lado izquierdo completo
        self.frame_izq = Frame(self.root_inicio, bg=background)
        self.frame_izq.place(x=5, y=15, width=280, height=480)
        Label(self.frame_izq, text="BUSQUEDAS NO\nINFORMADAS IA", font=(font, 15, "bold"), bg=background, fg=blanco).place(
            x=60, y=15)

        # informacion inicial 
        Label(self.frame_izq, text="Busquedas por\namplitud, costos y profundidad.\nSeleccione la busqueda a emplear: ",
              font=(font, 12, "italic"), bg=background, fg=blanco).place(x=15, y=80)

        # lista de caminos a recorrer
        ruta = r'Caminos/'
        contenido = listdir(ruta)
        archivo = [nombre for nombre in contenido if isfile(join(ruta, nombre))]
        # etiqueta de seleccion
        Label(self.frame_izq, text="Seleccione el nivel", font=(font, 12, 'italic'), bg=background, fg=blanco).place(x=70,
                                                                                                               y=150)
        self.lista = ttk.Combobox(self.frame_izq, width=20, height=12, state='readonly')
        self.lista['values'] = archivo
        self.lista.place(x=70, y=180)

        # boton busqueda
        boton_busqueda = Button(self.frame_izq, text="Busqueda", command=self.iniciar, font=(font, 15), bg=c_boton,
                            fg=blanco, bd=2, cursor="top_left_arrow")
        boton_busqueda.place(x=40, y=323, width=200)

        # boton integrante
        boton_info = Button(self.frame_izq, text="Integrante", command=self.info_grupo, font=(font, 15), bg=c_boton, fg=blanco,
                            bd=2, cursor="top_left_arrow")
        boton_info.place(x=40, y=410, width=55,)

        # boton salir 
        boton_salir = Button(self.frame_izq, text="Salir", command=self.root_inicio.destroy, font=(font, 15), bg=c_boton,
                             fg=blanco, bd=2, cursor="top_left_arrow")
        boton_salir.place(x=170, y=410, width=70)

        # franja de la derecha 
        self.frame_der1 = LabelFrame(self.root_inicio,text='Costo',labelanchor='n',font=(font,15,'bold'),bd=0,fg=blanco ,bg=background)
        self.frame_der1.place(x=510, y=15, width=215, height=480)

        # lado centro
        self.frame_der2 = LabelFrame(self.root_inicio,text='Amplitud',labelanchor='n',font=(font,15,'bold'),bd=0,fg=blanco ,bg=background)
        self.frame_der2.place(x=290, y=15, width=215, height=480)
        self.root_inicio.mainloop()

    def info_grupo(self):
        messagebox.showinfo("Introducción Inteligencia Artificial", "Desarrollado por:\n\n "
                                                                       "* Santiago Gonzalez Rodriguez \n"
                                                                       "  1958714-3743\n"
                                                                       )

    def iniciar(self):

        leer = lector() # crean una instancia de la clase 
        self.camino = self.lista.get() # asignan el valor de la selección actual en la lista a la variable
        fichero = open('Caminos/' + self.camino)# selecionamos los caminos
        self.cami = leer.recibir(1, fichero) # las coordenadas de inicio y fin del camino
        fichero = open('Caminos/' + self.camino)#  se vuelve a abrir 
        self.recorrido = leer.recibir(2, fichero)#  se deben leer los datos del segundo tipo 
        
        
         # poner en el texto de la derecha y proceder hacer la otra busqueda
        busquedaC = Costo()
        self.text = scrolledtext.ScrolledText(self.frame_der1,width = 10,height = 15, font = (font,15))
        self.text.grid(column = 0, pady = 10, padx = 50)
        camino_costo = busquedaC.costo(self.recorrido)
        listaCosto = ""
        for i in range(len(camino_costo) - 1):
            listaCosto += str(camino_costo[i]) + "\n"
        nodosC = str(camino_costo[-1])  # obtiene el último elemento y lo convierte en cadena
        listaCosto += "\n Numero de Nodos: " + nodosC  # agrega el último elemento a la cadena
        self.text.insert(tkinter.INSERT, listaCosto)                                            
        self.text.configure(state ='disabled',bg=background,fg=blanco,bd=0)
        
        # poner en el texto del medio y hacer la otra busqueda
        amplitud = Amplitud()
        self.text = scrolledtext.ScrolledText(self.frame_der2,width = 10,height = 15, font = (font,15))
        self.text.grid(column = 0, pady = 10, padx = 50)
        texto, mastexto , camino = amplitud.raiz(self.recorrido)    # nos ingresa directamente el recorrido
        camino_ampli = texto , mastexto   # nos ingresa directamente el recorrido
        self.text.insert(tkinter.INSERT, camino_ampli) # nos imprime el recorrido 
        self.text.configure(state ='disabled',bg=background,fg=blanco,bd=0)

        self.iniciarGUI()

    def iniciarGUI(self):

        self.root_secundaria = Toplevel()
        self.offset = 30
        board = Board(self.root_secundaria, self.recorrido, self.cami)
        self.root_secundaria.title("Recorrido del Mapa")
        self.root_secundaria.resizable(0,0)
        self.root_secundaria.iconbitmap("Images/ia.ico")
                            
        x = board.getBoardWidth() + self.offset
        y = board.getBoardHeight() + 2 * self.offset

        self.root_secundaria.geometry(str(x) + 'x' + str(y))


gui =GUIinicio()
