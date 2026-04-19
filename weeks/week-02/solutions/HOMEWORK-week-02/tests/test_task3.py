import unittest

from task3_log_summary import summarize_logs


class TestTask3(unittest.TestCase):
    def test_normal_case(self):
        logs = [
            ("alice", "login"),
            ("bob", "login"),
            ("alice", "view"),
            ("alice", "logout"),
            ("bob", "view"),
            ("bob", "view"),
            ("chris", "login"),
            ("bob", "logout"),
        ]
        users, top = summarize_logs(logs)
        self.assertEqual(users, [("bob", 4), ("alice", 3), ("chris", 1)])
        self.assertEqual(top, ("login", 3))

    def test_empty_logs(self):
        users, top = summarize_logs([])
        self.assertEqual(users, [])
        self.assertEqual(top, ("none", 0))

    def test_top_action_tie(self):
        logs = [("u1", "x"), ("u2", "y")]
        users, top = summarize_logs(logs)
        self.assertEqual(users, [("u1", 1), ("u2", 1)])
        self.assertEqual(top, ("x", 1))


if __name__ == "__main__":
    unittest.main()
