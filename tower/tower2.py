from .baseTower import baseTower


class Tower2(baseTower):
    def __init__(self, parent, canvas, pos):
        self.parent = parent
        self.damage = 10
        self.cooltime = 0.5
        self.range = 500
        self.maxHP = 300
        self.HP = self.maxHP
        self.color = "purple"
        baseTower.__init__(self, canvas, pos)
        self.id = canvas.create_rectangle(
            self.x - 15, self.y - 15, self.x + 15, self.y + 15, fill=self.color
        )

    def nearEnemy(self):
        if self.parent in self.canvas.towerList:
            for unit in self.canvas.unitList:
                if unit.unit not in self.enemies:
                    if self.distance(unit.unit) < self.range:
                        self.inBattle = True
                        self.enemies.append(unit.unit)