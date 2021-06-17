from tkinter import *
from tkinter.font import *
from map import Map
from components.buttons import BackButton, UnitButton, UpgradeButton


class Game(Frame):
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.difficulty = StringVar()
        self.title = Label(self, textvariable=self.difficulty, font=Font(size=50), width=10)
        self.title.grid(row=0, column=0, columnspan=2)

        self.backButton = BackButton(self)
        self.backButton.grid(row=0, column=2)

        self.unitFrame = UnitFrame(self)
        self.unitFrame.grid(row=2, column=0)

        self.upgradeList = [1, 1, 1, 0.1]  # damageRate, HPRate, speedRate, mps
        self.upgradeFrame = UpgradeFrame(self)
        self.upgradeFrame.grid(row=2, column=1)

        self.money = Money(100)
        self.moneyLabel = Label(self, text=self.money)
        self.moneyLabel.grid(row=2, column=2)
        self.after(1000, self.moneyPerSecond)

        self.map = Map(self, width=1200, height=600, background="green")
        self.after(20, self.map.nextFrame)
        self.map.grid(row=1, column=0, columnspan=3)

    def moneyPerSecond(self):
        self.money += self.upgradeList[3] * 10
        self.after(1000, self.moneyPerSecond)


class Money:
    def __init__(self, value=0):
        self.value = value

    def get(self):
        return self.value

    def set(self, newValue):
        self.value = newValue

    def __iadd__(self, other):
        self.value += other  # other = float
        return self

    def __str__(self):
        return "$" + str(int(self.value))

    def __imul__(self, other):
        self.value = int(self.value * other)  # other = float
        return self

    def __isub__(self, other):
        self.value -= other
        return self


class UnitFrame(Frame):
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        self.configure(highlightbackground="black")
        self.configure(highlightthickness=1)
        self.parent = parent
        self.unitCosts = [
            Money(10),
            Money(20),
            Money(40),
            Money(80),
            Money(150),
            Money(300),
            Money(1000),
        ]
        self.unitButtons = [UnitButton(self, i) for i in range(1, 8)]
        self.unitLabels = [Label(self, text=i) for i in self.unitCosts]
        for (i, B, L) in zip(range(7), self.unitButtons, self.unitLabels):
            B.bind("<Enter>", B.mouseHoverIn)
            B.bind("<Leave>", B.mouseHoverOut)
            B.grid(row=0, column=i, padx=15, pady=(20, 0))
            L.grid(row=1, column=i, padx=15, pady=5)


class UpgradeFrame(Frame):
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        self.configure(highlightbackground="black")
        self.configure(highlightthickness=1)
        self.parent = parent
        self.upgradeParams = ["damage", "HP", "speed", "money"]
        self.upgradeCosts = [Money(100), Money(100), Money(100), Money(100)]
        self.upgradeButtons = [UpgradeButton(self, i) for i in range(4)]
        self.upgradeLabels = [Label(self, text=i) for i in self.upgradeCosts]
        for (i, B, L) in zip(range(7), self.upgradeButtons, self.upgradeLabels):
            B.grid(row=0, column=i, padx=20, pady=(20, 0))
            L.grid(row=1, column=i, padx=20, pady=5)
