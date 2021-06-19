from .unit1 import Unit1
from .unit2 import Unit2


class Unit:
    def __init__(self, parent, unitId, road):
        if unitId == 1:
            self.unit = Unit1(self, parent, road)
        elif unitId == 2:
            self.unit = Unit2(self, parent, road)

    def update(self):
        self.unit.update()