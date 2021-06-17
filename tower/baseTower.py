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

    def update(self):
        if not self.inBattle:
            enemy = self.nearEnemy()
            if enemy != None:
                self.attack(self.canvas.unitList[enemy])

    def const(self):  # difficulty constant
        difficulty = self.canvas.parent.difficulty.get()
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
            self.canvas.parent.money += self.maxHP * self.const() / 50 * moneyFactor
            self.canvas.itemconfig(self.id, fill="gray")
            self.canvas.itemconfig(self.hpbar, fill="#333333")
            self.inBattle = False
            self.canvas.towerList.remove(self.parent)
            self.respawning()
            self.kill = self.canvas.create_text(
                self.x, self.y, text="$" + str(int(self.maxHP / self.const()))
            )
            self.canvas.tag_bind(self.kill, "<Button-1>", self.mouseClick)

        else:  # tower alived
            self.HP -= damage
            self.canvas.parent.money += damage * (self.const() - 1) / 5 * moneyFactor
            (x1, y1, x2, y2) = self.canvas.coords(self.hpbar)
            x2 = x1 + self.HP / self.maxHP * 28
            self.canvas.coords(self.hpbar, x1, y1, x2, y2)

    def attack(self, unit):  # tower hit unit
        if unit in self.canvas.unitList and self.inBattle and self.distance(unit.unit) < self.range:
            unit.unit.attacked(self.damage)
            self.canvas.after(int(1000 * self.cooltime), lambda: self.attack(unit))
        else:
            self.inBattle = False

    def distance(self, other):
        x1, y1, x2, y2 = self.canvas.coords(self.id)
        z1, w1, z2, w2 = other.canvas.coords(other.id)
        return 0.5 * ((x1 + x2 - z1 - z2) ** 2 + (y1 + y2 - w1 - w2) ** 2) ** 0.5

    def nearEnemy(self):
        if self.canvas.unitList:
            dist = [-1, self.range]
            for i in range(len(self.canvas.unitList)):
                unit = self.canvas.unitList[i].unit
                newdist = self.distance(unit)
                if newdist < dist[1]:
                    dist[1] = newdist
                    dist[0] = i
            if dist[0] != -1:
                self.inBattle = True
                return dist[0]

    def respawning(self):
        if self.respawn:
            if self.HP < self.maxHP:  # respawning
                self.HP += self.maxHP * 0.05
                (x1, y1, x2, y2) = self.canvas.coords(self.hpbar)
                x2 = x1 + self.HP / self.maxHP * 28
                self.canvas.coords(self.hpbar, x1, y1, x2, y2)
                self.canvas.after(500, self.respawning)
            else:  # respawned
                self.HP = self.maxHP
                self.canvas.itemconfig(self.id, fill=self.color)
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
