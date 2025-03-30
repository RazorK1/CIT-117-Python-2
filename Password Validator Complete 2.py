#  Kyle Harris
#  CIT-117/117L Python
#  Password Validator

def main():
    print("Welcome to Kyle Harris's Password Validator!")

    #  Prompt for user's name
    sName = input("\nEnter full name such as John Smith: ").strip()

    #  Extract initials
    name_parts = sName.split()
    if len(name_parts) != 2:
        print("\nPlease enter both first and last name.")
        return
    sInitials = name_parts[0][0].upper() + name_parts[1][0].upper()

    while True:
        #  Prompt for password
        sPassword = input("\nEnter your desired password: ").strip()

        #  Check password length
        if not (8 <= len(sPassword) <= 12):
            print("\nPassword must be between 8 and 12 characters.")
            continue

        #  Check password does not start with 'Pass' or 'pass'
        if sPassword.lower().startswith("pass"):
            print("\nPassword can't start with Pass.")
            continue

        #  Check for at least one uppercase letter
        if not any(char.isupper() for char in sPassword):
            print("\nPassword must contain at least 1 uppercase letter.")
            continue

        #  Check for at least one lowercase letter
        if not any(char.islower() for char in sPassword):
            print("\nPassword must contain at least 1 lowercase letter.")
            continue

        #  Check for at least one number
        if not any(char.isdigit() for char in sPassword):
            print("\nPassword must contain at least 1 number.")
            continue

        #  Check for at least one special character
        special_chars = "!@#$%^"
        if not any(char in special_chars for char in sPassword):
            print("\nPassword must contain at least 1 of these special characters: ! @ # $ % ^")
            continue

        #  Check password does not contain initials
        if sInitials.lower() in sPassword.lower():
            print("\nPassword must not contain user initials.")
            continue

        #  Check for no repeated characters
        char_count = {}
        for char in sPassword.lower():
            char_count[char] = char_count.get(char, 0) + 1

        repeated_chars = [char for char, count in char_count.items() if count > 1]
        if repeated_chars:
            print("\nThese characters appear more than once:", ", ".join(repeated_chars))
            continue

        #  If all checks pass
        print("\nPassword is valid and OK to use.")
        break

if __name__ == "__main__":
    main()

#  Prevents the program from closing.
input("Press Enter to exit...")