def dist(p1, p2):
    return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5


class baseUnit:
    def __init__(self, canvas, road):
        self.canvas = canvas
        self.inBattle = False
        self.road = []
        for i in range(0, len(road), 2):
            self.road.append((road[i], road[i + 1]))
        self.id = self.canvas.create_oval(-15, 465, 15, 435)
        self.hpbarBackground = canvas.create_rectangle(-15, 430, 15, 420, fill="gray")
        self.hpbar = canvas.create_rectangle(-14, 429, 14, 421, fill="red")

    def update(self):
        if not self.inBattle:
            enemy = self.nearEnemy()
            if enemy != None:
                self.attack(self.canvas.towerList[enemy])
            else:
                dx, dy = self.nextPosition()
                self.canvas.move(self.id, dx, dy)
                self.canvas.move(self.hpbar, dx, dy)
                self.canvas.move(self.hpbarBackground, dx, dy)

    def nextPosition(self):
        if len(self.road) == 1:
            return (0, 0)
        (x1, y1, x2, y2) = self.canvas.coords(self.id)
        _x, _y = (x1 + x2) / 2, (y1 + y2) / 2  # center
        x, y, length = _x, _y, self.speed * self.canvas.parent.upgradeList[2]  # speedRate
        if dist((_x, _y), self.road[1]) < length:  # corner of road
            length -= dist((_x, _y), self.road[1])
            x, y = self.road[1]
            self.road.pop(0)
            if len(self.road) == 1:
                return (x - _x, y - _y)
        xvec = self.road[1][0] - self.road[0][0]
        yvec = self.road[1][1] - self.road[0][1]
        mag = (xvec ** 2 + yvec ** 2) ** 0.5
        if xvec != 0:  # not vertical
            x += xvec * length / mag  # x_1 = x_0 + dx
            y = yvec / xvec * (x - self.road[0][0]) + self.road[0][1]  # correction
        else:  # vertical
            y += yvec * length / mag
            x = xvec / yvec * (y - self.road[0][1]) + self.road[0][0]
        return (x - _x, y - _y)

    def attacked(self, damage):
        if self.HP <= damage:
            self.HP = 0
            self.canvas.delete(self.id)
            self.canvas.delete(self.hpbar)
            self.canvas.delete(self.hpbarBackground)
            self.inBattle = False
            del self.canvas.unitList[self.canvas.unitList.index(self.parent)]
        else:
            self.HP -= damage
            (x1, y1, x2, y2) = self.canvas.coords(self.hpbar)
            x2 = x1 + self.HP / self.maxHP * 28
            self.canvas.coords(self.hpbar, x1, y1, x2, y2)

    def attack(self, tower):
        if tower in self.canvas.towerList and self.HP > 0 and self.inBattle:
            tower.tower.attacked(int(self.damage * self.canvas.parent.upgradeList[0]))
            self.canvas.after(int(1000 * self.cooltime), lambda: self.attack(tower))
        else:
            self.inBattle = False

    def distance(self, other):
        x1, y1, x2, y2 = self.canvas.coords(self.id)
        z1, w1, z2, w2 = other.canvas.coords(other.id)
        return 0.5 * ((x1 + x2 - z1 - z2) ** 2 + (y1 + y2 - w1 - w2) ** 2) ** 0.5

    def nearEnemy(self):
        if self.canvas.towerList:
            dist = [-1, self.range]
            for i in range(len(self.canvas.towerList)):
                unit = self.canvas.towerList[i].tower
                newdist = self.distance(unit)
                if newdist < dist[1]:
                    dist[1] = newdist
                    dist[0] = i
            if dist[0] != -1:
                self.inBattle = True
                return dist[0]
