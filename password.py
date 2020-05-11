import re

# TODO: use getpass instead of input(), it does not echo the typed password
# https://docs.python.org/2/library/getpass.html
p=string( input("Enter password"))
# TODO: Separate function to validate_password
x = True
while x:

    # TODO: Read about re.compile and re.match 
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
    # TODO: Why not valid. Would be better to give reason. Would help user to enter a valid password on next try
    print("Not a Valid Password")
