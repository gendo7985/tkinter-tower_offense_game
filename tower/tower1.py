from tkinter import PhotoImage
from .baseTower import baseTower


class Tower1(baseTower):
    def __init__(self, parent, canvas, pos):
        self.parent = parent
        self.damage = 10 * canvas.stage
        self.cooltime = 1
        self.range = 300
        self.maxHP = 300 * canvas.stage
        self.HP = self.maxHP
        baseTower.__init__(self, canvas, pos)
        self.image = PhotoImage(file="./src/tower1.png")
        self.id = canvas.create_image(self.x, self.y, image=self.image)
