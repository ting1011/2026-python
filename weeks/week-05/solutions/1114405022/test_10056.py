# 純 Python 執行的測試程式
from io import StringIO
import sys

def run_test(module, input_data, expected):
    old_stdin = sys.stdin
    old_stdout = sys.stdout
    sys.stdin = StringIO(input_data)
    sys.stdout = StringIO()
    module.main()
    output = sys.stdout.getvalue()
    sys.stdin = old_stdin
    sys.stdout = old_stdout
    assert output == expected, f"預期: {expected!r}\n實際: {output!r}"
    print(f"測試通過: {module.__name__}")

if __name__ == "__main__":
    import QUESTION_10056_easy
    import QUESTION_10056
    input_data = "3 0.16666667 1\n3 0.16666667 2\n3 0.16666667 3\n"
    expected = "0.2000\n0.1667\n0.1333\n"
    run_test(QUESTION_10056_easy, input_data, expected)
    run_test(QUESTION_10056, input_data, expected)
    print("所有測試通過！")
