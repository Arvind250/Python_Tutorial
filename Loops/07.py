# Validate input ( keep asing user for input value until they enter number btw 1 to 10)

while True:
    i = int(input("Enter a number btw 1 and 10 to exit : "))
    if 0< i <=10:
        print("Ended")
        break