"""
Check the password length and change the password that was typed into Asterisks
Password check created by Keashyn Naidoo, 30 July 2020
"""
def main():
    length = 8
    password = get_password(length)
    print_asterisks(password)

def get_password(length):
    password = input("Please enter your password: ")
    while len(password) < length:
        print("Your password should be {} characters".format(length))
        password = input("Please enter your password: ")
    return password

def print_asterisks(password):
    print("Your password is:")
    for char in password:
        print("*", end='')

main()