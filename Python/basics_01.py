

# Use of integer types 
print(3+4)
print(3-4)
print(3*4)
print(3/4)
print(3//4)  #floor divison
print(3**4)  #exponentiation
print(3%4)
# Short hand assignment operator 
var1 = 3
var2= 8
var2 += var1
print(var2)
var2 -= var1
print(var2)
var2 /= var1
print(var2)
var2 *= var1
print(var2)
var2 //= var1
print(var2)
var2 **= var1
print(var2)
var2 %= var1
print(var2)
# Type conversion
print(int(3.1445678))
print(int('6789'))
print(int('1100',2))  #converts from binary to int
print(int('341',8))  #Converts from octal to decimal int
print(int('21',16))  #Converts from  hexadecimal to decimal int
print(float(2))
print(float('890567'))
print(type(complex(6)))  #Coverts to complex with imaginary part 0 
print(complex(6.70))  #Coverts to complex with imaginary part 0 
print(complex(6,9.65)) # converts to complex
print(bool(1.4))
print(bool(0))
print(bool(-6))
print(type(str(1)))
print(type(str(-1)))
print(type(str('1')))
print(chr(8))
b=1+2j
print(b.real)
print(b.imag)
print(b.conjugate)

#Built in functions
x=3.456
y=3
print(abs(x))# absolute value of x
print(pow(x,y))
print(min(x,y))
print(max(x,y))
print(divmod(x,y))# returns a pair (x//y , x%y)
print(bin(34)) #binary equivalent
print(oct(34)) #octal equivalent
print(hex(34)) #hexadecimal equivalent
print(round(x,2))

#Library functions
import math  #many useful mathematical functions
x=6.7982
print(math.pi,math.e)
print(math.sqrt(x))
print(math.factorial(5))#should be integer
print(math.fabs(x))
print(math.log(x))
print(math.log10(x))
print(math.exp(x))
print(math.trunc(x)) #for positive numbers floor() & for negative numbers ceil()
print(math.floor(x)) #rounds to negative infinity
print(math.ceil(x))  #rounds to positive infinity
print(math.modf(x))  #fractional and integer parts of x
print(math.trunc(-x)) #for positive numbers floor() & for negative numbers ceil()
print(math.floor(-x)) #rounds to negative infinity
print(math.ceil(-x))
#Trignometric functions in math module
print(math.degrees(x)) #radians to degrees
print(math.radians(x)) #degrees to radians
print(math.sin(x)) 
print(math.cos(x)) 
print(math.tan(x))
print(math.sinh(x)) #hyperbolic sine of x
print(math.cosh(x)) 
print(math.tanh(x))
print(math.asin(-1)) #arc sine or inverse the value should be betwwen -1 to 1(inclusive)
print(math.acos(1)) 
print(math.atan(.56))
print(math.hypot(3,4))#sqrt(x*x + y*y) returns value in float
print(math.hypot(3.4,5.6))

# cmath module - For performing operations on complex numbers
#decimal module - for precise arithmetic operations
import random
print(random.seed(6))
print(random.randint(1,3))
print(random.random())

# Questions
#answer 1 
a,b=3,4
print("Before swap a=",a," b=" , b)
a,b=b,a
print("After swap a=",a," b=" , b)

#answer2
import math
z=5.2
print(math.sin(z))
print(math.cos(z))
print(math.tan(z)) #No coses , sec , cot
print(math.sinh(z))
print(math.cosh(z))
print(math.tanh(z))
print(math.asin(.67))
print(math.acos(.67))
print(math.atan(.67))
print(math.hypot(5,6))
#answer3
import random
random.seed(6)
for i in range(1,7):
    print(random.randint(10,50))
    random.seed(i)
    
#answer4
import math
print(math.trunc(-2.8)) 
print(math.floor(-2.8)) 
print(math.ceil(-2.8)) 
print(math.trunc(-.5)) 
print(math.floor(-.5)) 
print(math.ceil(-.5)) 
print(math.trunc(.2)) 
print(math.floor(.2)) 
print(math.ceil(.2)) 
print(math.trunc(1.5)) 
print(math.floor(1.5)) 
print(math.ceil(1.5)) 
print(math.trunc(2.9)) 
print(math.floor(2.9)) 
print(math.ceil(2.9)) 
#answer5
bs=40000
gs=bs+bs*(40/100) + bs*(20/100) #gs=bs+da+hra+ca
print("Gross salary =" ,gs)

#answer f
# dis_km= int(input("Enter the distance in km :"))
# dis_m = dis_km * 1000 
# dis_cm = dis_km * 100000
# dis_feet = dis_km * 3280
# dis_inch = dis_km *39370
# print("Distance km :" , dis_km)
# print("Distance m :" , dis_m)
# print("Distance cm :" , dis_cm)
# print("Distance feet :" , dis_feet)
# print("Distance inch :" , dis_inch)

#answer g
# temp_farhenite=float(input("Enter temperature in farhenite :"))
# temp_celcius=float(5*(temp_farhenite-32)/9)
# print("temp_farhenite = " , temp_farhenite,"F")
# print("temp_celcius = ",temp_celcius,"C")

# question B
# a).
b=2+3j
print(b.imag)
# b).
b=4+2j
print(b.conjugate())
#c).
print(int('1100001110',2))
#d).
print(str(4.33))
#e).
print(divmod(29,5))
#f).
print(hex(34567))
#g).
print(round(45.6782,2))
#h).
import math
print(math.ceil(3.556))
#i).
import math
print(math.ceil(16.7844))
#j).
print(3.45%1.22)


import keyword
print(keyword.kwlist)

import math
print(dir(math))
print(help(math.asin))

print(dir(__builtins__))
help()