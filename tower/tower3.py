from tkinter import PhotoImage
from .baseTower import baseTower


class Tower3(baseTower):
    def __init__(self, parent, canvas, pos):
        self.parent = parent
        self.damage = 20
        self.cooltime = 0.5
        self.range = 300
        self.maxHP = 1000
        self.HP = self.maxHP
        baseTower.__init__(self, canvas, pos)
        self.image = PhotoImage(file="./src/tower3.png")
        self.id = canvas.create_image(self.x, self.y, image=self.image)
