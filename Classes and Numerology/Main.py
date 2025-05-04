import re
from Numerology import Numerology


def get_valid_name():
    while True:
        name = input("Enter your full birth name: ").strip()
        if name:
            return name
        print("Invalid input. Name cannot be empty.")


def get_valid_dob():
    while True:
        dob = input("Enter your birthdate (MM-DD-YYYY): ")
        if re.match(r'^(0[1-9]|1[0-2])[-/](0[1-9]|[12][0-9]|3[01])[-/]\d{4}$', dob):
            return dob.replace('/', '-')
        print("Invalid format. Please enter date as MM-DD-YYYY.")


if __name__ == "__main__":
    name = get_valid_name()
    dob = get_valid_dob()

    numerology = Numerology(name, dob)

    print("\n--- Numerology Reading ---")
    print(f"Name: {numerology.getName()}")
    print(f"Birthdate: {numerology.getBirthdate()}")
    print(f"Life Path Number: {numerology.getLifePath()}")
    print(f"Birth Day Number: {numerology.getBirthDay()}")
    print(f"Attitude Number: {numerology.getAttitude()}")
    print(f"Soul Number: {numerology.getSoul()}")
    print(f"Personality Number: {numerology.getPersonality()}")
    print(f"Power Name Number: {numerology.getPowerName()}")
