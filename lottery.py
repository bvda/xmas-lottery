class Lottery:
  def __init__(self):
    self.pool = list(range(1,101))
  
  def get_pool(self):
    return self.pool