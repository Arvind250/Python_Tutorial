#Determine if a fruit namely banana is riped ,unriped or overriped based on its color.(yellow green ,brown)

color=input("Enter banana's color :")
colors = ['yellow','green','brown']
if color not in colors:
    print("enter valid color for banana !!!")
else:
    if color =='yellow':
        print("riped")
    elif color =='green':
        print("unriped")
    else:
        print("over-riped")