from .baseUnit import baseUnit


class Unit1(baseUnit):
    def __init__(self, parent, canvas):
        baseUnit.__init__(self, canvas)
        self.parent = parent
        self.damage = 5
        self.cooltime = 1
        self.range = 200
        self.maxHP = int(50 * self.canvas.parent.upgradeList[1])
        self.HP = self.maxHP
        self.speed = 3
        self.color = "red"
        self.id = self.canvas.create_oval(-15, 465, 15, 435, fill=self.color)