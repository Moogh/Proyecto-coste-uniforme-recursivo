from PIL import Image, ImageTk

class Meta:
    def __init__(self,x,y):
        self.x = x
        self.y=y
        icon = Image.open('Images/muriel.png')
        self.img = ImageTk.PhotoImage(icon)

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getImg(self):
        return self.img
