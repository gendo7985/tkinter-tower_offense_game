from .baseTower import baseTower


class Tower2(baseTower):
    def __init__(self, parent, canvas, pos):
        baseTower.__init__(self, canvas, pos)
        self.parent = parent
        self.damage = 5
        self.cooltime = 0.2
        self.range = 500
        self.maxHP = 300
        self.HP = self.maxHP
        self.color = "purple"
        self.id = canvas.create_rectangle(
            self.x - 15, self.y - 15, self.x + 15, self.y + 15, fill=self.color
        )
        self.enemies = []
        self.attack()

    def update(self):
        pass

    def attack(self):  # tower hit unit
        self.canvas.after(int(1000 * self.cooltime), self.attack)
        self.nearEnemy()
        for unit in self.enemies:
            if unit in self.canvas.unitList:
                unit.unit.attacked(self.damage)

    def nearEnemy(self):
        if self.canvas.unitList:
            self.enemies = []
            for i in range(len(self.canvas.unitList)):
                unit = self.canvas.unitList[i].unit
                if self.distance(unit) < self.range:
                    self.enemies.append(unit.parent)