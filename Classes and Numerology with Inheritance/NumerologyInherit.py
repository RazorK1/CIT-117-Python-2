#  Kyle Harris
#  CIT-117/117L Python
#  Numerology Inheritance – Properties and Decorators

from NumerologyLifePathDetails import NumerologyLifePathDetails

def main():
    # Get user input
    name = input("Enter your full name: ").strip()
    print("\nPlease use '-' for entering your birth date.")
    dob = input("Enter your birth date (MM-DD-YYYY): ").strip()

    # Validate inputs
    if not name or not dob or len(dob) != 10 or not all(c.isdigit() or c in "-/" for c in dob):
        print("Invalid input. Ensure the name is not empty and date is in MM-DD-YYYY format.")
        return  # Exit function if validation fails

    # Create a NumerologyLifePathDetails object
    person = NumerologyLifePathDetails(name, dob)

    # Output results using properties
    print(f"\nNumerology Details for {person.Name}:")
    print(f"Birthdate: {person.Birthdate}")
    print(f"Life Path Number: {person.LifePath}")
    print(f"Birthday Number: {person.BirthDay}")
    print(f"Attitude Number: {person.Attitude}")
    print(f"Soul Number: {person.Soul}")
    print(f"Personality Number: {person.Personality}")
    print(f"Power Name Number: {person.PowerName}")
    print(f"Life Path Description: {person.LifePathDescription}")

# Call the main function
if __name__ == "__main__":
    main()

#  Prevents the program from closing.
input("\nPress Enter to exit...")