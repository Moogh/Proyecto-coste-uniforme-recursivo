from Arbol import Arbol
from Punto import Punto
from Queue import Queue

class Amplitud:

    
    # iniciacion base la busqueda en el mapa

    def raiz(self, juego):

        mostrar = ""
        x = 0
        y = 0
        recorrido = []
        # buscamos donde inicia el juego con el caracter que preseleccionamos
        for i in range(len(juego)):
            for j in range(len(juego[i])):
                if (juego[i][j] == "@"):
                    x = i
                    y = j
        # inicamos el punto de partida 
        punto = Punto()
        punto.__int__(x, y)
        # inicaimos la contruccion del arbol
        arbol = Arbol()
        arbol.__int__(punto, recorrido, False)
        # iniciamos el camino a recorrer y contar los nodos lo guardamos en camino
        # y el contador de veces accedido al campo para buscar
        global cambio 

        cambio  =+ 1

        camino = buscar(juego, arbol)
        #mostramos en pantalla el camino recorrido y el numero de nodos creados
        for i in range(len(camino)):
            mostrar = str(mostrar) + str(camino[i].getX()) + "," + str(camino[i].getY()) + "\n"
        texto = 'Nodos: ' + str(nodos) + '\n'
        return texto, mostrar , camino
    
    # empezamos a buscar con la raiz inicial y a crear la busqueda
def buscar(estadoJuego, raiz):

    global nodos
    nodos = 0
    salida = []
    puntoActual = raiz
    
    
    
    
    busqueda = Queue()
    busqueda.enqueue(puntoActual)

    while(not busqueda.isEmpty() and not puntoActual.getVictoria()):

        if not cambio % 2 == 0:
            buscarOrden = True
        else:
            buscarOrden = False

        busqueda.dequeue()
            
        if (buscarOrden):
            # arriba
            if (puntoActual.getPosicion().getX() > 0 and not (estadoJuego[puntoActual.getPosicion().getX()-1][puntoActual.getPosicion().getY()] == "#")):
                nuevoPunto = Punto()
                nuevoPunto.__int__(puntoActual.getPosicion().getX() - 1, puntoActual.getPosicion().getY())
                if (not buscarPunto(puntoActual.getRecorrido(), nuevoPunto)):
                    busqueda.enqueue(generarHijo(nuevoPunto, puntoActual, estadoJuego))
                        
        
                # abajo
            if (puntoActual.getPosicion().getX() < len(estadoJuego[0]) - 1 and not (estadoJuego[puntoActual.getPosicion().getX()+1][puntoActual.getPosicion().getY()] == "#")):
                nuevoPunto = Punto()
                nuevoPunto.__int__(puntoActual.getPosicion().getX() + 1, puntoActual.getPosicion().getY())
                if (not buscarPunto(puntoActual.getRecorrido(), nuevoPunto)):
                    busqueda.enqueue(generarHijo(nuevoPunto, puntoActual, estadoJuego))


                #izquierda
            if(puntoActual.getPosicion().getY() > 0 and not (estadoJuego[puntoActual.getPosicion().getX()][puntoActual.getPosicion().getY()-1] == "#")):
                nuevoPunto = Punto()
                nuevoPunto.__int__(puntoActual.getPosicion().getX(), puntoActual.getPosicion().getY() - 1)
                if(not buscarPunto(puntoActual.getRecorrido(), nuevoPunto)):
                    busqueda.enqueue(generarHijo(nuevoPunto, puntoActual, estadoJuego))


                # derecha
            if (puntoActual.getPosicion().getY() < len(estadoJuego[0]) - 1 and not (estadoJuego[puntoActual.getPosicion().getX()][puntoActual.getPosicion().getY()+1] == "#")):
                nuevoPunto = Punto()
                nuevoPunto.__int__(puntoActual.getPosicion().getX(), puntoActual.getPosicion().getY() + 1)
                if (not buscarPunto(puntoActual.getRecorrido(), nuevoPunto)):
                    busqueda.enqueue(generarHijo(nuevoPunto, puntoActual, estadoJuego))

        else:

            # arriba
            if (puntoActual.getPosicion().getX() > 0 and not (estadoJuego[puntoActual.getPosicion().getX()-1][puntoActual.getPosicion().getY()] == "#")):
                nuevoPunto = Punto()
                nuevoPunto.__int__(puntoActual.getPosicion().getX() - 1, puntoActual.getPosicion().getY())
                if (not buscarPunto(puntoActual.getRecorrido(), nuevoPunto)):
                    busqueda.enqueue(generarHijo(nuevoPunto, puntoActual, estadoJuego))
            
                # abajo
            if (puntoActual.getPosicion().getX() < len(estadoJuego[0]) - 1 and not (estadoJuego[puntoActual.getPosicion().getX()+1][puntoActual.getPosicion().getY()] == "#")):
                nuevoPunto = Punto()
                nuevoPunto.__int__(puntoActual.getPosicion().getX() + 1, puntoActual.getPosicion().getY())
                if (not buscarPunto(puntoActual.getRecorrido(), nuevoPunto)):
                    busqueda.enqueue(generarHijo(nuevoPunto, puntoActual, estadoJuego))


                # derecha
            if (puntoActual.getPosicion().getY() < len(estadoJuego[0]) - 1 and not (estadoJuego[puntoActual.getPosicion().getX()][puntoActual.getPosicion().getY()+1] == "#")):
                nuevoPunto = Punto()
                nuevoPunto.__int__(puntoActual.getPosicion().getX(), puntoActual.getPosicion().getY() + 1)
                if (not buscarPunto(puntoActual.getRecorrido(), nuevoPunto)):
                    busqueda.enqueue(generarHijo(nuevoPunto, puntoActual, estadoJuego))


                #izquierda
            if(puntoActual.getPosicion().getY() > 0 and not (estadoJuego[puntoActual.getPosicion().getX()][puntoActual.getPosicion().getY()-1] == "#")):
                nuevoPunto = Punto()
                nuevoPunto.__int__(puntoActual.getPosicion().getX(), puntoActual.getPosicion().getY() - 1)
                if(not buscarPunto(puntoActual.getRecorrido(), nuevoPunto)):
                    busqueda.enqueue(generarHijo(nuevoPunto, puntoActual, estadoJuego))

        nodos +=1
        puntoActual = busqueda.peek()

    if(not busqueda.isEmpty()):
        salida = busqueda.peek().getRecorrido()
        salida.append(busqueda.peek().getPosicion())
    else:
        ("No encontró la meta")

    return salida

def generarHijo(nuevoPunto, puntoActual, estadoActual):
    recorridoNuevo = []
    for x in range(len(puntoActual.getRecorrido())): # 0

        recorridoNuevo.append(puntoActual.getRecorrido()[x])

    recorridoNuevo.append(puntoActual.getPosicion())

    victoria = False

    if (estadoActual[nuevoPunto.getX()][nuevoPunto.getY()] == '$'):
        victoria = True

    nuevoHijo = Arbol()

    nuevoHijo.__int__(nuevoPunto,recorridoNuevo,victoria)
    return nuevoHijo

def buscarPunto(recorrido, punto):
    for x in range(len(recorrido)):
        if(recorrido[x].getX() == punto.getX() and recorrido[x].getY() == punto.getY()):
            return True
    return False