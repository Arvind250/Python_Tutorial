#generator function with yeild for even numbers
def even(a):
    for i in range(2,a+1,2):
        yield i

for num in even(10):
    print(num)