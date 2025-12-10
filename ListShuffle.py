li=[1,2,3,4,5,6]
divide= len(li)//2
print(divide)
player_No=li[:divide]
player_score=li[divide:]
result=[]
for i in range(divide):
    result.append(player_No[i])
    result.append(player_score[i])
print(result)