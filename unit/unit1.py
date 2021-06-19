from .baseUnit import baseUnit


class Unit1(baseUnit):
    def __init__(self, parent, canvas, road):
        baseUnit.__init__(self, canvas, road)
        self.parent = parent
        self.damage = 5
        self.cooltime = 1
        self.range = 200
        self.maxHP = int(50 * self.canvas.parent.upgradeList[1])
        self.HP = self.maxHP
        self.speed = 3
        self.color = "red"
        self.canvas.itemconfig(self.id, fill=self.color)