#a = 91 * 90
#b = str(a) 
#c = len(b) 
#c1 = c-1 #last array
#d = 0 #decrease
#e = 0
x = 999
y = 1 #first factor
m = 0 #collect largest number
l = 1
#z = 1
array2 = []
#check is number palindrome
while y < x:
  z = 1 #second factor
  while z < x:
    a = y*z
    b = str(a)
    c = len(b)
    c1 = c-1
    d = 0
    e = 0 #sign for tell the number is palindrome or not
    array1 = []
    if c % 2 == 0:
      for i in b:
        array1.append(i)
      while d < c1:
        if array1[d] == array1[c1-d]:
          e = 1
        else:
          e = 0
          break
        d += 1
      if e == 1 :
        #print(a)
        array2.append(a)
    z += 1
  y += 1
# find the most largest number in array
k = len(array2)
while l < k:
  if array2[l] > m:
    m = array2[l]
  l += 1
  
print(array2)
print(m)