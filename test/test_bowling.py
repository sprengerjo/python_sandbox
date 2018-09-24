import unittest

from src.bowling import BowlingScoreCalculator


class BowlingScoreCalculatorTest(unittest.TestCase):

    def setUp(self):
        g = BowlingScoreCalculator()
        self.roll = g.roll
        self.score = g.score

    def roll_many(self, rolls, pins):
        for r in [pins] * rolls:
            self.roll(r)

    def test_gutter_games_should_score_0(self):
        rolls = 20
        self.roll_many(rolls, 0)

        self.assertEqual(0, self.score())

    def test_one_pins_games_should_score_20(self):
        self.roll_many(20, 1)

        self.assertEqual(20, self.score())

    def test_one_spare_bonus_should_be_added_to_score(self):
        self.roll(4)
        self.roll(6)
        self.roll_many(18, 4)

        self.assertEqual(4 + 6 + 4 + 18 * 4, self.score())

    def test_one_strike_bonus_should_be_added_to_score(self):
        self.roll(10)
        self.roll_many(18, 4)

        self.assertEqual(10 + 4 + 4 + 18 * 4, self.score())

    def test_perfect_game_should_score_300(self):
        self.roll_many(12, 10)

        self.assertEqual(300, self.score())
