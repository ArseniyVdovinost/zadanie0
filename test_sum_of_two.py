import unittest
from sum_of_two import two_sum

class TestTwoSum(unittest.TestCase):

    def test_example_1(self):
        self.assertEqual(two_sum([2, 7, 11, 15], 9), [0, 1])

    def test_example_2(self):
        self.assertEqual(two_sum([3, 2, 4], 6), [1, 2])

    def test_example_3(self):
        self.assertEqual(two_sum([3, 3], 6), [0, 1])

    # Граничные случаи (corner cases)

    def test_empty_list(self):
        self.assertIsNone(two_sum([], 5))

    def test_single_element(self):
        self.assertIsNone(two_sum([5], 5))

    def test_no_solution(self):
        self.assertIsNone(two_sum([1, 2, 3], 7))

    def test_negative_numbers(self):
        self.assertEqual(two_sum([-3, 4, 3, 90], 0), [0, 2])

    def test_large_numbers(self):
        self.assertEqual(two_sum([10**9, -10**9, 0], 0), [0, 1])

    def test_duplicate_values_different_indices(self):
        # Проверка, что не используется один и тот же элемент дважды
        self.assertEqual(two_sum([2, 5, 5, 11], 10), [1, 2])

    def test_zero_target(self):
        self.assertEqual(two_sum([0, 4, 3, 0], 0), [0, 3])

if __name__ == "__main__":
    unittest.main()
