value = str(input("type text: "))
array1 = []
array_shift = []
for i in value :
  array1.append(ord(i))


def shift():
      
  s = 1
  while s < 100:
    array_shift = []
    for x in array1:
      y = (x + s) % 127
      array_shift.append(y)
    for z in range(len(array_shift)):
       print(chr(array_shift[z]), end= '')
    print('\n') 
    s += 1

shift()
