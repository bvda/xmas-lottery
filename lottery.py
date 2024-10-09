from lottery_number import LotteryNumber

class Lottery:
  def __init__(self):
    self.pool = [LotteryNumber(n, c) for c in ['red', 'green', 'blue', 'yellow'] for n in list(range(1,101))]
  
  def get_pool(self):
    return self.pool