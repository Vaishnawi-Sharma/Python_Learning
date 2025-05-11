# Functions 

# re.findall()- Return all non- overlapping pattern matches in string , as a list of strings .The string is scanned left to right , and matches are returned in the order found . 

# re.compile() - Regular expressions are compiled into pattern objects , which have methods for various operations such as searching for pattern matches or performing string substitutions . 

# re.split() - Split string by the occurrences of a character or pattern , upon finding that pattern , the renaming characters from the string are returned as part of a resulting string . 

# re.sub() - The method returns a string where matched occurrences are replaced with the content of replace variable .

# re.subn() - subn() is similar to sub() in all ways , except int its way of providing output . It returns a tuple with a cout of the total of replacement and the new string rather than just a string .

# re.escape() - Returns string with all non-alphanumerics backslashed , this is useful if you want to match an arbitrary literal string that may have regular expression meta characters in it . takes only one parameter that is our string

# re.search() - This method either returns none(if the pattern does not match ) , or a re . This method stops after the first match , so this is best suited for testing a regular expression more than extracting data . 

import re 

b="Fantastic 5 turtules"
a="""John has scored 89 marks 
Lisa has scored 90 marks 
David has scored 70 marks """

print(re.findall("\d+",a)) # + is used of reoccurring occurrences

print(re.findall(r"[A-Z][a-z]*",a)) # * is used for reoccuring value

p = re.compile("[a-d]")
print(re.findall(p,a))

p = re.compile("\d+")
print(re.findall(p,a))

print(re.split("\d+",a))

print(re.split("\d+",b))

print(re.sub("\s+","",a))

print(re.sub("\s+","",b))

print(re.subn("\s+","",a))

print(re.escape(a))

print(re.search("\d+",a))


