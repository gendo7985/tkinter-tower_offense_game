from tkinter import PhotoImage
from .baseTower import baseTower


class Nexus(baseTower):
    def __init__(self, parent, canvas, pos):
        self.parent = parent
        self.damage = 0
        self.cooltime = 1
        self.range = 0
        self.maxHP = 3000 * canvas.stage
        self.HP = self.maxHP
        baseTower.__init__(self, canvas, pos)
        self.image = PhotoImage(file="./src/nexus.png")
        self.id = canvas.create_image(self.x, self.y, image=self.image)

    def attack(self):
        pass

    def attacked(self, damage):  # tower get damage
        if self.HP <= damage:  # tower broken
            self.canvas.unitList = []
            self.canvas.towerList = []
            self.canvas.after(1000, self.clear())

        else:  # tower alived
            self.HP -= damage
            (x1, y1, x2, y2) = self.canvas.coords(self.hpbar)
            x2 = x1 + self.HP / self.maxHP * 28
            self.canvas.coords(self.hpbar, x1, y1, x2, y2)

    def clear(self):
        self.canvas.delete("all")
        self.canvas.create_text(
            600, 300, text="CLEAR", fill="white", font=("Arial", 100, "bold italic")
        )
        self.canvas.after(2000, self.canvas.nextStage)
