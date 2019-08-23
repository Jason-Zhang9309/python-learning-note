import numpy as np
import numpy.matlib
from random import choice, randint



class Matrix(object):
  def __init__(self):
    self.numbers = np.matlib.zeros((4, 4), dtype=int)
    self.blocks = []

  def new_block(self):
    i = 0
    while i <2:
      x = randint(0, 3)
      y = randint(0, 3)
      if self.numbers[x,y] == 0:
        self.numbers[x,y] = choice([2,4])
        i += 1
    

  def update(self):
    #先把元素全部归零，在更新到最新状态

    pass

  def list_move(self,list,direction):
    if direction == 'left':
      for i in range(1,4):
        print(list[0,i])
        if list[0,i-1] == list[0,i]:
          list[0,i-1] *= 2
          list[0,i] = 0
        if list[0,i-1] == 0:
          list[0,i-1] = list[0,i]
          list[0,i] = 0    
      return(list)

    if direction == 'right':
      for i in range(2,-1,-1):
        if list[0,i+1] == list[0,i]:
          list[0,i+1] *= 2
          list[0,i] = 0
        if list[0,i+1] == 0:
          list[0,i+1] = list[0,i]
          list[0,i] = 0    
      return(list)

    if direction == 'up':
      for i in range(1,4):
        if list[i-1,0] == list[i,0]:
          list[i-1,0] *= 2
          list[i,0] = 0
        if list[i-1,0] == 0:
          list[i-1,0] = list[i,0]
          list[i,0] = 0    
      return(list)

    if direction == 'down':
      for i in range(2,-1,-1):
        if list[i+1,0] == list[i,0]:
          list[i+1,0] *= 2
          list[i,0] = 0
        if list[i+1,0] == 0:
          list[i+1,0] = list[i,0]
          list[i,0] = 0    
      return(list)

  def move(self,direction):
    if direction == 'left':
      for i in range(4):
        list = self.numbers[i,:]
        print(list)
        self.numbers[i,:] = self.list_move(list,'left')
              
    if direction =='right':
      for i in range(4):
        list = self.numbers[i,:]
        print(list)
        self.numbers[i,:] = self.list_move(list,'right')

    if direction == 'up':
      for i in range(4):
        list = self.numbers[:,i]
        print(list)
        self.numbers[:,i] = self.list_move(list,'up')

    if direction == 'down':
      for i in range(4):
        list = self.numbers[:,i]
        print(list)
        self.numbers[:,i] = self.list_move(list,'down')

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

def keybroad_check(m):
    key = input('-> ')
    if key == 'a':
      m.move('left')
    if key == 'd':
      m.move('right')
    if key == 'w':
      m.move('up')
    if key == 's':
      m.move('down')
 

def main():
  m = Matrix()
  m.new_block()
  m.new_block()
  
  m.update()
  m.show()
  while True:
  
    keybroad_check(m)
    m.update()
    #m.new_block()
    m.show()


if __name__ == '__main__':
  main()
