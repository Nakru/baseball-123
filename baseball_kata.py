import re
class Game:
    def guess(self, guess_number):
        if guess_number is None:
            raise TypeError()

        if len(guess_number) != 3:
            raise TypeError()

        pattern = r'^\d{3}$'
        if not re.match(pattern, guess_number):
            raise  TypeError()