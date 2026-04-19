import unittest

from task1_sequence_clean import dedupe_preserve_order, parse_numbers, sequence_clean


class TestTask1(unittest.TestCase):
    def test_normal_case(self):
        nums = parse_numbers("5 3 5 2 9 2 8 3 1")
        got = sequence_clean(nums)
        self.assertEqual(got["dedupe"], [5, 3, 2, 9, 8, 1])
        self.assertEqual(got["asc"], [1, 2, 2, 3, 3, 5, 5, 8, 9])
        self.assertEqual(got["desc"], [9, 8, 5, 5, 3, 3, 2, 2, 1])
        self.assertEqual(got["evens"], [2, 2, 8])

    def test_empty_input(self):
        nums = parse_numbers("")
        got = sequence_clean(nums)
        self.assertEqual(got["dedupe"], [])
        self.assertEqual(got["asc"], [])
        self.assertEqual(got["desc"], [])
        self.assertEqual(got["evens"], [])

    def test_dedupe_order(self):
        self.assertEqual(dedupe_preserve_order([2, 1, 2, 1, 3]), [2, 1, 3])


if __name__ == "__main__":
    unittest.main()
