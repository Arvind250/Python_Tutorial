# n = 3
# i = 1 
# while i<=10:
#     print(i*n)
#     i+=1


# num=[1,2,3,4,5,6,7,8,9]
# i=0
# while i<len(num):
#     print(num[i])
#     i+=1

# for i in range(1,5,2):
#    print(i)

# num=6
# for i in range(1,10):
#     print(num*i)

# a=["hello","world","coding","python","tutorials"]
# for i in range(len(a)-1,-1,-1):
#     print(i,a[i])

# n = int(input("Enter the value of n : "))
# i=0
# sum=0
# while i<n:
#     sum+=i
#     i+=1
# print(sum)

n = int(input("Enter a number : "))
fact=1
for i in range(n,0,-1):
    fact*=i
print(fact)