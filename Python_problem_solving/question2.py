day = input(" Enter the day today :")
age = int(input("Enter Your age :"))
discount = 0 
if(day.lower() == 'wednesday'):
    discount = 2 
else :
    discount = 0 

if (age >= 18 ):
    ticket_price = 12 
else :
    ticket_price =  8    

total = ticket_price - discount
print(f"Your ticket price is : { total }$")