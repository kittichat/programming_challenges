# m > n
n = 1

while n < 100:
  m = n + 1
  while m < 100:
    a = pow(m,2) - pow(n,2)
    b = 2*m*n
    c = pow(m,2) + pow(n,2)
    if (a+b+c == 1000):
      print(a*b*c)
      print("%s %s %s  %s %s" %(a,b,c,m,n))
    m += 1
  n += 1
