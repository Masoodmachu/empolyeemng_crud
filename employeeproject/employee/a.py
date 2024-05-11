#
#
# q2) print the series
#  2,5,10,17,26
#
#
# i=2
# k=3
#
# while(i<=20):
#     print(i)
#     i=i+k;
#     k=k+2
# print(i)
#
#
# # q6)primme or not
#
# num=int(input("Enter num:"))
#
# for i in range(2,num):
#     if(num%i==0):
#         print("Not Prime")
#         break
# else:
#     print("Prime")
#
#
# q4)check whether number is armstrong or not
#
# num=int(input("Enter the number:"))
#
# sum=0
# temp=num
#
# while temp>0:
#     digit=temp%10
#     sum=sum+digit**3
#     temp//=10
# if num==sum:
#     print("Number is amstrong")
# else:
#     print("Number is not armstrong")
#
#
#
#
# q7)l=[12,-34,67,19,56,-26,-4]
#
# [12,-34,67,19,56,-26,-4]
#
# a)find sum and count of possitive number
#
# sum=0
# count=0
#
#
#
# s= [12,-34,67,19,56,-26,-4]
#
# for i in s:
#     if(i>0):
#         sum=sum+i
#         count=count+1
#
# print(sum)
# print(count)
#
# # b)find the sum and count of negative number
# s= [12,-34,67,19,56,-26,-4]
#
# sum=0
# count=0
#
# for i in s:
#     if(i<0):
#         sum=sum+i
#         count=count+1
#
# print("sum of negative number:",sum)
# print(count)
#
#
# q5)
#
#
# f=input("Enter the string")
# s=f[::-1]
# print(s)
# if(f==s):
#     print("it is palindrom")
# else:
#     print("Not Palindrom")
#
#
# q1)
#
# l=["banana","orange","apple","grapes","pinapple"]
#
# # a)
#
# for i in l:
#     print(i)
#
#
# b)

# l = ["banana", "orange", "apple", "grapes", "pinapple"]
# for i in l:
#     if 'n' in i:
#         print(i)
#
#
#
#
#
#
# # q9)
# i=[1,2,3,4,1,1,5,6,7,8,9]
#
# s=set(i)
# print(s)