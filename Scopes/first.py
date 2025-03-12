# name = 'Alice'  #declared globally
# def fun():
#     name = "BOb"     #declared within the scope
#     print(name)
# print(name)
# fun()

# x = 50
# def fun(y):
#     return x+y
# print(fun(3))


# x= 50
# def fun():
#     x = 2
#     print(x)
# fun()


x = 50
def fun1():
    x=20
    def func2():
        print(x)
    func2()
fun1()