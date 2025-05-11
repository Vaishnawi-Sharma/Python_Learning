import re 

phn ="222-444-8787"

if re.search("\d{3}-\d{3}-\d{4}",phn):
    print('It is a verified number ')
else :
    print("Incorrect number")    

email = "john78@gmail.com john@.com david.989@yahoo.com"

print(re.findall("[\w._%]{0,20}@[\w-].[A-Za-z]{2,3}",email))

print(len(re.findall("[\w._%]{0,20}@[\w-].[A-Za-z]{2,3}",email)))

# Web Scraping

import urllib.request
from re import findall 

# url = ""

# a=urlib.request.urlopen(url)
# html = a.read()
# htmlstr=html.decode()
# phn = findall("\(\d{3}\) \d{3}-\d{4}",htmlstr)