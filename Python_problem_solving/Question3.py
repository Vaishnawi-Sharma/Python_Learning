Marks = int(input("Enter your Marks out of 100 : "))
if Marks>100 :
    print("Please Verify Your Marks Again :")
    break 
else:
    if 90<=Marks<=100 :
        print("Grade : A")
    elif 80<=Marks<90 :
        print("Grade : B")
    elif 70<=Marks<80 :
        print("Grade : C") 
    elif 60<=Marks<70:
        print("Grade : D") 
    else :
        print("Grade : E")          
    
