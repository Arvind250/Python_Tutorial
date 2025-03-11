# program to find sum of n natural numbers using recurson function
def sum (num):
    if num ==0:
        return 0
    else:
        return num + sum(num-1)
print(sum(9))