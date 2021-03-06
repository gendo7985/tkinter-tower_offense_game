from tkinter import PhotoImage
from .baseUnit import baseUnit


class Unit5(baseUnit):
    def __init__(self, parent, canvas, road):
        baseUnit.__init__(self, canvas, road)
        self.parent = parent
        self.damage = 250
        self.cooltime = 5
        self.range = 150
        self.maxHP = int(200 * self.canvas.parent.upgradeList[1])
        self.HP = self.maxHP
        self.speed = 1
        self.image = PhotoImage(file="./src/unit5.png")
        self.canvas.itemconfig(self.id, image=self.image)