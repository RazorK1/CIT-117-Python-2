import re

class Numerology:
    def __init__(self, name, dob):
        self._name = name.upper()
        self._dob = dob  # Expected format: MM-DD-YYYY

        # Compute values upon initialization
        self._life_path = self._reduce_to_single_digit(sum(int(d) for d in re.sub(r'\D', '', self._dob)))
        self._birthday = self._reduce_to_single_digit(int(self._dob.split('-')[1]))  # Extract day and reduce
        self._attitude = self._reduce_to_single_digit(int(self._dob.split('-')[0]) + self._birthday)  # Month + Day

        # Compute name-based numbers
        vowels = "AEIOU"
        self._soul = self._reduce_to_single_digit(
            sum(self._get_letter_value(l) for l in self._name if l in vowels)
        )
        self._personality = self._reduce_to_single_digit(
            sum(self._get_letter_value(l) for l in self._name if l.isalpha() and l not in vowels)
        )
        self._power_name = self._reduce_to_single_digit(self._soul + self._personality)

    def _reduce_to_single_digit(self, num):
        #Reduce numbers until a single digit remains.
        while num > 9:  # Always reduce
            num = sum(int(d) for d in str(num))
        return num

    def _get_letter_value(self, letter):
        """Convert letters into numerology values."""
        numerology_chart = {
            1: "AJS", 2: "BKT", 3: "CLU", 4: "DMV", 5: "ENW",
            6: "FOX", 7: "GPY", 8: "HQZ", 9: "IR"
        }
        for value, letters in numerology_chart.items():
            if letter in letters:
                return value
        return 0  # Ignore non-A-Z characters

    # Convert getters to properties
    @property
    def Name(self): return self._name

    @property
    def Birthdate(self): return self._dob

    @property
    def LifePath(self): return self._life_path

    @property
    def BirthDay(self): return self._birthday

    @property
    def Attitude(self): return self._attitude

    @property
    def Soul(self): return self._soul

    @property
    def Personality(self): return self._personality

    @property
    def PowerName(self): return self._power_name


# Extended Class with Life Path Description
class NumerologyLifePathDetails(Numerology):
    def __init__(self, name, dob):
        super().__init__(name, dob)  # Call parent constructor

    @property
    def LifePathDescription(self):
        descriptions = {
            1: "The Independent: Wants to work/think for themselves",
            2: "The Mediator: Avoids conflict and wants love and harmony",
            3: "The Performer: Likes music, art and to perform or get attention",
            4: "The Teacher/Truth Seeker: Is meant to be a teacher or mentor and is truthful",
            5: "The Adventurer: Likes to travel and meet others, often an extrovert",
            6: "The Inner Child: Is meant to be a parent and/or one that is young at heart",
            7: "The Naturalist: Enjoys nature and water and alternative life paths, open to spirituality",
            8: "The Executive: Gravitates to money and power",
            9: "The Humanitarian: Helps others and/or experiences pain and learns the hard way"
        }
        return descriptions.get(self.LifePath)
