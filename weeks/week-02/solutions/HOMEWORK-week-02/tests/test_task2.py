import unittest

from task2_student_ranking import rank_students


class TestTask2(unittest.TestCase):
    def test_normal_case(self):
        students = [
            ("amy", 88, 20),
            ("bob", 88, 19),
            ("zoe", 92, 21),
            ("ian", 88, 19),
            ("leo", 75, 20),
            ("eva", 92, 20),
        ]
        got = rank_students(students, 3)
        self.assertEqual(got, [("eva", 92, 20), ("zoe", 92, 21), ("bob", 88, 19)])

    def test_k_larger_than_n(self):
        students = [("a", 90, 20), ("b", 80, 20)]
        got = rank_students(students, 10)
        self.assertEqual(got, [("a", 90, 20), ("b", 80, 20)])

    def test_tie_break_name(self):
        students = [("c", 88, 19), ("a", 88, 19), ("b", 88, 19)]
        got = rank_students(students, 3)
        self.assertEqual(got, [("a", 88, 19), ("b", 88, 19), ("c", 88, 19)])


if __name__ == "__main__":
    unittest.main()
