number = 101
x = 0
z = 0
a = 0
b = 0
for i in range(1,number):
  z = z+i
  b = z*z
print(b)
for y in range(1,number):
  x  = y*y
  a = a + x 
print(a)

print(b-a)