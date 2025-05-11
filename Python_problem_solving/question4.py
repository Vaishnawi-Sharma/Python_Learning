fruit = 'Banana'
color = input("What's the color of the fruit ??")
if(fruit.lower()=='banana'):
    if (color.lower()=='green'):
        print("Unripe")
    elif (color.lower()=='yellow'):
        print("Ripe") 
    elif (color.lower()=='brown'):
        print("Overripe")
    else :
        print("You have not entered a valid color !")        
else:
    print("Please Enter a valid fruit !")        