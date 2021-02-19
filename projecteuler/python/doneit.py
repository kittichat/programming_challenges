x = 1
y = 2
array1 = []
z = 0
while z < 500 :
  x = y + x
  i = 1
  z = 0
  while i <= x:
    if x % i == 0:
      z += 1
    i += 1
  
  array1.append(z)
  y += 1
print(x)
print(array1)
