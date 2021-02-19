array1 = []
with open("data.txt","r") as f :
    data = f.readlines()
    print(data)
    
    for i in data:
        #print(i)
        i = i.replace("\n",'')
       # i = i.replace(" ",',')
        i = list(i.split(" "))
        print(i)
        array1.append(i)
    print(len(data))


print(array1,"\n")
array2 = []

for i in range(len(array1)):
    for j in range(len(array1[i])):
      # print(array1[i][j])
        array2.append(int(array1[i][j]))
    #print('\n')
print(array2,"\n")

round = 0
array_round = 0
limit = len(data)
array3 = ["0","1",]
print(limit)
while round <= limit:
    i = array_round   
    #print(i)
    array_round = array_round + round 
    print(f'\n\n {i} and {array_round} {array3}')
    while i < array_round:
        array_temp = []
#        while x < len(array3[round]):
#        if array3 != 0:
        temp = 0
        x = 0
        while x < len(array3[round]):
        #        for x in range(len(array3[round])):
            temp =  int(array3[round][x]) + array2[i]
            array_temp.append(str(temp))
            array3.append(array_temp)
            x += 1
        
        print(array2[i],",",end ="")
        i += 1
            #print(",")
    round += 1

print("\n\n",array3)
checked = 0
for i in array3:
    str1 = ''.join(i)
    str2 = int(str1) - 1
    if str2 > checked:
        checked = str2
print("\n\n\n",checked)
#for i in range(len(array1)):
#    for j in range(len(array1[i])):
      # print(array1[i][j])
#        x = int(array1[i][j])
#        print(x)
#    print('\n')






