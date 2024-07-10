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

    def test_exception_when_invalid_input(self):
        self.assert_illegal_argument(None)
        self.assert_illegal_argument("12")
        self.assert_illegal_argument("1234")
        self.assert_illegal_argument("1dd")
        self.assert_illegal_argument("121")

    def test_solve_result_if_match_number(self):
        self.game.question = "123"
        result: GameResult = self.game.guess("123")

        self.assertIsNotNone(result)
        self.assertTrue(result.get_solved())
        self.assertEqual(3, result.get_strikes())
        self.assertEqual(0, result.get_balls())

    def test_solve_result_if_umatched_number(self):
        self.game.question = "123"
        result: GameResult = self.game.guess("456")

        self.assertIsNotNone(result)
        self.assertFalse(result.get_solved())
        self.assertEqual(0, result.get_strikes())
        self.assertEqual(0, result.get_balls())
