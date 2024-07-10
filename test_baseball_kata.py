from unittest import TestCase

from GameResult import GameResult
from baseball_kata import Game


class TestGame(TestCase):

    def setUp(self):
        self.game = Game()

    def assert_illegal_argument(self, guess_number):
        try:
            self.game.guess(guess_number)
            self.fail()
        except TypeError:
            pass

    def assert_matched_number(self, result, solved, strikes, balls):
        self.assertIsNotNone(result)
        self.assertEqual(solved, result.get_solved())
        self.assertEqual(strikes, result.get_strikes())
        self.assertEqual(balls, result.get_balls())

    def generate_question(self, answer):
        self.game.question = answer

    def test_exception_when_invalid_input(self):
        self.assert_illegal_argument(None)
        self.assert_illegal_argument("12")
        self.assert_illegal_argument("1234")
        self.assert_illegal_argument("1dd")
        self.assert_illegal_argument("121")

    def test_solve_result_if_match_number(self):
        self.generate_question("123")
        self.assert_matched_number(self.game.guess("123"), True, 3, 0)

    def test_solve_result_if_umatched_number(self):
        self.generate_question("123")
        self.assert_matched_number(self.game.guess("456"), False, 0, 0)

    def test_return_solve_result_if_some_matched_number(self):
        self.generate_question("123")
        self.assert_matched_number(self.game.guess("120"), False, 2, 0)
        self.assert_matched_number(self.game.guess("061"), False, 0, 1)

