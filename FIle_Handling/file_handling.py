# import os
# os.chdir(r"c:\Users\bhard\OneDrive\Documents\Python\FIle_Handling")
# print(os.getcwd())
# f1=open("file1.txt",'r')
# print(f1.read())
# print(f1.tell())

# f2=open("file1.txt",'w')
# f2.write("Why are you so upset ??")
# f2.write("Don't be upsate , time is changed")

# f3=open("file1.txt",'a')
# print(f3.tell())
# f3.write("Yahooooo !")

import os
os.chdir(r"c:\Users\bhard\OneDrive\Documents\Python\FIle_Handling")
print(os.getcwd())


f1=open("file1.txt","a")
print(f1.tell())
f1.write("Yahooooo  !")
print(f1.tell())




















