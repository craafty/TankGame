from tkinter import *
import random
import time


class Target:
    def __init__(self, canvas):
        self.canvas = canvas
        self.targetImage = PhotoImage(
            file="T:\VSCode\Python\TankGame/target.png")
        self.target = canvas.create_image(
            random.randint(100, 900), random.randint(100, 600), image=self.targetImage, anchor=NW)

        self.explosions = []
        for i in range(6):
            self.explosions.append(PhotoImage(
                file="T:\VSCode\Python\TankGame/explosion"+str(i+1)+".png"))

        self.exploding = False
        self.removed = False

        if random.randint(0, 1) == 0:
            self.xVelocity = -1
        else:
            self.xVelocity = 1
        if random.randint(0, 1) == 0:
            self.yVelocity = -1
        else:
            self.yVelocity = 1

    def getLocation(self):
        return self.canvas.coords(self.target)

    def getRemoved(self):
        if self.removed:
            return True
        return False

    def move(self):
        if self.removed:
            return
        x, y = self.canvas.coords(self.target)
        if (x >= self.canvas.winfo_width()-self.targetImage.width() or x < 0):
            self.xVelocity *= -1
        if (y >= self.canvas.winfo_height()-self.targetImage.height() or y < 0):
            self.yVelocity *= -1
        self.canvas.move(self.target, self.xVelocity, self.yVelocity)

    def explode(self):
        x, y = self.canvas.coords(self.target)
        self.canvas.delete(self.target)
        self.removed = True

        for i in range(len(self.explosions)):
            explosion = self.canvas.create_image(
                x, y, image=self.explosions[i])
            self.canvas.update()
            self.canvas.after(30, self.canvas.delete(explosion))
            self.canvas.update()
