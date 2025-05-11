email = input("Enter the Email: ")
a, b, c = 0, 0, 0

if len(email) >= 6:
    if email[0].isalpha():
        if ('@' in email) and (email.count('@') == 1):
            if email[-3] == '.' or email[-4] == '.':  
                for i in email:
                    if i.isspace():  
                        a = 1
                    elif i.isalpha():
                        if i.isupper():  
                            b = 1
                    elif i.isdigit():
                        continue
                    elif i in "@_.":
                        continue
                    else:
                        c = 1  

                if a == 1 or b == 1 or c == 1:
                    print("Wrong Email (Contains spaces, uppercase letters, or invalid symbols)")
                else:
                    print("Right Email")
            else:
                print("Wrong Email (. is not at the appropriate position)")
        else:
            print("Wrong Email (@ is missing or appears more than once)")
    else:
        print("Wrong Email (First letter is not an alphabet)")
else:
    print("Wrong Email (Length is less than 6)")


# Via Regex
# import re

# email = input("Enter the Email: ")

# # Regular expression for email validation
# pattern = r"^[a-zA-Z][a-zA-Z0-9_.]+@[a-zA-Z]+\.[a-zA-Z]{2,4}$"

# if re.match(pattern, email):
#     print("Right Email")
# else:
#     print("Wrong Email")
