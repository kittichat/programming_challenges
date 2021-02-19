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
print(limit)
while round <= limit:
    i = array_round   
    #print(i)
    array_round = array_round + round 
    print(f'\n\n {i} and {array_round}')
    while i < array_round:
        print(array2[i],",",end ="")
        i += 1
    #print(",")
    round += 1


#for i in range(len(array1)):
#    for j in range(len(array1[i])):
      # print(array1[i][j])
#        x = int(array1[i][j])
#        print(x)
#    print('\n')






