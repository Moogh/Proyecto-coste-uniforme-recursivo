
import heapq

class Costo:

    def costo(self, arbol):
        inicio_x = 0
        inicio_y = 0

        fin_x = 0
        fin_y = 0
        filas = len(arbol)
        columnas = len(arbol[0])

        recorrido = []

        for i in range(len(arbol)):
            for j in range(len(arbol[i])):
                if (arbol[i][j] == "@"):
                    inicio_x = i
                    inicio_y = j

        for i in range(len(arbol)):
            for j in range(len(arbol[i])):
                if (arbol[i][j] == "$"):
                    fin_x = i
                    fin_y = j

        #iniciamos la lista a acumular costos
        listaARecorrer = [(0, inicio_x,inicio_y, [])]
        #iniciamos la lista de recorridos
        explorado = set()
        # Iniciamos el contador de nodos creados
        contador = 1

        while listaARecorrer:
            (costo, fila, colm, recorrido) = heapq.heappop(listaARecorrer)

            if (fila, colm) in explorado:
                continue

            recorrido = recorrido + [(fila, colm)]

            if arbol[fila][colm] == arbol[fin_x][fin_y]:
                
                return recorrido, contador
            

            explorado.add((fila, colm))
            nodosV = nodosVecinos(arbol,fila, colm, filas, columnas)
            for (f, c, w) in nodosV:
                if (f, c) not in explorado and arbol[f][c] != "#":
                    heapq.heappush(listaARecorrer, (costo + w, f, c, recorrido))
                    contador += 1

        return recorrido, contador

def nodosVecinos(arbol, fila, colm, filas, columnas):
    nodos = []
    if fila > 1 and arbol[fila][colm] != "#" :  #arriba
        if (arbol[fila-1][colm]== "%"):
            nodos.append((fila-1, colm, -2))
        elif (arbol[fila-1][colm]== "&"):
            nodos.append((fila-1, colm, 3))
        elif (arbol[fila-1][colm]== " "):
            nodos.append((fila-1, colm, 1))

    if fila < filas-2 and arbol[fila][colm] != "#" : # abajo
        if (arbol[fila+1][colm]== "%"):
            nodos.append((fila+1, colm, -2))
        elif (arbol[fila+1][colm]== "&"):
            nodos.append((fila+1, colm, 3))
        elif(arbol[fila+1][colm]== " "):
            nodos.append((fila+1, colm, 1))


    if colm > 1 and arbol[fila][colm] != "#": #izquierda
        if (arbol[fila][colm-1] == "%"):
                nodos.append((fila, colm-1, -2))
        elif (arbol[fila][colm-1]== "&"):
                nodos.append((fila, colm-1, 3))
        elif (arbol[fila][colm-1]== " "):
                nodos.append((fila, colm-1, 1))
    

    if colm < columnas-2 and arbol[fila][colm] != "#" : #derecha
        if (arbol[fila][colm+1] == "%"):
                nodos.append((fila, colm+1, -2))
        elif (arbol[fila][colm+1]== "&"):
                nodos.append((fila, colm+1, 3))
        elif (arbol[fila][colm+1]== " "):
                nodos.append((fila, colm+1, 1))

    return nodos