# Key points
# enumerate function for indexes as well as data 
# tuple to string conversion via ".join(Tuple_name)
# operator.itemgetter() for sorting according to our choice or indexes
# datetime module date conversion method
# zip method for combining the list into a list of tuples
# conversion of list of tuples into seperate tuples and conversion of list of tuples into seperate lists 
# map function


# Exercise 
# c).
from datetime import date
date1=(12,5,2024)
date2 =(17,7,2025)

date_1=date(date1[2],date1[1],date1[0])
date_2=date(date2[2],date2[1],date2[0])

difference = date_2 - date_1

print("Difference =",difference)

# d).
import operator
lst=[('item1',53.60),('item2',67.60),('item3',45.50)]

sort = sorted(lst , key=operator.itemgetter(1))
print(sort)

# e).
tpl=(('Share1',(12-5-2024),2300,5,3500),('Share2',(17-5-2024),1700,20,1500))
print("Total Cost = ",((tpl[0][2]*5)+(tpl[1][2]*20)))
amount = ((tpl[0][4]*5)+(tpl[1][4]*20))-((tpl[0][2]*5)+(tpl[1][2]*20))
print("Total amount = ",amount )
profit = (amount / ((tpl[0][2]*5)+(tpl[1][2]*20)))*100
print("Prcentage Profit = ",round(profit,2))

# f).
lst = [(),('Radha',),('Sushma',),(9,),(1,), (), (2,), (), (3,), ()]

for i in lst :
    if i== ():
        lst.remove(i)
    else:
        pass
print(lst)    

# g).

lst_1=['Ramu','Pappu','Mukesh'] 
lst_2=[202345,30345,23456]
lst_3=[45.67,78.90,34.00]

combined = list(zip(lst_1, lst_2, lst_3))

all_names = tuple([item[0] for item in combined])

# Extracting all roll numbers
all_roll_numbers = tuple([item[1] for item in combined])

# Extracting all marks
all_marks = tuple([item[2] for item in combined])

# Print the results
print("All names:", all_names)
print("All roll numbers:", all_roll_numbers)
print("All marks:", all_marks)  
