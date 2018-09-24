from distutils.sysconfig import _init_posix


class BowlingScoreCalculator(object):

    def __init__(self):
        self._scores = []

    def roll(self, pins):
        self._scores.append(pins)

    def score(self):
        return self.bonus(self._scores) + sum(self._scores)

    def bonus(self, rolls):

        if not rolls[3:]:
            return 0
        else:
            head, tail = rolls[0], rolls[1:]

            if head == 10:
                return sum(tail[:2]) + self.bonus(tail)
            if head + tail[0] == 10:
                return tail[1] + self.bonus(tail[1:])
            else:
                return self.bonus(tail[1:])
