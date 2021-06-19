from .baseUnit import baseUnit


class Unit3(baseUnit):  # Bomb unit
    def __init__(self, parent, canvas, road):
        baseUnit.__init__(self, canvas, road)
        self.parent = parent
        self.damage = 300
        self.cooltime = 0
        self.maxHP = int(80 * self.canvas.parent.upgradeList[1])
        self.HP = self.maxHP
        self.speed = 5
        self.color = "pink"
        self.canvas.itemconfig(self.id, fill=self.color)

    def update(self):  # bomb unit attack only nexus tower
        dx, dy = self.nextPosition()
        self.canvas.move(self.id, dx, dy)
        self.canvas.move(self.hpbar, dx, dy)
        self.canvas.move(self.hpbarBackground, dx, dy)
        for tower in self.canvas.towerList:
            if self.distance(tower) < 15:
                tower.attacked(self.damage)
                self.attacked(self.maxHP)  # suicide
