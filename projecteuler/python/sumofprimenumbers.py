max = 2000000
i = 2
sum = 1
array1 = [2,]
while i < max:
  j = 2
  x = 0
  while j < i :
    if i % j == 0:
      x = 0
      break
    else:
      x = 1
    j += 1
  if x == 1: 
    array1.append(i)
  i += 1

for z in array1:
  sum = sum + z
print(array1)
print(sum)