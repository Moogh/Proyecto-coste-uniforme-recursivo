class Queue:

    # Inicializar queue
    def __init__(self, size=1000):
        self.q = [None] * size  # Lista  para almacenar elementos de queue
        self.capacity = size  # capacidad máxima de la queue
        self.front = 0  # front apunta al elemento frontal en la queue
        self.rear = -1  # La parte trasera que apunta al último elemento de la queue
        self.count = 0  # tamaño actual de la queue

    # Función para quitar la queue del elemento frontal
    def dequeue(self):
        # el desbordamiento de la queue
        if self.isEmpty():
            print('Queue Underflow!! Terminating process.')
            exit(-1)
        x = self.q[self.front]
        self.front = (self.front + 1) % self.capacity
        self.count = self.count - 1
        return x

    # Función para agregar un elemento a la queue
    def enqueue(self, value):
        # si hay desbordamiento de queue
        if self.isFull():
            print('Overflow!! Terminating process.')
            exit(-1)
        self.rear = (self.rear + 1) % self.capacity
        self.q[self.rear] = value
        self.count = self.count + 1

    # Función para devolver el elemento frontal de la queue
    def peek(self):
        if self.isEmpty():
            print('Queue UnderFlow!! Terminating process.')
            exit(-1)
        return self.q[self.front]

    # Función para devolver el tamaño de la queue
    def size(self):
        return self.count

    # Función para comprobar si la queue está vacía o no
    def isEmpty(self):
        return self.size() == 0

    # Función para comprobar si la queue está llena o no
    def isFull(self):
        return self.size() == self.capacity