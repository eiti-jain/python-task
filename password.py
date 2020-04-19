import re
p=string( input("Enter password"))
x = True
while x:

    if not re.search("[a-z]",p):
        break
    elif not re.search("[A-Z]",p):
        break
    elif not re.search("[0-9]",p):
        break
    elif not re.search("[$#@%]",p):
        break
    elif (len(p)<6):
        break
    else:
        print("Valid Password")
        x=False
        break

if x:
    print("Not a Valid Password")
