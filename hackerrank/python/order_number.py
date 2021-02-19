# input number and print output in string format with order number
n = int(input("Type the number : "))
array1 = []
i = 1 
j = 1
x = ""
while i <= n:
  array1.append(str(i))
  i += 1

for j in range(len(array1)):
    print(array1[j], end= "")
    