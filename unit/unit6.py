from .baseUnit import baseUnit


class Unit6(baseUnit):  # healer unit
    def __init__(self, parent, canvas, road):
        baseUnit.__init__(self, canvas, road)
        self.parent = parent
        self.damage = -5
        self.cooltime = 0.2
        self.range = 100
        self.maxHP = int(100 * self.canvas.parent.upgradeList[1])
        self.HP = self.maxHP
        self.speed = 3
        self.color = "magenta"
        self.canvas.itemconfig(self.id, fill=self.color)

    def update(self):
        if not self.inBattle:  # if unit in battle:
            patient = self.nearPatient()  # search patient unit
            if patient != None:  # if there is patient:
                self.attack(self.canvas.unitList[patient])  # heal that unit
            else:  # if there is no patient
                if self.id in self.canvas.find_all():  # prevent error
                    dx, dy = self.nextPosition()  # move forward
                    self.canvas.move(self.id, dx, dy)
                    self.canvas.move(self.hpbar, dx, dy)
                    self.canvas.move(self.hpbarBackground, dx, dy)

    def attack(self, unit):
        if unit in self.canvas.unitList and self.HP > 0 and self.inBattle:
            if unit.unit.HP >= unit.unit.maxHP:
                unit.unit.HP = unit.unit.maxHP
                self.inBattle = False
            else:
                unit.unit.attacked(int(self.damage * self.canvas.parent.upgradeList[0]))
                self.canvas.after(int(1000 * self.cooltime), lambda: self.attack(unit))
        else:
            self.inBattle = False

    def nearPatient(self):  # find worst Patient
        if self.canvas.unitList:
            health = [-1, 1]
            for i in range(len(self.canvas.unitList)):
                unit = self.canvas.unitList[i].unit
                newdist = self.distance(unit)
                if (
                    newdist < self.range  # in range
                    and unit.HP < unit.maxHP  # is attacked
                    and (unit.maxHP - unit.HP) / unit.maxHP < health[1]  # worst patient
                ):
                    health[1] = (unit.maxHP - unit.HP) / unit.maxHP
                    health[0] = i
            if health[0] != -1:
                self.inBattle = True
                return health[0]