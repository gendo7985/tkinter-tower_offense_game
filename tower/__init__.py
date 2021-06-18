from .tower1 import Tower1
from .tower2 import Tower2
from .nexus import Nexus


class Tower:
    def __init__(self, parent, towerId, pos):
        if towerId == 0:
            self.tower = Nexus(self, parent, pos)
        elif towerId == 1:
            self.tower = Tower1(self, parent, pos)
        elif towerId == 2:
            self.tower = Tower2(self, parent, pos)

    def update(self):
        self.tower.update()