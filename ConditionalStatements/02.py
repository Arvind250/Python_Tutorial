#movie tickets are priced based on age : $12 for adults (18 and over),$8for children.everyone gets discount of $2 on wednesday.

print("----This program finds the cost of your movie tickets ----")
age = int(input("Enter your age : "))
day = input("What day is the movie show ? :")
if(age < 18):
    if(day == "wednesday"):
        print("The cost of the ticket is $",8-2)
    else:
        print("The cost of the ticket is $",8)
else:
    if(day == "wednesday"):
        print("The cost of the ticket is $",12-2)
    else:
        print("The cost of the ticket is $",12)