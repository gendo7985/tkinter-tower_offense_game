from tkinter import *
from tkinter.font import *


class MainButton(Button):
    def __init__(self, parent, text, command, *args, **kwargs):
        Button.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self["font"] = Font(size=30)
        self["width"] = 10
        self["height"] = 2
        self["text"] = text
        self["command"] = command


class BackButton(Button):
    def __init__(self, parent, *args, **kwargs):
        Button.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.configure(font=Font(size=15), text="메인으로")
        self.configure(width=4, height=2)

        def command():
            self.parent.pack_forget()
            if type(self.parent).__name__ == "Game":
                self.parent.parent.Game.destroy()
            self.parent.parent.Main.pack()

        self.configure(command=command)


class LevelButton(MainButton):
    def __init__(self, parent, text, command, *args, **kwargs):
        MainButton.__init__(self, parent, text, command, *args, **kwargs)
        self.parent = parent
        self.configure(width=7, height=5)


class UnitButton(Button):
    def __init__(self, parent, unitId, *args, **kwargs):
        Button.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.unitId = unitId
        self.configure(text=str(unitId))
        self.configure(width=2, height=2)
        self.description = [
            "1) basic unit.\n  HP: 50, DPS: 5, range:200, speed: 3",
            "2) tanker unit.\n  HP: 300, speed: 2",
            "3) bomb unit.\n  HP: 80, damage: 300(nexus), speed: 5",
            "4) power unit.\n  HP: 250, DPS: 20, range: 300, speed: 3",
            "5) anti-tower unit.\n  HP: 200, DPS: 50, range: 150, speed: 1",
            "6) healer unit.\n  HP: 100, HPS: 10, range: 100, speed: 2",
            "7) final unit.\n  HP: 500, DPS: 100(10%-kill), range: 200, speed: 1",
        ]

        def command():
            diffMoney = self.parent.parent.money.get() - self.parent.unitCosts[unitId - 1].get()
            if diffMoney >= 0:
                self.parent.parent.map.addUnit(unitId)
                self.parent.parent.money.set(diffMoney)

        self.configure(command=command)

    def mouseHoverIn(self, _):
        self.tip = self.parent.parent.map.create_text(
            10, 570, text=self.description[self.unitId - 1], anchor=W
        )

    def mouseHoverOut(self, _):
        self.parent.parent.map.delete(self.tip)


class UpgradeButton(Button):
    def __init__(self, parent, paramId, *args, **kwargs):
        Button.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.paramId = paramId
        self.configure(text=parent.upgradeParams[paramId])
        self.configure(width=4, height=2)

        def command():
            diffMoney = (
                self.parent.parent.money.get() - self.parent.upgradeCosts[self.paramId].get()
            )
            if diffMoney >= 0:
                self.parent.parent.money.set(diffMoney)
                self.parent.parent.upgradeList[self.paramId] += 0.1
                self.parent.upgradeCosts[self.paramId] *= 1.1
                self.parent.upgradeLabels[self.paramId].configure(
                    text=self.parent.upgradeCosts[self.paramId]
                )
                if self.paramId == 1:  # present unit HP correction
                    for unit in self.parent.parent.map.unitList:
                        unit.unit.maxHP = int(
                            unit.unit.maxHP
                            * self.parent.parent.upgradeList[2]
                            / (self.parent.parent.upgradeList[2] - 0.1)
                        )
                        unit.unit.HP = int(
                            unit.unit.HP
                            * self.parent.parent.upgradeList[2]
                            / (self.parent.parent.upgradeList[2] - 0.1)
                        )

        self.configure(command=command)

    def mouseHoverIn(self, e):
        self.description = [
            "Damage rate: x {0:0.1f}".format(self.parent.parent.upgradeList[0]),
            "HP rate: x {0:0.1f}".format(self.parent.parent.upgradeList[1]),
            "Speed rate: x {0:0.1f}".format(self.parent.parent.upgradeList[2]),
            "Money/s: ${0:d}".format(int(self.parent.parent.upgradeList[3] * 10)),
        ]
        self.tip = self.parent.parent.map.create_text(
            1190, 580, text=self.description[self.paramId], anchor=E
        )

    def mouseHoverOut(self, e):
        self.parent.parent.map.delete(self.tip)
