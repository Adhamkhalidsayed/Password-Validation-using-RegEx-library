import re

def passwordValidation(password):
    #check for the length of the password
    if len(password) < 8:
        return False

    
    #password must contain one uppercase letter at least
    if not re.search(r"[A-Z]", password):
        return False
    
    #password must contain one lowercase letter at least
    if not re.search(r"[a-z]", password):
        return False

    #password must contain one digit at least
    if not re.search("\d", password):
        return False
    
    #password must contain on special character at least
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return False
    
    return True

while True:
    password = input("Input your password: ")
    pass_is_valid = passwordValidation(password)

    if pass_is_valid:
        print("Password accepted")
        break
    else:
        print("Password is not accepted, Try again!")




