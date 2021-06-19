from .baseUnit import baseUnit


class Unit2(baseUnit):
    def __init__(self, parent, canvas, road):
        baseUnit.__init__(self, canvas, road)
        self.parent = parent
        self.damage = 0
        self.cooltime = 0
        self.maxHP = 300
        self.HP = self.maxHP
        self.speed = 2
        self.color = "blue"
        self.canvas.itemconfig(self.id, fill=self.color)

    def update(self):
        dx, dy = self.nextPosition()
        self.canvas.move(self.id, dx, dy)
        self.canvas.move(self.hpbar, dx, dy)
        self.canvas.move(self.hpbarBackground, dx, dy)