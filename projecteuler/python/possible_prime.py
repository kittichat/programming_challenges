prime = int(input("type prime number :"))
prime_sub = 2
array1 = []
x = 0
y = 0

#if x not equal prime number then continous find prime number
#x is multiply from prime number in array

# while(x != prime):
    
#     for i <= prime:
        


#find prime number
while prime_sub < prime:

    for i in range(2,prime_sub):
        #print(i)
        if prime_sub % i == 0:
            # i is not prime number
            #collect prime to array
            y = 0 # not prime
            break
        else:
            y = 1 # prime

    if y == 1 and prime_sub not in array1:     
        #print("This is prime %s"% (prime_sub))    
        array1.append(prime_sub)     
    prime_sub += 1
      

print(array1)


#check if prime in array don't append to array
