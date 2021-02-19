class Learn:
  def func(self,x: int):
    s = False
    self.x = x
    z = list(str(self.x))
    self.y = [i for i in range(len(z)) if z[i] == z[len(z) - (i+1)]]
    if len(self.y) == len(self.x):
      s = True
    return s

test = Learn()
print(test.func("13377331"))