from .baseUnit import baseUnit


class Unit1(baseUnit):
    def __init__(self, parent):
        baseUnit.__init__(self)
        self.parent = parent
        self.attack = 5
        self.attackRate = 2
        self.HP = 50
        self.speed = 5
        self.color = "red"
        self.id = self.parent.create_oval(-25, 475, 25, 425, fill=self.color)

    def update(self):
        dx, dy = self.nextPosition()
        self.parent.move(self.id, dx, dy)