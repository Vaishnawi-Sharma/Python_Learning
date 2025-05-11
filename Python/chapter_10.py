# Exercise
# B).
# a).
s={'Anand','Bhoomi','Bhawna','Aniruddh','Aaditya','Bharya'}
s_a=set()
s_b=set()
for i in s :
    if i.startswith('A'):
        s_a.add(i) 
    else :
        s_b.add(i) 
print(s_a)    
print(s_b)   
# b).     
# Initialize an empty set
# s = set()

# # Loop to get 5 names from the user
# for i in range(5):
#     name = input('Enter the name: ')
#     s.add(name)

# # Print the set of names
# print("Original set:", s)

# # Modify one name (remove an existing one and add a new one)
# name_to_modify = input('Enter a name to modify (an existing name): ')
# new_name = input('Enter the new name: ')

# if name_to_modify in s:
#     s.remove(name_to_modify)  # Remove the specified name
#     s.add(new_name)           # Add the new name
# else:
#     print(f"{name_to_modify} is not in the set!")

# # Print the updated set after modification
# print("Set after modification:", s)

# # Remove two names from the set
# names_to_remove = []
# for i in range(2):
#     name = input(f'Enter name {i+1} to remove: ')
#     names_to_remove.append(name)

# for name in names_to_remove:
#     if name in s:
#         s.remove(name)  # Remove the name
#     else:
#         print(f"{name} is not in the set!")

# # Print the final set after removal
# print("Final set after removal:", s)

# c).
# import random

# # Initialize an empty set
# s = set()

# # Populate the set with 10 random integers between 15 and 46
# for i in range(10):
#     num = random.randint(15, 46)
#     s.add(num)

# print("Original set:", s)

# # Initialize a count for numbers less than 30
# count = 0

# # Create a list to store items to remove
# to_remove = []

# # Iterate over the set and check conditions
# for i in s:
#     if i < 30:
#         count += 1  # Count numbers less than 30
#     elif i > 35:
#         to_remove.append(i)  # Add numbers greater than 35 to removal list

# # Remove the collected items from the set
# for item in to_remove:
#     s.remove(item)

# print("Count of numbers less than 30:", count)
# print("Updated set:", s)

# d). 
# List: Remove duplicates
lst = [10, 2, 6, 10, 4, 6, 7, 8, 9, 2, 8, 7, 8, 7]
new_lst = []
for i in lst:
    if i not in new_lst:
        new_lst.append(i)
print("New list without duplicates:", new_lst)

# String: Remove duplicate characters
original_str = "aiahgjklghfjsksd"  # Renamed variable
new_str = ''
for char in original_str:
    if char not in new_str:
        new_str += char  # Append unique characters
print("New string without duplicate characters:", new_str)

# Tuple: Remove duplicates
tpl = (10, 2, 6, 10, 4, 6, 7, 8, 9, 2, 8, 7, 8, 7)
new_tpl = ()
for i in tpl:
    if i not in new_tpl:
        new_tpl += (i,)  # Add unique items as a tuple
print("New tuple without duplicates:", new_tpl)
