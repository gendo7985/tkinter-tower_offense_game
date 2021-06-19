def dist(p1, p2):
    return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5


class baseUnit:  # inherit to unit1 ~ unit7
    def __init__(self, canvas, road):
        self.canvas = canvas
        self.inBattle = False  # if unit in battle, don't move and attack tower
        self.road = []  # unit follow this road
        for i in range(0, len(road), 2):
            self.road.append((road[i], road[i + 1]))

        # self image, hpbar
        self.x, self.y = self.road[0][0], self.road[0][1]  # initial position
        self.id = self.canvas.create_oval(self.x - 15, self.y - 15, self.x + 15, self.y + 15)
        self.hpbarBackground = canvas.create_rectangle(
            self.x - 15, self.y - 20, self.x + 15, self.y - 30, fill="gray"
        )
        self.hpbar = canvas.create_rectangle(
            self.x - 14, self.y - 21, self.x + 14, self.y - 29, fill="red"
        )

    def update(self):
        if not self.inBattle:  # if unit in battle:
            enemy = self.nearEnemy()  # search enemy tower
            if enemy != None:  # if there is enemy tower:
                self.attack(self.canvas.towerList[enemy])  # attack that tower
            else:  # if there is no enemy
                if self.id in self.canvas.find_all():  # prevent error
                    dx, dy = self.nextPosition()  # move forward
                    self.canvas.move(self.id, dx, dy)
                    self.canvas.move(self.hpbar, dx, dy)
                    self.canvas.move(self.hpbarBackground, dx, dy)

    def nextPosition(self):  # next position of unit
        if len(self.road) == 1:  # at the end of road:
            return (0, 0)  # don't move
        (x1, y1, x2, y2) = self.canvas.coords(self.id)
        _x, _y = (x1 + x2) / 2, (y1 + y2) / 2  # center of unit
        x, y, length = _x, _y, self.speed * self.canvas.parent.upgradeList[2]  # speedRate
        if dist((_x, _y), self.road[1]) < length:  # corner of road
            length -= dist((_x, _y), self.road[1])  # go through to corner
            x, y = self.road[1]
            self.road.pop(0)
            if len(self.road) == 1:  # end of the road
                return (x - _x, y - _y)
        xvec = self.road[1][0] - self.road[0][0]  # x direction of road
        yvec = self.road[1][1] - self.road[0][1]  # y direction of road
        mag = (xvec ** 2 + yvec ** 2) ** 0.5  # length of road
        if xvec != 0:  # not vertical
            x += xvec * length / mag  # x_1 = x_0 + dx
            y = yvec / xvec * (x - self.road[0][0]) + self.road[0][1]  # correction
        else:  # vertical
            y += yvec * length / mag
            x = xvec / yvec * (y - self.road[0][1]) + self.road[0][0]
        return (x - _x, y - _y)

    def attacked(self, damage):  # tower attack unit
        if self.HP <= damage:  # unit died
            self.HP = 0
            self.canvas.delete(self.id)
            self.canvas.delete(self.hpbar)
            self.canvas.delete(self.hpbarBackground)
            self.inBattle = False
            del self.canvas.unitList[self.canvas.unitList.index(self.parent)]
        else:  # unit not died(just damaged)
            self.HP -= damage
            (x1, y1, x2, y2) = self.canvas.coords(self.hpbar)  # reduced HP
            x2 = x1 + self.HP / self.maxHP * 28
            self.canvas.coords(self.hpbar, x1, y1, x2, y2)

    def attack(self, tower):  # unit attack tower
        if tower in self.canvas.towerList and self.HP > 0 and self.inBattle:  # prevent error
            tower.tower.attacked(int(self.damage * self.canvas.parent.upgradeList[0]))
            self.canvas.after(int(1000 * self.cooltime), lambda: self.attack(tower))
        else:  # if tower already dead
            self.inBattle = False  # don't fight anymore

    def distance(self, other):  # distance between center of unit and center of other
        x1, y1, x2, y2 = self.canvas.coords(self.id)
        z1, w1, z2, w2 = other.canvas.coords(other.id)
        return 0.5 * ((x1 + x2 - z1 - z2) ** 2 + (y1 + y2 - w1 - w2) ** 2) ** 0.5

    def nearEnemy(self): # find nearest Enemy
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
