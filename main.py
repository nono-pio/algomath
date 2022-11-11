class baseFonction():
  def __add__(self, added):
    return add(self, added)

class add():
  def __init__(self, a, b):
    self.a = a
    self.b = b

class log(baseFonction):
  def __init__(self, x, base=2.718):
    self.x = x
    self.base = base

ln = log(2)
x = ln + 2
print(x,x.a.x,x.a.base,x.b)