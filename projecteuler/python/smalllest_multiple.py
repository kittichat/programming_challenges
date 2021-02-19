
max = 20
min = 1
x = 1
y = False
while y == False:
  for i in range(min,max+1):
    if x % i != 0:
      y = False
      break
    else:
      y = True
  x += 1
print(x-1)



