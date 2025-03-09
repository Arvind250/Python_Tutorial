#reverse a string using loop

my_str = input("Enter a string : ")
new_str = ''
for char in my_str:
    new_str= char+new_str
print(new_str)