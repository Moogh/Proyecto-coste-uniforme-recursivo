from PIL import Image, ImageTk
class Gato:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        icon = Image.open('Images/gato.png')
        self.imagen = ImageTk.PhotoImage(icon)

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getImg(self):
        return self.imagen