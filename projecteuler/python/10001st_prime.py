prime = 3
array1 = [1, 2]
x = False
y = 0
while len(array1) != 10002:
  #while prime < 10000000:
  for i in range(2,prime):
    if prime % i == 0:
      x = False
      break
    else:
      x = True
  if x == True:
    array1.append(prime)
  prime += 1
  #array1.append(y)
print(array1[10001])
