from lottery_number import LotteryNumber
import random

class Lottery:
  def __init__(self):
    self.pool = [LotteryNumber(n, c) for c in ['red', 'green', 'blue', 'yellow'] for n in list(range(1,101))]
    self.drawn = []

  def get_pool(self):
    return self.pool
  
  def draw(self):
    drawn = self.pool.pop(random.randint(0, len(self.pool)))
    self.drawn.append(drawn)
    return self.pool, self.drawn
  

  def clear(self):
    self.pool = [LotteryNumber(n, c) for c in ['red', 'green', 'blue', 'yellow'] for n in list(range(1,101))]
    self.drawn = []
    return self.pool, self.drawn