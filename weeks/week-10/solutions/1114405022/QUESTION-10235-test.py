"""QUESTION-10235 測試程式"""

import subprocess
import sys
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
TARGETS = [
    BASE_DIR / "QUESTION-10235.py",
    BASE_DIR / "QUESTION-10235-easy.py",
    BASE_DIR / "QUESTION-10235-easy-handtyped.py",
]


def run_program(path: Path, input_data: str) -> str:
    completed = subprocess.run(
        [sys.executable, str(path)],
        input=input_data,
        text=True,
        capture_output=True,
        check=False,
    )
    if completed.returncode != 0:
        raise RuntimeError(f"{path.name} failed\n{completed.stderr}")
    return completed.stdout.rstrip("\n")


def main() -> None:
    test_input = "17\n18\n13\n23\n101\n"
    expected = "\n".join(
        [
            "17 is emirp.",
            "18 is not prime.",
            "13 is emirp.",
            "23 is prime.",
            "101 is prime.",
        ]
    )

    all_passed = True
    for target in TARGETS:
        actual = run_program(target, test_input)
        ok = actual == expected
        print(f"=== 測試 {target.name} ===")
        print(f"[case1] {'PASS' if ok else 'FAIL'}")
        if not ok:
            all_passed = False
            print("--- 預期輸出 ---")
            print(expected)
            print("--- 實際輸出 ---")
            print(actual)
        print()

    if all_passed:
        print("全部測試通過")
    else:
        print("有測試失敗")
        sys.exit(1)


if __name__ == "__main__":
    main()
