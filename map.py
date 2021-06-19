from tkinter import *
from unit import Unit
from tower import Tower


class Map(Canvas):
    def __init__(self, parent, *args, **kwargs):
        Canvas.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.stage = 1
        self.unitList = []
        self.towerList = []

        self.roadInfo = []
        self.towerInfo = []
        # mapData: # of stage \n roadInfo \n towerInfo \n ...
        with open("./mapData.txt", "r") as f:
            for i in range(int(f.readline())):
                self.roadInfo.append([*map(int, f.readline().split())])
                self.towerInfo.append([*map(int, f.readline().split())])
        # road
        self.create_line(*self.roadInfo[0], width=50, capstyle=ROUND, fill="#613613")
        # tower
        for i in range(0, len(self.towerInfo[0]), 3):
            tower = self.towerInfo[0]
            self.towerList.append(Tower(self, tower[i], (tower[i + 1], tower[i + 2])))
        self.bind("<Button-1>", self.getXY)  # for tower initialization

    def addUnit(self, unitId):
        self.unitList.append(Unit(self, unitId, self.roadInfo[self.stage - 1]))

    def nextFrame(self):
        self.after(20, self.nextFrame)
        for unit in self.unitList:
            unit.update()
        self.parent.moneyLabel.configure(text=self.parent.money)

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
