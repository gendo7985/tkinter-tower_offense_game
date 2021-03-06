from tkinter import PhotoImage
from .baseUnit import baseUnit


class Unit4(baseUnit):
    def __init__(self, parent, canvas, road):
        baseUnit.__init__(self, canvas, road)
        self.parent = parent
        self.damage = 10
        self.cooltime = 0.5
        self.range = 200
        self.maxHP = int(250 * self.canvas.parent.upgradeList[1])
        self.HP = self.maxHP
        self.speed = 3
        self.image = PhotoImage(file="./src/unit4.png")
        self.canvas.itemconfig(self.id, image=self.image)