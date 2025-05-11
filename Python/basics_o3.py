# Exercise
a=2
b = 10 if a<10 else 20
print("b =" ,b)  # Print does not support direct assignment inside it

time=8
print('Status = ','Morning' if time<12 else 'Afternoon')

x=3 
y=3.0 
print('x and y are equal' if x==y else 'x and y are not equal')# == only checks value equality
print(type(x)==type(y))

i,j,k=4,-1,0
w=i or j or k
x=i and j and k
y=i or j and k
z=i and j or k 
print(w,x,y,z)  #
# w = i or j or k
# The or operator returns the first truthy value or the last value if none are truthy.

# i (4) is a truthy value, so w = 4.

# x = i and j and k
# The and operator returns the first falsy value or the last value if all are truthy.

# i (4) and j (-1) are truthy, but k (0) is falsy, so x = 0.

# y = i or j and k
# and has higher precedence than or, so j and k is evaluated first.

# j and k → -1 and 0 → The first falsy value is 0.

# Now, i or 0 → 4 or 0, and since 4 is truthy, y = 4.

# z = i and j or k
# and has higher precedence than or, so i and j is evaluated first.

# i and j → 4 and -1 → Since both are truthy, it returns the last value -1
#Now, -1 or k → -1 or 0, and since -1 is truthy, z = -1

a=10
a=not not a 
print(a)

x,y,z=20,40,45
if x>y and x>z:
    print("Biggest = ",str(a))
elif (y>x and y>z):
    print("Biggest = ",str(b)) 
elif (z>x and z> y):
    print("Biggest = ",str(z))       # else is not necessary 

num =300
k=100 if num<=10 else 500
print(k)  #500

# Answer C).
a=12.25 
b=12.52
if a==b :
    print('a and b are equal')

if ord('X')<ord('x'):
    print("Unicode value of X is smaller than that of x")

x=10
if x>=2 :
    print('x')    

x=10 ; y= 15 
if x%2 ==y%3 :
    print("Carpathians")

x,y=30,40
if x==y :
    print("x is equal to y")
elif x>y :
    print('x is greater than y')  
elif x<y :
    print("x is less than y ")      

# Answer D).   
a,b,c=10,12,0
print(a!=6 and b >5)
print(a==9 or b<3)
print(not(a<10))
print(not(a>5 and c))
print(5 and c!=8 )

# Answer E). 
# a).
s =("Nagpur-440010")
alpha=0
digit=0
i=0
for char in s :
    if char.isalpha() :
        alpha+=1
    elif char.isdigit() :
        digit+=1
print("Alphabet = ", alpha)  
print("Digit = ",digit)     

# b).
number = 0
if(number%2==0 and number!=0):
    print("Even")
elif(number%2!=0):
    print("Odd")
else :
    print("Zero")    
        
# c).
year=2024

if year%4==0 :
    if(year%100==0):
        if(year%400==0):
            print("Leap year")
        else :
            print("No leap year")    
    else :
        print("leap year")
else :
    print("No leap year")        

# d).
# number=34256
# reverse=number[::-1]
# count=len(number)

# if (count==5 ) :
#     if int(number)==int(reverse):
#         print("Equal")
#     else :
#         print("Not equal") 
# else :
#     print("Enter a valid number")   

# e).
# age_ram=int(input("Enter the age of Ram :"))
# age_shyam=int(input("Enter the age of Shyam :"))
# age_mohan=int(input("Enter the age of Mohan :"))
# if(age_ram<age_shyam and age_ram<age_mohan):
#    print("Ram is Youngest ")
# elif(age_shyam<age_ram and age_shyam<age_mohan):
#     print("Shyam is youngest")   
# else :
#     print("Mohan is youngest")     

# f).    

# angle_1 = int(input("Enter the first angle "))
# angle_2 = int(input("Enter the second angle"))
# angle_3 = int(input("Enter the third angle "))
# if angle_1 + angle_2 + angle_3 ==180 :
#     print("Triangle is valid")
# else :
#     print("Triangle is invalid ")    

# g).

# number=float(input("Enter a number :")) #The absolute value of a number is its distance from zero on the number line, regardless of direction. It always results in a non-negative value
# print(abs(number))   

# h).
# length=int(input("Enter the length of rectnagle "))
# width=int(input("Enter the width of rectnagle "))
# area=length*width
# perimeter = 2*(length+width)
# if area >perimeter :
#     print("Greater than perimeter")
# else :
#     print("Not greater than perimeter")    

#i).
# x1,y1 =map(int,input("enter the value of x1 and y1 ").split(" "))#The map() function in Python is used to apply a function to every item in an iterable (like a list or tuple) without needing a loop. It’s particularly useful for transforming data efficiently.
# x2,y2 =map(int,input("enter the value of x2 and y2 ").split(" "))
# x3,y3 =map(int,input("enter the value of x3 and y3 ").split(" "))
# area = x1*(y2-y3)+x2*(y3-y1)+x3*(y1-y2)
# if(area ==0):
#     print("the points are co-linear")
# else :
#     print("Not co-linear")   

# J).
# import math
# h,k = 0,0
# r=5 
# x,y=map(int,input("Enter the value of x and y").split(" "))
# dis=math.sqrt(math.pow((x-h),2) + math.pow((y-k),2))
# if dis< r :
#     print("Point is inside the circle")
# elif dis==r :
#     print("Point is on the circle ") 
# elif dis>r :
#     print("Point is outside the circle ")       

# K).
# x,y = map(int,input("Enter x and y :").split(" "))
# if x==0 and y==0 :
#     print("On the origin")
# elif x==0 :
#     print("On the x-axis ")   
# elif y==0 :
#     print("On the y-axis ") 
# else :
#     print("Not on any axis or origin") 

# L).
year=2000

if year%4==0 :
    if year %100==0 and year%400==0 :
        print("Leap year")
    elif year %100!=0   :
        print("Leap year") 
    else :
        print("No leap year")
else :
    print("No leap year")   

#year = 2000
# if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
#     print("Leap year")
# else:
#     print("No leap year")
    
# m).
# a= int(input("Enter side 1 :"))
# b = int(input("Enter side 2 :"))
# c = int(input("Enter side 3 :"))
# if (a+b>c)and(b+c>a)and(a+c>b):
#     print("Triangle is valid")
# else :
#     print("Invalid") 
       
# n). 
# a= int(input("Enter side 1 :"))
# b = int(input("Enter side 2 :"))
# c = int(input("Enter side 3 :"))
# if (a==b==c):
#     print("Equilateral")
# elif a == b or b == c or a == c:
#     print("Isosceles Triangle")
# else:
#     print("Scalene Triangle")

# # Check if it's a right-angled triangle using Pythagorean theorem
# if (a**2 + b**2 == c**2) or (b**2 + c**2 == a**2) or (a**2 + c**2 == b**2):
#     print("Right-Angled Triangle")
# o).
# for i in range(10) :
#     working_hours=int(input(f"Enter the number of hours for employee {i+1}:"))
#     if(working_hours >= 40):
#         extra_hours= working_hours - 40
#         overtime_pay = extra_hours * 12 
        
#     else :
#         overtime_pay = 0 
#     print("Overtime pay = ",overtime_pay)

# P).
# num = int(input("Enter the number: "))

# if num < 0:
#     print("Factorial is not defined for negative numbers.")
# elif num == 0:
#     print("Factorial of 0 is 1.")  # Since 0! = 1
# else:
#     fact = 1
#     while num > 0:
#         fact *= num
#         num -= 1
#     print("Factorial =", fact)

# Q).
# for i in range(501):  
#     num_str = str(i)  # Convert number to string for indexing
#     num_len = len(num_str)  # Get the number of digits
#     armstrong_sum = sum(int(digit)**num_len for digit in num_str)  # Sum of digits raised to power of length

#     if armstrong_sum == i:
#         print(i)  # Print Armstrong number
# R). 
# count=0
# for i in range(301):
#     if i > 1:
#         for j in range(2, int(i**0.5) + 1):  # Check divisibility up to sqrt(num)
#             if i % j == 0:
#                 break
#         else:
#             print(f"{i}")
#             count+=1
# print(count)

# S).
# num=int(input("Enter a number :"))
# for i in range(10):
#     print(num," * ",i+1," = ",num*(i+1))

# T).
# for i in range(10)   :
#     p=int(input("Enter the principal amount in Rupees:"))
#     r=int(input("Enter the rate of interest % :"))/100
#     n=int(input("Enter the no. of years :"))
#     q=int(input("Enter number of times compounded per year :"))
#     a= p*(1+(r/q))**(n*q)
#     print("A = " ,a)
# U). 
# for a in range(1, 31):  # Side 1
#     for b in range(a, 31):  # Side 2 (starts from a to avoid duplicates)
#         for c in range(b, 31):  # Side 3 (hypotenuse)
#             if a**2 + b**2 == c**2:  # Pythagorean condition
#                 print(f"Triplet: ({a}, {b}, {c})")

# V).
# pop=100000
# for i in range(10,0,-1):
#     print(f"At the end of {i}th year , population is {round(pop,2)}")
#     pop-=pop*.1

# W).

# 1729=1**3+12**3=9**3+10**3

# X).
# for i in range(1,25):
#     if i < 12:
#         print(f"{i} AM")
#     elif i ==12 :
#         print(f"{i} Noon") 
#     elif i >12 and i != 24 :
#         print(f"{i-12} PM")   
#     elif i == 24 :
#         print(f"{i-12} Mid Night")        