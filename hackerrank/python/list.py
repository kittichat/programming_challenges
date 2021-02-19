#"""
x = int(input())
y = int(input())
z = int(input())
n = int(input())
#i = 0
# j = 0
# k = 0
list1 = [0, 0 ,0]
list2 = []
# a = 0 # a is sum of object in list1
# c = 0
# d = 0
while list1[0] < x:   #***********
  a = 0
  g = list1
  for b in list1:
    a = a + b
  if a != n:
    list2.append(g)
    #print(list1)
  #list1[0] += 1
  #i += 1
  g = 0
  print(list2)
  list1[1] = 0
  #j = 0
  while list1[1] < y:     #***********
    c = 0
    h =list1
    for e in list1:
      c = c + e
    if c != n:
      list2.append(h)
      #print(list1)
    #list1[1] += 1
    print(list2)
    #j += 1
    h = 0
    list1[2] = 0  
    #k = 0
    while list1[2] < z:   #***********
      d = 0
      m = list1
      for f in list1:
        d = d + f
      if d != n:
        list2.append(m)
      print(list1)
      m = 0
      list1[2] += 1
      #k += 1
      print(list2)
    list1[1] += 1
    #j += 1
  list1[0] += 1
  #i += 1

list6 = []

for f in list2:
  if f not in list6:
    list6.append(f)

#print(list6)


#"""

# the problem is when i append list1 to list2 after change value in list1 the value in list2 change too.