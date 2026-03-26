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
    import QUESTION_10050_easy
    import QUESTION_10050
    input_data = "1\n14\n3\n3\n4\n8\n"
    expected = "5\n"
    run_test(QUESTION_10050_easy, input_data, expected)
    run_test(QUESTION_10050, input_data, expected)
    print("所有測試通過！")
