from tkinter import PhotoImage
from .baseUnit import baseUnit
from random import random


class Unit7(baseUnit):
    def __init__(self, parent, canvas, road):
        baseUnit.__init__(self, canvas, road)
        self.parent = parent
        self.damage = 50
        self.cooltime = 0.5
        self.range = 200
        self.maxHP = int(500 * self.canvas.parent.upgradeList[1])
        self.HP = self.maxHP
        self.speed = 1
        self.image = PhotoImage(file="./src/unit7.png")
        self.canvas.itemconfig(self.id, image=self.image)

    def attack(self, tower):  # unit attack tower
        if tower in self.canvas.towerList and self.HP > 0 and self.inBattle:  # prevent error
            tower.tower.attacked(int(self.damage * self.canvas.parent.upgradeList[0]))
            if random() < 0.1:
                tower.tower.attacked(int(self.damage * 10000))
            self.canvas.after(int(1000 * self.cooltime), lambda: self.attack(tower))
        else:  # if tower already dead
            self.inBattle = False  # don't fight anymore