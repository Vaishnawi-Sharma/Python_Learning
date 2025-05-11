# Special Sequence 

# \A - Matches if the string begins with the given character 

# \b  - Matches if the word begins or ends with the given character . \b (string) will check 
# for the beginning of the eord and (string)\b  will check for the ending of the word 

# \B - It is opposite of the \b  i.e. the string should not start or end with the given regex

# \d - Matches any decimal digit , this is equivalent to the set class[0,9]

# \D - Matches any non-digit character , this is equivalent to the set class[^0-9]

# \s - Matches any whitespace character .

# \S - Matches any non-whitespace character .

# \w - Matches any alphanumeric character , this is equivalent to the class [a-z, A-Z ,0-9]

# \W - Matches any non-alphanumeric character 

# \Z - Matches if the string ends with the given regex .

import re 

a="harry potter"

match = re.search(r'\Ahar',a)
print(match)

match = re.search(r'\Apot',a)
print(match) # None 

match = re.search(r'\bh',a)
print(match) 

match = re.search(r'r\b',a)
print(match) 

match = re.search(r'\Br',a)
print(match) 

match = re.search(r'ha\B',a)
print(match) 

a="harry1 potter2345"
match = re.findall(r'\d',a)
print(match)

match = re.findall(r'\D',a)
print(match)

a="harry1 potter @2345"
match = re.findall(r'\s',a)
print(match)

match = re.findall(r'\S',a)
print(match)

match = re.findall(r'\w',a)
print(match)

match = re.findall(r'\W',a)
print(match)


match = re.search(r'5\Z',a)
print(match)

match = re.findall(r'h\Z',a)
print(match) # [] 









