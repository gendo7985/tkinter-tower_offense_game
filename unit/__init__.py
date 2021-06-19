from .unit1 import Unit1
from .unit2 import Unit2
from .unit3 import Unit3
from .unit4 import Unit4
from .unit5 import Unit5
from .unit6 import Unit6
from .unit7 import Unit7


class Unit:  # collection of unit1 ~ unit7
    def __init__(self, parent, unitId, road):
        if unitId == 1:
            self.unit = Unit1(self, parent, road)
        elif unitId == 2:
            self.unit = Unit2(self, parent, road)
        elif unitId == 3:
            self.unit = Unit3(self, parent, road)
        elif unitId == 4:
            self.unit = Unit4(self, parent, road)
        elif unitId == 5:
            self.unit = Unit5(self, parent, road)
        elif unitId == 6:
            self.unit = Unit6(self, parent, road)
        elif unitId == 7:
            self.unit = Unit7(self, parent, road)

    def update(self):
        self.unit.update()