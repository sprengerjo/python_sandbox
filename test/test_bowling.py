import unittest

from src.bowling import BowlingScoreCalculator


class BowlingScoreCalculatorTest(unittest.TestCase):

    def setUp(self):
        g = BowlingScoreCalculator()
        self.roll = g.roll
        self.score = g.score

    def testGutterGamesStest_gutter_games_should_score_0houldScore0(self):
        self.roll_many(20, 0)
        self.assertEqual(self.score(), 0)

    def test_one_pin_games_should_score_20(self):
        self.roll_many(20, 1)
        self.assertEqual(self.score(), 20)

    def test_one_spare_bonus_should_be_added(self):
        self.roll(4)
        self.roll(6)
        self.roll_many(18, 4)
        self.assertEqual(self.score(), 4 + 6 + 4 + 18 * 4)

    def test_one_strike_bonus_should_be_added(self):
        self.roll(10)
        self.roll_many(18, 4)
        self.assertEqual(self.score(), 10 + 4 + 4 + 18 * 4)

    def test_perfect_game_should_score_300(self):
        self.roll_many(12, 10)
        self.assertEqual(self.score(), 300)

    def roll_many(self, rolls, pins):
        for i in [pins] * rolls:
            self.roll(i)
