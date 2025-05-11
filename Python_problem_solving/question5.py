weather=input("Enter the current weather situation(Sunny/Snowy/Rainy) :") 
if(weather.lower()=='sunny'):
    print("Go for a walk !")
elif(weather.lower()=='snowy'):
    print("Build a Snowman !")
elif(weather.lower()=='rainy'):
    print("Read a book !")
else: 
    print("Please enter a correct weather situation !")