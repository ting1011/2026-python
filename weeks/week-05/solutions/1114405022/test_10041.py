# 測試程式，需搭配 pytest 使用
# 測試資料與預期結果
from io import StringIO
import sys

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
    import QUESTION_10041_easy
    import QUESTION_10041
    input_data = "2 2 2 4 3 2 4 6\n"
    expected = "2\n4\n"
    run_test(QUESTION_10041_easy, input_data, expected)
    run_test(QUESTION_10041, input_data, expected)
    print("所有測試通過！")

def test_10041(monkeypatch, capsys):
    input_data = "2\n2 2 4\n3 2 4 6\n"
    expected = "2\n4\n"
    monkeypatch.setattr('sys.stdin', StringIO(input_data))
    import QUESTION_10041
    out, _ = capsys.readouterr()
    assert out == expected
