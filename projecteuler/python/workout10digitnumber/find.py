f = open("data.txt","r")
x = 0
while f.readline() :
    x = f.readline()
    print(x.strip(),end = "")
