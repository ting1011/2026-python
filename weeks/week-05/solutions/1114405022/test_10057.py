import unittest
from io import StringIO
import sys
import importlib

class Test10057(unittest.TestCase):
    def run_code(self, user_input):
        backup = sys.stdin
        sys.stdin = StringIO(user_input)
        backup_out = sys.stdout
        sys.stdout = StringIO()
        try:
            import 10057_easy as target
        except Exception:
            # 強制 reload，避免重複 import 錯誤
            import importlib
            import 10057_easy as target
            importlib.reload(target)
        output = sys.stdout.getvalue()
        sys.stdin = backup
        sys.stdout = backup_out
        return output.strip()

    def test_sample(self):
        # 範例測資
        inp = '2\n4 1 2 3 4\n5 1 2 3 4 5\n'
        expected = '2 2 2\n3 1 1'
        result = self.run_code(inp)
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
