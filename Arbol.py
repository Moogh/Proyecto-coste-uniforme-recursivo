
class Arbol:
    #posicion -> punto
    #recorridos -> vector
    #derrota, victoria, muro -> boolean
    def __int__(self, posicion, recorrido, victoria):
        self.posicion = posicion
        self.recorrido = recorrido
        self.victoria = victoria
        self.visitadoInicio = False
        self.visitadoFin = False
        self.padre = None

    def getPosicion(self):
        return self.posicion

    def getRecorrido(self):
        return self.recorrido

    def getVictoria(self):
        return self.victoria