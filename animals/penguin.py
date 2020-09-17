from movements import ISwimming, IWalking

class Penguin(IWalking, ISwimming):
  def __init__(self, name):
    ISwimming.__init__(self)
    IWalking.__init__(self)
    self.name = name

  def run(self):
    print(f'{self} waddles')

  def swim(self):
    print(f'{self} effortlessly glides')

  def __str__(self):
    return f'{self.name} the penguin'