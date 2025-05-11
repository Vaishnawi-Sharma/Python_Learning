import re 
a="charlie chchchaplin coa and the choclate factory" 
b="ayushi.jain@gmail.com"
c="hello"
d="xyz,yz,xyzz,xyyz,xxzzy,zyz,xxyyyzz,xyz,xyzxyz"

# \ used to drop a special meaning of character following it
# [ ] represent a character class 
# ^ matches the beginning 
# $ Matches the end 
# . Matches any character except newline
# | Means OR (Matches with any of the character seperated by it)
# ? Matches zero or one occurrence
# * Any number of occurrences (including zero occurrences)
# + One or more occurrences
# { } Indicate the number of occurrences of a preceding regex to match 
# ( ) Enclose a group of regex


match = re.search(r"\.",b)
print(match)

match = re.search(r"[@]",b)
print(match)

match = re.search(r"[l]",b)
print(match)

match = re.findall(r"[l]",b)
print(match)

match = re.findall(r"[a]",b)
print(match)

match = re.search(r"^a",b) # carrot symbol ya circumflex
print(match)

match = re.search(r"^c",b) # None
print(match)

match = re.search(r"^ayu",b) # carrot symbol ya circumflex
print(match)

match = re.search(r"com$",b)  
print(match)

match = re.search(r"lo$",b)  # None
print(match)

match = re.findall(r"c.a",a)  
print(match)

match = re.findall(r"cha|fac",a)  
print(match)

match = re.search(r"rli|fac",a)  
print(match)

match = re.search(r"ch?a",a)  
print(match)

match = re.findall(r"ch?a",a)  
print(match)

match = re.search(r"ch*a",a)  
print(match)

match = re.findall(r"ch*a",a)  
print(match)

match = re.search(r"ch?a",a)  
print(match)

match = re.findall(r"xy+z",d)  
print(match)

match = re.findall(r"x{2,4}",d)  
print(match)

match = re.findall(r"y{2,4}",d)  
print(match)

match = re.findall(r"(x|z)yz",d)  
print(match)