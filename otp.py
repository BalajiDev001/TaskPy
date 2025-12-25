import random as rand

li=[]
num=int(input("Enter a Number :"))
for i in range(1,num+1):
    data=rand.randint(1000,9999)
    li.append(data)
    # print(data)
    
# print(li)      #exactly what the given randomly with repetation
print(set(li))   #without duplicates 
print(len(li))


