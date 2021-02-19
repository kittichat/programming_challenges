# if number is even then number/2
# if number is odd then number*3 + 1
#number = 2
array1 = []
limit = 1000000
i = 2

while i <= limit:
  count = 0
  number = i
  while number != 1:
    if number % 2 == 0:
      number = number / 2
    else :
      number = (number * 3) + 1
    #print(number)
    count += 1
  array1.append(count)
  i += 1

z = 0
for y in array1:
  if z < y:
    z = y

  
print(z)
print(array1.index(z))

#when the result comes up >> you need to plus 2 because number (i) start from 2 and index count from 0
