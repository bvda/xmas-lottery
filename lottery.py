from lottery_number import LotteryNumber
import random
import time

class Lottery:
  def __init__(self):
    self.pool = [LotteryNumber(n, c[0], c[1]) for c in [['red', 'C'], ['green', 'G'], ['blue', 'F'], ['yellow', 'A'], ['orange', 'E']] for n in list(range(1,101))]
    self.drawn = []
    self.time = time.time()
    with open(f'{self.time}.txt', 'w') as file:
      file.write(f'{self.time}\n')
    random.seed(self.time)

  def get_pool(self):
    return self.pool
  
  def draw(self):
    drawn = self.pool.pop(random.randint(0, len(self.pool)))
    self.drawn.append(drawn)
    with open(f'{self.time}.txt', '+a') as file:
      file.write(f'{drawn.litra} {drawn.number}\n')
    return self.pool, self.drawn
  

  def clear(self):
    self.pool = [LotteryNumber(n, c[0], c[1]) for c in [['red', 'C'], ['green', 'G'], ['blue', 'F'], ['yellow', 'A'], ['orange', 'E']] for n in list(range(1,101))]
    self.drawn = []
    return self.pool, self.drawn