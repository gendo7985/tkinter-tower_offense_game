from tkinter import *
from unit import Unit
from tower import Tower

mapData = [
    2,
    "0 450 200 400 600 500 900 375 300 225 600 100 1000 200 1200 150",
    "0 1170 150 1 500 375 1 820 520 1 730 240 1 370 80",
    "0 450 200 400 600 500 900 375 300 225 600 100 1000 200 1200 150",
    "0 100 150 1 500 375 2 820 520 1 730 240 1 370 80",
]


class Map(Canvas):
    def __init__(self, parent, *args, **kwargs):
        Canvas.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.stage = 1
        self.unitList = []
        self.towerList = []

        self.roadInfo = []
        self.towerInfo = []
        for i in range(mapData[0]):
            self.roadInfo.append(map(int, mapData[2 * i + 1].split()))
            self.towerInfo.append([*map(int, mapData[2 * i + 2].split())])

        # road
        self.create_line(*self.roadInfo[0], width=50, capstyle=ROUND, fill="#613613")
        # tower
        for i in range(0, len(self.towerInfo[0]), 3):
            tower = self.towerInfo[0]
            self.towerList.append(Tower(self, tower[i], (tower[i + 1], tower[i + 2])))

        self.bind("<Button-1>", self.getXY)  # for tower initialization

    def addUnit(self, unitId):
        self.unitList.append(Unit(self, unitId))

    def nextFrame(self):
        for unit in self.unitList:
            unit.update()
        for tower in self.towerList:
            tower.update()
        self.parent.moneyLabel.configure(text=self.parent.money)
        self.after(20, self.nextFrame)

    def getXY(self, e):  # for tower initialization
        print(e)

    def nextStage(self):
        self.stage += 1
        self.parent.difficulty.set(self.parent.difficulty.get()[:-3] + str(self.stage) + "단계")
        self.delete("all")
        # road
        self.create_line(*self.roadInfo[self.stage - 1], width=50, capstyle=ROUND, fill="#613613")
        # tower
        for i in range(0, len(self.towerInfo[self.stage - 1]), 3):
            tower = self.towerInfo[self.stage - 1]
            self.towerList.append(Tower(self, tower[i], (tower[i + 1], tower[i + 2])))
