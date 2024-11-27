from tkinter import *


class Bullet:
    def __init__(self, x, y, direction, canvas):
        self.canvas = canvas
        self.direction = direction
        self.bulletEastImage = PhotoImage(
            file="T:\VSCode\Python\TankGame/bulletEast.png")
        self.bulletWestImage = PhotoImage(
            file="T:\VSCode\Python\TankGame/bulletWest.png")
        self.bulletNorthImage = PhotoImage(
            file="T:\VSCode\Python\TankGame/bulletNorth.png")
        self.bulletSouthImage = PhotoImage(
            file="T:\VSCode\Python\TankGame/bulletSouth.png")

        self.bullet = canvas.create_image(x, y, image=self.bulletEastImage)
        self.removed = False

    def hitTarget(self):
        self.removed = True

    def getLocation(self):
        return self.canvas.coords(self.bullet)

    def setDirection(self, direction):
        self.direction = direction
        if (self.direction == "n"):
            self.canvas.itemconfig(self.bullet, image=self.bulletNorthImage)
        if (self.direction == "e"):
            self.canvas.itemconfig(self.bullet, image=self.bulletEastImage)
        if (self.direction == "s"):
            self.canvas.itemconfig(self.bullet, image=self.bulletSouthImage)
        if (self.direction == "w"):
            self.canvas.itemconfig(self.bullet, image=self.bulletWestImage)

    def move(self):
        if (self.direction == "n"):
            self.canvas.move(self.bullet, 0, -15)
        if (self.direction == "e"):
            self.canvas.move(self.bullet, 15, 0)
        if (self.direction == "s"):
            self.canvas.move(self.bullet, 0, 15)
        if (self.direction == "w"):
            self.canvas.move(self.bullet, -15, 0)

    def removeBullet(self):
        coordinates = self.canvas.coords(self.bullet)
        if self.removed:
            return True
        if (coordinates[0] >= self.canvas.winfo_width()+self.bulletEastImage.width() or coordinates[0] < 0-self.bulletWestImage.width()):
            self.removed = True
            return True
        if (coordinates[1] >= self.canvas.winfo_height()+self.bulletNorthImage.height() or coordinates[1] < 0-self.bulletSouthImage.height()):
            self.removed = True
            return True
        return False
