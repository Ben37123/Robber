from level1 import level1
from level2 import level2

class Game(object):

    def __init__(self):
        self.__currentHealth = 100
        self.__currentLevel = level1

