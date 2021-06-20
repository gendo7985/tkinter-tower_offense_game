from tkinter import PhotoImage
from .baseUnit import baseUnit


class Unit2(baseUnit):
    def __init__(self, parent, canvas, road):
        baseUnit.__init__(self, canvas, road)
        self.parent = parent
        self.damage = 0
        self.cooltime = 0
        self.maxHP = int(300 * self.canvas.parent.upgradeList[1])
        self.HP = self.maxHP
        self.speed = 2
        self.image = PhotoImage(file="./src/unit2.png")
        self.canvas.itemconfig(self.id, image=self.image)

    def update(self):  # tanker cannot attack tower
        if self.id in self.canvas.find_all():
            dx, dy = self.nextPosition()
            self.canvas.move(self.id, dx, dy)
            self.canvas.move(self.hpbar, dx, dy)
            self.canvas.move(self.hpbarBackground, dx, dy)