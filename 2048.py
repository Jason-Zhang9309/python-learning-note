import numpy as np
from random import choice, randint
import pygame
from time import sleep
import sys

class Matrix(object):
  def __init__(self):
    self.numbers = np.zeros((4, 4), dtype=int)
    self.blocks = []

  def new_block(self):
    empty_list = []
    for x in range(0,4):
      for y in range(0,4):
        if self.numbers[x,y] == 0:
          empty_list.append((x,y))
    print("empty_list:" ,empty_list)

    try:
      for i in range(randint(0,2)):
        index = choice(empty_list)
        print(index)
        self.numbers[index] = choice([2,4])
        empty_list.remove(index)
      return(False)
      
    except IndexError:
      try:
        index = choice(empty_list)
        print(index)
        self.numbers[index] = choice([2,4])
        empty_list.remove(index)
      except IndexError:
        return(True)
    

  def list_move(self,list):

    moved = True
    while moved:
      moved = False
      print(moved)
      
      for i in range(1,4):
        if list[i] != 0 and list[i-1] == 0:
          list[i-1] = list[i]
          list[i] = 0
          moved = True
          print(moved)
    return(list)

  def list_merge(self,list):
    for i in range(1,4):
      if  list[i] != 0 and list[i-1] == list[i]:
        list[i-1] *= 2
        list[i] = 0
          
  def move_and_merge(self,list):
    self.list_move(list)
    self.list_merge(list)
    self.list_move(list)
    return(list)

  def move(self,direction):
    if direction == 'left':
      for i in range(4):
        list = self.numbers[i,:]
        print(list)

        self.numbers[i,:] = self.move_and_merge(list)
              
    if direction =='right':
      for i in range(4):
        list = self.numbers[i,:]
        list = list[::-1]
        print(list)
        self.numbers[i,:] = self.move_and_merge(list)[::-1]

    if direction == 'up':
      for i in range(4):
        list = self.numbers[:,i]
        print(list)
        self.numbers[:,i] = self.move_and_merge(list)

    if direction == 'down':
      for i in range(4):
        list = self.numbers[:,i]
        list = list[::-1]
        print(list)
        self.numbers[:,i] = self.move_and_merge(list)[::-1]

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
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      sys.exit()
    elif event.type == pygame.KEYDOWN:
      if event.key == pygame.K_LEFT:
        m.move('left')
        return(True)
        break
      if event.key == pygame.K_RIGHT:
        m.move('right')
        return(True)
        break
      if event.key == pygame.K_UP:
        m.move('up')
        return(True)
        break
      if event.key == pygame.K_DOWN:
        m.move('down')
        return(True)
        break


def game_over_check(numbers):
  moveable = False
  def list_check(list):
    moveable_list = False
    for i in range(1,4):
      if  list[i] != 0 and list[i-1] == list[i]:
        moveable_list = True
        break
    return(moveable_list)
      


  for i in range(4):
    list = numbers[i,:]
    if list_check(list):
      moveable = True
      break

 
  for i in range(4):
    list = numbers[:,i]
    if list_check(list):
      moveable = True
      break

  return(moveable)

def blocks_draw(screen,numbers):
  for i in range(4):
    for j in range(4):
      image = pygame.image.load('images/2048-{}.png'.format(numbers[i,j]))
      rect = image.get_rect()
      rect.x = j*96
      rect.y = i*96
      screen.blit(image,rect)
 

def main():
  m = Matrix()
  m.new_block()
  pygame.init()
  m.show()

  screen = pygame.display.set_mode((374,374))
  pygame.display.set_caption("2048")
  bg_color = (230,230,230)
  screen.fill(bg_color)
  blocks_draw(screen,m.numbers)
  pygame.display.flip()

  while True:
    while True:
      if keybroad_check(m):
        break
    
    matrix_full = m.new_block()
    if matrix_full:
      if game_over_check(m.numbers)== False:
        break
    m.show()
    #screen.fill(bg_color)
    blocks_draw(screen,m.numbers)
    pygame.display.flip()
    
  print('game over')
  exit()

if __name__ == '__main__':
  main()



