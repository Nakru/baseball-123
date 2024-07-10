import re

from GameResult import GameResult


class Game:
    def __init__(self):
        super().__init__()
        self.question = ""

    def guess(self, guess_number):
        self.validate_guess_number(guess_number)
        if self.is_solved(guess_number):
            return self.get_success_game_result()
        else:
            return self.get_unsolved_game_result(guess_number)

    def get_unsolved_game_result(self, guess_number):
        strikes = 0
        balls = 0
        for i in range(len(self.question)):
            if self.question.find(guess_number[i]) == i:
                strikes += 1
            elif self.question.find(guess_number[i]) > -1:
                balls += 1
        return GameResult(False, strikes, balls)

    def get_success_game_result(self):
        return GameResult(True, 3, 0)

    def is_solved(self, guess_number):
        return guess_number == self.question

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
