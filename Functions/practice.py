# def my_function(a):
#     for i in a:
#         print(i,end=" ")

# my_function([1,2,3,4])

def fact_function (n):
    fact=1
    for i in range(1,n+1,1):
        fact*=i
    print(fact)
num= int(input("Enter a number : "))
fact_function(num)