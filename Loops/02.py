# calculate the sum of even numbers upto a given n 
n = int(input("Enter a number : "))
sum=0
for i in range(2,n+1,2):
    sum+=i
print(sum)