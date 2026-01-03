# Container is an entity in which we can store multiple data items.
# Container Data types : 
# Lists, Tuple, Set, Dictionary 

# Null List
# a = []

# Python Lists : 
# a = [3, 4, 5, 7, 8] # Similar data type data items 

# a = ["Shyam", 3, 4.5, True] # Data items of multiple data types 

# Lists are called as dyanamic array : The ability to grow and shrink during the time of execution 

# List is a sequence types: 
# a = [4, 5, 6]
# print(a[2])
# Strings, Lists, Tuple

# Duplicates 
# a = ['a'] * 5
# print(a)

# Indexing 
#a = ["Shyam", 3, 4.5, True]
# print(a[1])
# print(a[1:2]) # start:stop - 1:step 
# print(a[1:3])
# print(a[0:4:2])

# Iteration  - Loops 
# a = ["Shyam", 3, 4.5, True]

# i = 0
# while i < len(a):
#     print(a[i])
#     i +=1

# for i in range(0, 4):
#     print(a[i])

# for i in a:
#     print(i)

# Enumerate : for doing iteration with indexing 
# a = ["Shyam", 3, 4.5, True]

# for index, i in enumerate(a):
#     print(index, i)

# print(a[:])
# print(a[1:])
# print(a[:3])
# print(a[-1])
# print(a[-3:-1]) # -1-1 = -2
# print(a[-1:-3])
# print(a[-1:])
# print(a[::-1])

# Basic list operations 
# 1. Mutable
# 2. Concatenation
# 3. Merging
# 4. Conversion
# 5. Alaising or Shallow copying
# 6. Cloning or Deep copying 
# 7. Searching
# 8. Identity 
# 9. Empty 
# 10. Comparison 

# Mutable 
# a = "Shyam"
# print(a[1:4]) # Sequence data type 
# a[3] = 'b'
# print(a)    # immutable data type 

# lst = [3, 6, "Rita", 4.5]
# lst[2] = "Kavita"
# print(lst)


# Concatenation 
# lst = [1, 2, 3]
# lst_1 = lst + [4, 5]
# print(lst_1)

# Merging 
# lst_1 = [1, 2, 3]
# lst_2 = [4, 5, 6]
# lst = lst_1 + lst_2
# print(lst)

# Conversion 
# str/tpl/set  --> List 
# str = "Rashmika"
# print(list(str))

# tpl = (2, 4, 5, "Sam", 3.9) # 
# print(list(tpl))

# set = { 1, 3, 5, 6 }
# print(list(set))

# Shallow copying or aliasing 
# Assigning of one list to another in memeory will reference the data items of the assigned list 
# lst = [ 1, 2, 3]
# lst_1 = lst 
# print(lst)
# print(lst_1)

# print(lst is lst_1)

# lst_1[2] = 5
# print(lst)
# print(lst_1)

# Deep copying or cloning 
# lst = [2, 3, 4, 5 ]
# lst1= [] + lst

# print(lst)
# print(lst1)
# print(lst is lst1)

# Searching 
# Membership operators - in / not in 
# lst = [1, 2 , 3, 4]
# print(1 in lst)

# print(6 not in lst)

# Identity 
# lst = [1, 2, 3, 4]
# lst_1 = [1, 2, 3, 4]
# lst_2 = lst 
# print(lst is not lst_1)
# print(lst is not lst_2)

# a = "Srashti"
# b = "Srashti"
# print(a is b )

# Comparision 

# lst_1 = [5, 6, 7, 4]
# lst_2 = [5, 6, 3, 8]
# print(lst_2 > lst_1)

# Emptiness
# lst = []
# # if not lst :
# #     print("Empty")
# print(bool(lst))

# Built in fuctions of lists 
# len()
# max()
# min()
# sum()
# all()
# any()
# sorted()
# del()
# reversed()

# len()
# lst = [1, 2, 3, 4, 5, 6]
# print(len(lst))

# max()
# lst = [1, 2, 3, 4, 5, 6]
# print(max(lst))

# min()
# lst = [1, 2, 3, 4, 5, 6]
# print(min(lst))

# sum()
# lst = [1, 2, 3, 4, 5, 6]
# print(sum(lst))

# all()
# lst = [1, 2, 3, 4, 0, 6]
# print(all(lst))

# any()
# lst = [1, 0, 0]
# print(any(lst))

# del() - deletion - single data item, sliced data items, the whole list 
# lst = [1, 2, 3, 4, 5, 6]
# del(lst[3]) # [1, 2, 4, 5, 6]
# print(lst)

# del(lst[2:4]) #[1, 2, 6]
# print(lst)

# del(lst[:])
# print(lst)

# sorted 
# lst = [4, 6, 2, 3, 7, 1, 8, 9, 0]
# sorted(lst)
# print(lst)

# reversed 
# lst = [4, 6, 2, 3, 7, 1, 8, 9, 0]
# print(list(reversed(lst)))

# Sorted & Reversed list 
# lst = [4, 6, 2, 3, 7, 1, 8, 9, 0]
# print(sorted(lst, reverse = True))


# list Methods 
# append()
# remove()
# pop()
# insert()
# count()
# index()
# sort()
# reverse()

# Syntax -->  list.method()

# append()
# lst = [1, 2, 3, 4, 5]
# lst.append(6)
# print(lst)

# remove()
# lst = [1, 2, 3, 4, 5]
# lst.remove(3)
# print(lst)

# pop()
# lst = [1, 2, 3, 4, 5]  # by default it removes from last
# lst.pop()
# print(lst)

# lst.pop(1) # index of list in input 
# print(lst)

# insert(index, item)
# lst = [1, 2, 3, 4, 5]
# lst.insert(1, 9)
# print(lst)

# count()
# lst = [1, 2, 3, 4, 5, 4, 4, 4, 4, 4, 5, 6, 7, 8]
# print(lst.count(4))

# index()
# lst = [1, 2, 3, 4, 5, 4, 4, 4, 4, 4, 5, 6, 7, 8]
# print(lst.index(4))

# sort 
# lst = [1, 2, 3, 4, 5, 4, 4, 4, 4, 4, 5, 6, 7, 8]
# lst.sort()
# print(lst)

# reverse 
# lst = [1, 2, 3, 4, 5, 4, 4, 4, 4, 4, 5, 6, 7, 8]
# lst.reverse()
# print(lst)

# Sort & Reverse 
# lst = [1, 2, 3, 4, 5, 4, 4, 4, 4, 4, 5, 6, 7, 8]
# lst.sort(reverse = True)
# print(lst)


# Variety of lists 

# Nested list : List inside List 

# lst_1 = [1, 2, 3, 4]
# lst_2 = [2, 6, 7, 88]
# lst =[lst_1, lst_2]
# print(lst) #[[1, 2, 3, 4], [2, 6, 7, 88]]
# print(lst[1][3])

# Unpacking of lists and strings 
# lst =[1, 2, 3, 4]
# str = "Radhika"
# lst_1 = [*lst]
# print(lst_1)

# lst_2 = [*str]
# print(lst_2)

# lst_1 =[1, 2]
# lst = [3, 4, 5, 6, lst_1, 9]
# print(lst)