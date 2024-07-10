import re


class Game:
    def guess(self, guess_number):
        if guess_number is None:
            raise TypeError()

        if len(guess_number) != 3:
            raise TypeError()

        if not self.is_three_digit_number(guess_number):
            raise TypeError()

    def is_three_digit_number(self, s):
        pattern = r'^\d{3}$'
        if re.match(pattern, s):
            return True
        return False
