# check if a password is weak, medium or strong based on chars in it.

password=input("Enter password :")

if len(password) > 10:
    print("strong")
elif len(password) >=6 :
        print("medium")
else:
    print("weak")