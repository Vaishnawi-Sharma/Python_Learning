# Exercise 2
x= 'Shenanigan'
print(x[0],x[1])
print(x[-2],x[-1])
print(x[2:])
print(x[0:6])
print(x[:6])
print(x[-10:-4])
print(x[0:6:1])
print(x)
print(x[0:10:2])
print(x[0:10:3])
print(x[0:10:4])
print(x+'Type')
y='Wabbit'
print(x+y)

z='an inferior lawyer with dubious practices'
print(z.title())  # For each character should be in upper case

a="Light travels faster than sound .This is why some people appear bright until you hear them speak "
a=a.replace('Light','LIGHT').replace('sound','SOUND')
print(a)

#answer d).
#s= HumptyDumpty
#True
#False
#True
#False
#False
#True
#False

s='HumptyDumpty'
print('s =',s)
print(s.isalpha())
print(s.isdigit())
print(s.isalnum())
print(s.islower())
print(s.isupper())
print(s.startswith('Hump'))
print(s.endswith('Dump'))

#A raw string is used to retain characters like \ or " " or ' ' within a string
#The function chr() takes the ascii number and returns the value that are indexed of that number while ord() is just opposite it takes the value and returns the number
print(chr(70))
print(ord('M'))
# Yes , in ptyhon each string is treated as a object of built in type str .
print(type(s))

s1='The difference between stupidity and genius is that genius has its limits'
print(s1.split(' '))

msg = 'Keep yourself warm'
print(msg.partition(' '))

print(msg[-0])
print(msg[1:1:1])
print(msg[-1:3]) # Empty string
print(msg[-1:3:-1]) 

print(msg[:-3])
print(msg[0:-2])


# partition() method always returns a tuple with three elements—even if the separator isn't found in the string. This is a key characteristic of how partition() works in Python.

# If the separator exists in the string:

# The string is split into three parts: before, the separator, and after.

# If the separator does not exist, like in your example (text.partition(",") where , is missing):

# The entire string remains unchanged.

# The separator part is an empty string ("").

# The part after the separator is also an empty string ("").

print(dir(str))
print(help(str.partition))

help()