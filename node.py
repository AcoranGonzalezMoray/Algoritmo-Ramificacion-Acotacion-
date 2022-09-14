
from collections import namedtuple

Item = namedtuple("Item", ['index', 'value', 'weight'])

class Node:
    def __init__(self, index, taken, value, room):
        self.index = index
        self.taken = taken
        self.value = value
        self.room = room

    def estimate(self, items):
        RST=0

        for i in items:
            if i.index >= self.index-1:
                RST+=i.value
        return RST

