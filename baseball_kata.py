import re


class Game:
    def guess(self, guess_number):
        self.validate_guess_number(guess_number)

    def is_three_digit_number(self, guess_number):
        pattern = r'^\d{3}$'
        if re.match(pattern, guess_number):
            return True
        return False

    def is_duplicate_number(self, guess_number):
        if len(set(guess_number)) == 3:
            return True
        return False

    def validate_guess_number(self, guess_number):
        if not self.is_three_digit_number(guess_number):
            raise TypeError()
        if not self.is_duplicate_number(guess_number):
            raise TypeError()
