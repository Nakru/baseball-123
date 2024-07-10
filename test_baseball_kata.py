from unittest import TestCase

from baseball_kata import Game


class TestGame(TestCase):

    def setUp(self):
        self.game = Game()

    def test_exception_when_input_is_none(self):
        with self.assertRaises(TypeError):
            self.game.guess(None)





