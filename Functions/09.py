#generator function with yeild 
def even(a):
    for i in range(2,a+1,2):
        yield i

for num in even(10):
    print(num)