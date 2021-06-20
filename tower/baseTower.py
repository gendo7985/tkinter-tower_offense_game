class baseTower:
    def __init__(self, canvas, pos):
        self.canvas = canvas
        self.inBattle = False
        self.respawn = True
        self.x, self.y = pos[0], pos[1]
        self.hpbarBackground = canvas.create_rectangle(
            self.x - 15, self.y - 20, self.x + 15, self.y - 30, fill="gray"
        )
        self.hpbar = canvas.create_rectangle(
            self.x - 14, self.y - 21, self.x + 14, self.y - 29, fill="red"
        )
        self.enemies = []
        self.attack()

    def const(self):  # difficulty constant
        difficulty = self.canvas.parent.difficulty.get()[:2]
        if difficulty == "쉬움":
            return 3
        elif difficulty == "보통":
            return 2
        else:
            return 1.5

    def attacked(self, damage):  # tower get damage
        moneyFactor = self.canvas.parent.upgradeList[3] + 1  # mps
        if self.HP <= damage:  # tower broken
            self.HP = 0
            self.canvas.parent.money += (
                self.maxHP * self.const() / 50 * moneyFactor / self.canvas.stage
            )
            self.canvas.itemconfig(self.hpbar, fill="#333333")
            self.inBattle = False
            self.canvas.towerList.remove(self.parent)
            self.respawning()  # ready for respawn
            self.kill = self.canvas.create_text(
                self.x,
                self.y,
                text="$" + str(int(self.maxHP / self.const())),
            )
            self.canvas.tag_bind(self.kill, "<Button-1>", self.mouseClick)  # kill permanently

        else:  # tower alived
            self.HP -= damage
            self.canvas.parent.money += (
                damage * (self.const() - 1) / 5 * moneyFactor / self.canvas.stage
            )
            (x1, y1, x2, y2) = self.canvas.coords(self.hpbar)
            x2 = x1 + self.HP / self.maxHP * 28
            self.canvas.coords(self.hpbar, x1, y1, x2, y2)

    def attack(self):  # tower hit unit
        self.nearEnemy()
        if self.inBattle:
            for unit in self.enemies:
                if unit.parent in self.canvas.unitList and self.distance(unit) < self.range:
                    unit.attacked(self.damage)
                else:
                    self.enemies.remove(unit)
                    self.inBattle = self.enemies
        self.canvas.after(int(1000 * self.cooltime), self.attack)

    def distance(self, other):
        x1, y1 = self.canvas.coords(self.id)
        x2, y2 = other.canvas.coords(other.id)
        return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

    def nearEnemy(self):
        if (not self.enemies) and self.canvas.unitList and self.parent in self.canvas.towerList:
            nearest, dist = None, self.range
            for unit in self.canvas.unitList:
                newdist = self.distance(unit.unit)
                if newdist < dist:
                    dist = newdist
                    nearest = unit.unit
            if nearest != None:
                self.inBattle = True
                self.enemies.append(nearest)

    def respawning(self):
        if self.respawn and self.id in self.canvas.find_all():
            if self.HP < self.maxHP:  # respawning
                self.HP += self.maxHP * 0.05
                (x1, y1, x2, y2) = self.canvas.coords(self.hpbar)
                x2 = x1 + self.HP / self.maxHP * 28
                self.canvas.coords(self.hpbar, x1, y1, x2, y2)
                self.canvas.after(500, self.respawning)
            else:  # respawned
                self.HP = self.maxHP
                self.canvas.itemconfig(self.hpbar, fill="red")
                self.canvas.towerList.append(self.parent)
                self.canvas.tag_unbind(self.kill, "<Button-1>")
                self.canvas.delete(self.kill)
        else:
            self.canvas.delete(self.id)
            self.canvas.delete(self.hpbar)
            self.canvas.delete(self.hpbarBackground)

    def mouseClick(self, e):
        if self.canvas.parent.money.get() >= self.maxHP / self.const():
            self.canvas.parent.money -= self.maxHP / self.const()
            self.canvas.delete(self.kill)
            self.respawn = False
