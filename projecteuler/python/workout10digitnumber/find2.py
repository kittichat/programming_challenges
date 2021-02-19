
f = open("data.txt",'r')
y = 0
for i in range(0,100):
    x = f.readline()
    print(x)
    y = y + int(x)

print(y)
