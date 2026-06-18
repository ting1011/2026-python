import unittest
from benchmark import generate_data


class TestBenchmark(unittest.TestCase):

    def test_generate_data_length(self):
        for n in (0, 1, 10, 100):
            with self.subTest(n=n):
                data = generate_data(n)
                self.assertEqual(len(data), n)

    def test_generate_data_all_integers(self):
        data = generate_data(50)
        for v in data:
            self.assertIsInstance(v, int)

    def test_search_functions_run_without_error(self):
        from search import linear_search, binary_search, set_search
        from timing import timeit
        data = generate_data(10)
        target = data[0] if data else 1
        for func in (linear_search, binary_search, set_search):
            with self.subTest(func=func.__name__):
                func(data, target)
