# to dtermine if a yeay is leap year or not

year=int(input("Enter a year : "))
if ((year % 4 or year % 100 != 0) or year % 400 ==0):
    print("Leap year")
else:
    print("Not a leap year")