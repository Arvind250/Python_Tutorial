# suggest an activity based on weather (sunny ,rainy,snowy)
weather=input("Enter weather :")
weathers = ['sunny','rainy','snowy']
if weather not in weathers:
    print("enter valid weather  !!!")
else:
    if weather =='sunny':
        print("go for a walk")
    elif weather =='rainy':
        print("read a book")
    else:
        print("build a snowman")