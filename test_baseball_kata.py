from unittest import TestCase

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
