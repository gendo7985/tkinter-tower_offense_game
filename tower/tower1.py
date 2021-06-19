from tkinter import PhotoImage
from .baseTower import baseTower


class Tower1(baseTower):
    def __init__(self, parent, canvas, pos):
        self.parent = parent
        self.damage = 10
        self.cooltime = 1
        self.range = 300
        self.maxHP = 300
        self.HP = self.maxHP
        self.color = "yellow"
        # self.image = PhotoImage(file="./src/test.png")
        # self.id = canvas.create_image(self.x, self.y, image=self.image)
        baseTower.__init__(self, canvas, pos)
        self.id = canvas.create_rectangle(
            self.x - 15, self.y - 15, self.x + 15, self.y + 15, fill=self.color
        )
