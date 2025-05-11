# Regex Sets 

# [atx] - Returns a match where one of the specified characters (a ,t ,or x) are present 

# [a-h] - Returns a match for any lower case character , alphabetically between a and h .

# [^atx] - Returns a match for any character except a , t , and x .

# [0123] - Returns a match where any of the specified digits (0,1,2,3) are present 

#[0-9] - Returns a match for any digit between 0 and 9 .

# [0-7][0-9] - Returns a match for any two-digit numbers from 00 to 79 .

# [a-z A-Z] - Returns a match for any character alphabetically between a and z in lower case and A and Z in upper case .

# [+] - In sets , +,*,.,|,(),$,{} has no special meaning .

import re 

a = "charlie and the choclate factory"

match = re.findall("[atx]",a)
print(match)

match = re.findall("[^atx]",a)
print(match)

match = re.findall("[a-t]",a)
print(match)

match = re.findall("[atx]",a)
print(match)

b="12hi3john#$@^67HELLO7356"

match= re.findall("[12346]",b)
print(match)

match= re.findall("[0-9]",b)
print(match)

match= re.findall("[0-7][0-9]",b)
print(match)

match= re.findall("[a-zA-Z]",b)
print(match)

match= re.findall("[$^]",b)
print(match)

