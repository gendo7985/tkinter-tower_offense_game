from tkinter import PhotoImage
from .baseTower import baseTower


class Tower2(baseTower):
    def __init__(self, parent, canvas, pos):
        self.parent = parent
        self.damage = 8
        self.cooltime = 0.5
        self.range = 300
        self.maxHP = 500
        self.HP = self.maxHP
        baseTower.__init__(self, canvas, pos)
        self.image = PhotoImage(file="./src/tower2.png")
        self.id = canvas.create_image(self.x, self.y, image=self.image)

    def nearEnemy(self):
        if self.parent in self.canvas.towerList:
            for unit in self.canvas.unitList:
                if unit.unit not in self.enemies:
                    if self.distance(unit.unit) < self.range:
                        self.inBattle = True
                        self.enemies.append(unit.unit)