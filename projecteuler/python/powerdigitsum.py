def exponent(x,y):
  i = 1
  count = 0
  while count < y:
    i = x * i
    count += 1
  
  return i
  
number = exponent(2,1000)
atlast = str(number)
summation = 0
for i in atlast:
  i = int(i)
  summation = summation + i

print(summation)