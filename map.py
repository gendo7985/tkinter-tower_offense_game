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

    def addUnit(self, unitId):  # button clicked
        self.unitList.append(Unit(self, unitId, self.roadInfo[self.stage - 1]))

    def nextFrame(self):  # update map screen
        self.after(20, self.nextFrame)  # recursion
        for unit in self.unitList:
            unit.update()
        self.parent.moneyLabel.configure(text=self.parent.money)  # update current money

    def getXY(self, e):  # for tower initialization
        print(e)

    def nextStage(self):  # if stage cleared
        self.stage += 1
        self.parent.money.set(50)
        if self.stage > len(self.roadInfo):  # stage clear
            if self.parent.difficulty.get()[:2] == "쉬움":  # add clear message at level button
                self.parent.parent.LevelPage.easyButton.configure(text="쉬움\nclear")
            elif self.parent.difficulty.get()[:2] == "보통":
                self.parent.parent.LevelPage.mediumButton.configure(text="보통\nclear")
            else:
                self.parent.parent.LevelPage.hardButton.configure(text="어려움\nclear")
            self.parent.parent.Game.pack_forget()
            self.parent.parent.LevelPage.pack()
            return  # break

        elif self.stage == len(self.roadInfo):  # last stage
            self.parent.difficulty.set(self.parent.difficulty.get()[:-3] + "FINAL")

        else:
            self.parent.difficulty.set(self.parent.difficulty.get()[:-3] + str(self.stage) + "단계")
        self.delete("all")

        # road
        self.create_line(*self.roadInfo[self.stage - 1], width=50, capstyle=ROUND, fill="#613613")

        # tower
        for i in range(0, len(self.towerInfo[self.stage - 1]), 3):
            tower = self.towerInfo[self.stage - 1]
            self.towerList.append(Tower(self, tower[i], (tower[i + 1], tower[i + 2])))
