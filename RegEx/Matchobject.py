import re 

a= 'John has scored 98 marks '

match = re.search("\d+",a)
print(match)
print(match.re)
print(match.string)
print(match.start())
print(match.end())
print(match.span())
print(match.group())

match = re.search("\w{2} s",a)
print(match)
print(match.re)
print(match.string)
print(match.start())
print(match.end())
print(match.span())
print(match.group())