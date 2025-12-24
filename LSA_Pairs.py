#Len sub array 0 & 1

nums = [1, 1, 0, 0, 1] 
newlis=[] 

for i in nums:
    if i==0:
        newlis.append(-1)
    else:
        newlis.append(i)
print(newlis)
print(len(nums)-sum(newlis))




























# liist=[1,0,0,1,1]

# one_count=liist.count(1)
# zero_count=liist.count(0)
# print(one_count)
# print(zero_count)

# print(min(one_count,zero_count)*2)


# def Longest_Subarray_with_Equal_0s_and_1s(li):
#     return min(li.count(1), li.count(0)) * 2


# if __name__ == "__main__":

#     li = []
#     n = int(input("Enter List Size: "))

#     for i in range(n):
#         li.append(int(input(f"Enter {i+1} value: ")))

#     print(Longest_Subarray_with_Equal_0s_and_1s(li))  # user choice

#     print(Longest_Subarray_with_Equal_0s_and_1s([1,0,1,1,0,1,1,0]))  # 6
#     print(Longest_Subarray_with_Equal_0s_and_1s([1,0,1,0,1,0]))      # 6
#     print(Longest_Subarray_with_Equal_0s_and_1s([1,1,0]))            # 2


# def Longest_Subarray_with_Equal_0s_and_1s(li):
#     return min(li.count(1),li.count(0))*2

# if __name__ == "__main__":
#     li=[]
#     n=int(input("Enter List Size :"))    
#     for i in range(n):
#         value=int(input(f"Enter {i+1} value :"))
#         li.append(value)
#     result=Longest_Subarray_with_Equal_0s_and_1s(li)    
#     print("longest subarray length",result)

#     test1=[1,0,1,1,0,1,1,0]
#     ans1=Longest_Subarray_with_Equal_0s_and_1s(test1)
#     print(ans1)
#     test2=[1,0,1,0,1,0]
#     ans2=Longest_Subarray_with_Equal_0s_and_1s(test2)
#     print(ans2)
#     test3=[1,1,0]
#     ans3=Longest_Subarray_with_Equal_0s_and_1s(test3)
#     print(ans3)


#sn ---------------- sn

# # nums = [0,1,0]
# # li=[]
# # one_count=0
# # zero_count=0
# # for i in nums:
# #     if i==1:
# #         one_count+=1
# #     else:
# #         zero_count+=1
# # li.append(one_count)
# # li.append(zero_count)
# # print(li)
# # sum=0
# # s=min(li)
# # print(s*2)


# li = [1,0,1,0,1,1,1]

# # one = li.count(1)
# # zero = li.count(0)
# print(min(li.count(1),li.count(0))*2)