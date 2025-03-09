# take a string and find the first non repeated character

my_str = input("Enter a string: ")

for char in my_str:
    if my_str.count(char) == 1:
        print("First non-repeated character:", char)
        break
