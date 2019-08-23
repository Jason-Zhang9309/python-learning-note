import numpy as np
import numpy.matlib
from random import choice, randint


class Numblock(object):
    def __init__(self, x, y, number=choice([2, 4])):
        self.number = number
        self.x = x
        self.y = y

    def move(self):
        pass

    def merge(self):
        pass


class Matrix(object):
    def __init__(self, numbers=np.matlib.zeros((4, 4), dtype=int)):
        self.numbers = numbers
        self.blocks = []

    def update(self):
        x = randint(0, 4)
        y = randint(0, 4)
        self.blocks.append(Numblock(x, y)
                           )
        for block in self.blocks:
            self.numbers[block.x, block.y] = block.number


    def show(self):
        print('+-----+-----+-----+-----+\n'
              '|  {}  |  {}  |  {}  |  {}  |\n'
              '+-----+-----+-----+-----+\n'
              '|  {}  |  {}  |  {}  |  {}  |\n'
              '+-----+-----+-----+-----+\n'
              '|  {}  |  {}  |  {}  |  {}  |\n'
              '+-----+-----+-----+-----+\n'
              '|  {}  |  {}  |  {}  |  {}  |\n'
              '+-----+-----+-----+-----+\n'
              .format(self.numbers[0, 0], self.numbers[0, 1], self.numbers[0, 2], self.numbers[0, 3],
                      self.numbers[1, 0], self.numbers[1, 1], self.numbers[1, 2], self.numbers[1, 3],
                      self.numbers[2, 0], self.numbers[2, 1], self.numbers[2, 2], self.numbers[2, 3],
                      self.numbers[3, 0], self.numbers[3, 1], self.numbers[3, 2], self.numbers[3, 3],
                      ))


def main():

    m = Matrix()
    m.update()
    m.show()


if __name__ == '__main__':
    main()
