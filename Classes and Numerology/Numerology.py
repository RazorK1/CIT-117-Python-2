import re


class Numerology:
    def __init__(self, name, dob):
        self.name = name.upper()
        self.dob = dob

    def getName(self):
        return self.name

    def getBirthdate(self):
        return self.dob

    def _reduce_to_single_digit(self, num):
        while num > 9 and num not in [11, 22, 33]:  # Master numbers are exceptions
            num = sum(int(digit) for digit in str(num))
        return num

    def getLifePath(self):
        digits = [int(d) for d in re.sub(r'\D', '', self.dob)]
        return self._reduce_to_single_digit(sum(digits))

    def getBirthDay(self):
        day = int(self.dob.split('-')[1])
        return self._reduce_to_single_digit(day)

    def getAttitude(self):
        month, day, _ = map(int, self.dob.split('-'))
        return self._reduce_to_single_digit(month + day)

    def _get_letter_value(self, letter):
        numerology_chart = {
            1: 'AJS', 2: 'BKT', 3: 'CLU', 4: 'DMV', 5: 'ENW',
            6: 'FOX', 7: 'GPY', 8: 'HQZ', 9: 'IR'
        }
        for value, letters in numerology_chart.items():
            if letter in letters:
                return value
        return 0

    def getSoul(self):
        vowels = "AEIOU"
        soul_number = sum(self._get_letter_value(letter) for letter in self.name if letter in vowels)
        return self._reduce_to_single_digit(soul_number)

    def getPersonality(self):
        vowels = "AEIOU"
        personality_number = sum(self._get_letter_value(letter) for letter in self.name if letter not in vowels)
        return self._reduce_to_single_digit(personality_number)

    def getPowerName(self):
        return self._reduce_to_single_digit(self.getSoul() + self.getPersonality())
