correct_password = "python123"

password = ""

while password != correct_password:
    password = input("Enter the password :")
    if password != correct_password:
        print("Incorrect password , try again.")
print("password correct . Access granted.")
