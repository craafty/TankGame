from tkinter import *
import time
import Target
import Bullet


class Tank():
    def __init__(self):
        self.tk = Tk()
        self.tk.title("Tank Game")
        self.tk.resizable(0, 0)

        self.frame = Frame(self.tk)
        self.frame.grid(row=0, column=0)

        self.backgroundImage = PhotoImage(
            file="T:\VSCode\Python\TankGame/background.png")

        self.WIDTH = self.backgroundImage.width()
        self.HEIGHT = self.backgroundImage.height()

        self.canvas = Canvas(self.tk, width=self.WIDTH, height=self.HEIGHT)
        self.canvas.grid(row=0, column=0)
        self.background = self.canvas.create_image(
            0, 0, image=self.backgroundImage, anchor=NW)

        self.tankEastImage = PhotoImage(
            file="T:\VSCode\Python\TankGame/tankEast.png")
        self.tankSouthImage = PhotoImage(
            file="T:\VSCode\Python\TankGame/tankSouth.png")
        self.tankNorthImage = PhotoImage(
            file="T:\VSCode\Python\TankGame/tankNorth.png")
        self.tankWestImage = PhotoImage(
            file="T:\VSCode\Python\TankGame/tankWest.png")

        self.tank = self.canvas.create_image(
            int(self.WIDTH/2), int(self.HEIGHT/2), image=self.tankEastImage)

        self.canvas.bind_all('<d>', self.east)
        self.canvas.bind_all('<s>', self.south)
        self.canvas.bind_all('<w>', self.north)
        self.canvas.bind_all('<a>', self.west)
        self.canvas.bind_all('<space>', self.shoot)

        self.tk.protocol("WM_DELETE_WINDOW", self.endProgram)
        self.stop = False
        self.direction = "e"
        self.targets = []
        self.score = 0

        self.scoreLabel = self.canvas.create_text(
            int(self.WIDTH/2), 30, text="Score: " + str(self.score), font=("Arial", 40, "bold"), fill="red")
        self.canvas.lift(self.scoreLabel)

        self.bullets = []
        for _ in range(10):
            self.targets.append(Target.Target(self.canvas))

    def shoot(self, event):
        location = self.canvas.coords(self.tank)
        self.bullets.append(Bullet.Bullet(
            location[0], location[1], self.direction, self.canvas))
        self.bullets[-1].setDirection(self.direction)

    def north(self, event):
        self.canvas.itemconfig(self.tank, image=self.tankNorthImage)
        self.direction = 'n'
        y = self.canvas.coords(self.tank)[1]
        if y > 0:
            self.canvas.move(self.tank, 0, -10)

    def south(self, event):
        self.canvas.itemconfig(self.tank, image=self.tankSouthImage)
        self.direction = 's'
        y = self.canvas.coords(self.tank)[1]
        if y < self.HEIGHT:
            self.canvas.move(self.tank, 0, 10)

    def west(self, event):
        self.canvas.itemconfig(self.tank, image=self.tankWestImage)
        self.direction = 'w'
        x = self.canvas.coords(self.tank)[0]
        if x > 0:
            self.canvas.move(self.tank, -10, 0)

    def east(self, event):
        self.canvas.itemconfig(self.tank, image=self.tankEastImage)
        self.direction = 'e'
        x = self.canvas.coords(self.tank)[0]
        if x < self.WIDTH:
            self.canvas.move(self.tank, 10, 0)

    def endProgram(self):
        self.stop = True

    def distance(self, bulletX, bulletY, targetX, targetY):
        return ((targetX - bulletX)**2 + (targetY - bulletY)**2)**0.5

    def move(self):
        for target in self.targets:
            target.move()
        for bullet in self.bullets:
            bullet.move()
        for target in self.targets:
            for bullet in self.bullets:
                targetLoc = target.getLocation()
                bulletLoc = bullet.getLocation()
                if self.distance(bulletLoc[0], bulletLoc[1], targetLoc[0], targetLoc[1]) < 50:
                    bullet.hitTarget()
                    target.explode()

                if bullet.removeBullet():
                    self.bullets.remove(bullet)
                    break

            if target.getRemoved():
                self.targets.remove(target)
                self.targets.append(Target.Target(self.canvas))
                self.score += 1
                self.canvas.itemconfig(
                    self.scoreLabel, text="Score: " + str(self.score))
                break

    def main(self):
        while True:
            time.sleep(0.01)
            self.move()
            self.tk.update()
            self.tk.update_idletasks()
            if self.stop == True:
                self.tk.destroy()
                break


tnk = Tank()
tnk.main()
