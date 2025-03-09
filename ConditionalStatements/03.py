# Assign a letter grade based on students score : A(100-90),B(89-80),C(79-70),D(60-69),F(below 60)

marks =int(input('Enter your marks : '))
if (marks>100):
    print('Enter valid marks !!!')
else:
    if(marks > 89):
        print("Your grade is : A")
    elif(marks >79):
        print("Your grade is : B")
    elif(marks >69):
        print("Your grade is : C")
    elif(marks >59):
        print("Your grade is : D")
    else:
        print("Your grade is : F")