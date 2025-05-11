#Problem 8.1
# list = ['Anil','Amol','Aditya','Avi','Alka']
# print(list)
# list.insert(2,'Anuj')
# print(list)
# list.append('Zulu')
# print(list)
# list.remove('Avi')
# print(list)
# list[0]=list[0]+'Kumar'
# print(list)
# list.sort()
# print(list)
# list.reverse()
# print(list)
# Problem 8.2
list1=[1,3,5,7,9]
list2=[2,4,6,8,10]
list3=list1+list2
print(list3)
list3=[11,17,29]+list3
print(list3)
print(len(list3))
list3[len(list3)-3:len(list3)]=[100,200,300]
print(list3)
del(list3[:])
print(list3)
# del(list3)
# print(list3)

# Problem 8.3
s=[]
s.append(10)
s.append(20)
s.append(30)
s.append(40)
s.append(50)
print(s)

print(s.pop())
print(s.pop())
print(s.pop())
print(s)
#Problem 8.4
import collections
q = collections.deque()
print(q)
q.append("Suhana")
q.append("Shabana")
q.append("Shakila")
q.append("Shakira")
q.append("Sameera")
print(q)

print(q.popleft())
print(q.popleft())
print(q.popleft())

print(q)
#Problem 8.5
import random
list4=[]
for i in range(0,20):
    num=random.randint(10,100)
    list4.append(num)
    i+=1
print(list4)    
count=0
for num in list4 :
    if num>20 and num <50 :
        list4.remove(num)
        count+=1
print(list4)
print(count)

#Problem 8.6
mat1 =[[1,2,3,4],[5,6,7,8],[9,10,11,12]]
mat2 =[[1,2,3,4],[5,6,7,8],[9,10,11,12]]
mat3 =[[0,0,0,0],[0,0,0,0],[0,0,0,0]]

for i in range(len(mat1)):
    for j in range(len(mat1[0])):
        mat3[i][j]=mat1[i][j]+mat2[i][j]
print(mat3)        

# Exercise

s=list('OnlineCourses')
print(s)

num=[10,20,30,40,50]
num[2:4]=[]
print(num)

num1=[60,70,80]
num.append(num1)
print(num)

lst=[10,25,4,12,3,8]
lst=sorted(lst)
print(lst)

a=[1,2,3,4]
b=[1,2,5]
print(a<b)

s=list("Hello")
s[1]='M'
print(s)

num=[10,20,30,40,50]
num.remove(30)
num.remove(40)
print(num)
a=[10,'Suraj',3450.55]
print(a)
a=[0,1,2,3,[10,20,30]]
print(a)
a=[[10,20,30],[40,50,60]]
print(a)

num1=[10,20,30,40,50]
num1=list('ABC')+num1+list('YZ')
print(num1)

lst=[10,25,4,12,3,8]
print(sorted(lst,reverse=True))
print(30 in lst)
print(lst.insert(2,30))
print(lst)

s='Hello'
print(list(s))


# extend() unpacks and adds each element from the iterable directly.

# append() treats the iterable as a single object and adds it as one element.
odd=[1,3,5,7,9]
even=[2,4,6,8]
odd[3]=even
print(odd)
flattend_list=[]
for item in odd :
    if isinstance(item,list):
        flattend_list.extend(item)
    else :
        flattend_list.append(item)    
print(flattend_list) 
print(sorted(flattend_list))

# Answer b).
# import random 
# lst=[]
# for i in range(0,20):
#     num=random.randint(1,100)
#     lst.append(num)
    
# print(lst)    
# number=int(input("Enter the number :")) 
# idx=[]
# for i in range(len(lst)):
#     if number==lst[i]:
#         idx.append(i)

# if idx :
#     print(idx)
# else :
#     print("The number is not present") 

# answer c).
import random 
lst=[]
for i in range(0,20):
    num=random.randint(1,100)
    lst.append(num)
    
print(lst)    

unique_lst = []  # New list to store unique elements
for item in lst:
    if item not in unique_lst:
        unique_lst.append(item)  # Add only if not already in the unique list

print(unique_lst)
 
# answer d).
lst =[-1, 3, 5, 7 , -6, 8,-9,3,5,8,-6,-7,-10]
pos=[]
neg=[]
for i in lst :
    if i < 0 :
        neg.append(i)
    elif i>0 :
        pos.append(i)
print(pos)
print(neg)

# Answer e).
lst=["amrit",'shweta',"pushpa",'kavita','guddo']
lst1=[]
for i in lst :
    lst1.append(i.upper())
print(lst1)    

# answer f).
lst_f=[99.8 ,98.6,100.0,97.6]
lst_c =[]
for i in lst_f :
    num=round((((i-32)*5)/9),2)
    lst_c.append(num)
    
print(lst_c)   

# Answer g).
# lst =[4,2,8,6,0,7,5,9,3,2,8,5,9]
# length = len(lst)
# sort = sorted(lst)
# print(sort)
# idx = length//2
# median=sort[idx]
# print(median)

# lst=[4,2,8,6,0,7,5,9,3,2,8,5]
# length = len(lst)
# print(length)
# sort = sorted(lst)
# print(sort)
# idx=length//2
# median=(sort[idx-1]+sort[idx])/2
# print(median)

lst = [4, 2, 8, 6, 0, 7, 5, 9, 3, 2, 8, 5]
length = len(lst)
print("Length of the list:", length)

sort = sorted(lst)
print("Sorted list:", sort)

idx = length // 2  # Middle index

# Calculate median
if length % 2 == 0:  # Even-length list
    median = (sort[idx - 1] + sort[idx]) / 2
else:  # Odd-length list
    median = sort[idx]

print("Median:", median)

# answer h)
lst =[-1, 3, 5, 7 , -6, 8,-9,3,5,8,-6,-7,-10]
count=0
for i in lst :
    if i <0 :
        count += 1 
print(count)

# Answer i).
lst=["amrit",'shweta',"pushpa",'kavita','guddo']
lst1=[]
for i in lst :
    lst1.append(i[0])
print(lst1)

# Answer j).
lst =[10,6,3,6,7,8,9,3,4,0,2,1,0,10,456,78,99]
lst_unique =[]
for i in lst :
    if i not in lst_unique :
        lst_unique.append(i)
print(lst_unique)

# Answer K).
lst =[10,6,3,6,7,8,9,3,4,0,2,1,0,10,456,78,99]
mean = round((sum(lst))/len(lst) ,2)
print("mean = " , mean)  


length = len(lst)
sort = sorted(lst)
idx = length //2
if length % 2  == 0 :
    median = (sort[idx-1]+ sort[idx])/2
else :
    median = sort[idx] 
print("median = " , median)  


# Create a dictionary to count occurrences of each element
frequency = {}
for num in lst:
    if num in frequency:
        frequency[num] += 1  # Increment the count if the number is already in the dictionary
    else:
        frequency[num] = 1  # Initialize the count for the number

# Find the maximum frequency
max_count = max(frequency.values())

# Find all elements with the maximum frequency (the modes)
modes = [key for key, value in frequency.items() if value == max_count]

print("Mode(s):", modes)

