"""Peter Humphris"""

MIN_LENGTH = 5

def main():
    print("Please enter a valid password.")
    print("A valid passowrd contains at least 5 characters")
    password = input("> ")
    while not password_validation(password):
        print("Invalid password")
        password = input("> ")
    censored_password = ""
    for i in password:
        censored_password += "*"
    print("Your " + str(len(password)) + " character password is valid: " + censored_password)


def password_validation(password):
    if len(password) < MIN_LENGTH:
        print("Password not long enough!")
        return False
    else:
        return True

main()