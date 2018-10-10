import random
import unittest

from src.quicksort import QuickSort

sort = QuickSort.sort


class TestListSort(unittest.TestCase):

    def test_sort_list(self):
        self.assertEqual([], sort([]))
        self.assertEqual([1], sort([1]))
        self.assertEqual([1, 2], sort([1, 2]))
        self.assertEqual([1, 2], sort([2, 1]))
        self.assertEqual([1, 2, 3], sort([3, 2, 1]))
        self.assertEqual([1, 2, 3], sort([2, 1, 3]))
        self.assertEqual([1, 2, 3], sort([2, 3, 1]))

    def test_sort_many(self):
        unsorted = list(map(lambda n: random.randint(1, 101), range(10000)))

        self.assertEqual(sorted(unsorted), sort(unsorted))
