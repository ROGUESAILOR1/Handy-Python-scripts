import re

def check():
    while True:
        s=input("Enter your password: ")
        if len(s)<8:
            print("Password must be more than or equal to 8 characters")
        elif re.search(r'[A-Z]', s) is None:
            print("Password must contain at least one uppercase letter")
        elif re.search(r"[!@|~`#$%+*?<>=]",s) is None:
            print("Password must contain at least one special character")
        elif re.search(r'\d', s) is None:
            print("password must contain at least one digit")
        else:
            print("Password is invalid")
            break

check()