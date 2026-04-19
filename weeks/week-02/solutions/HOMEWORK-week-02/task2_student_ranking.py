"""Task 2: Student Ranking

Sort rules:
1) score desc
2) age asc when score ties
3) name asc when score and age tie
"""

from __future__ import annotations


Student = tuple[str, int, int]


def rank_students(students: list[Student], k: int) -> list[Student]:
    ranked = sorted(students, key=lambda s: (-s[1], s[2], s[0]))
    if k < 0:
        return []
    return ranked[:k]


def parse_input(lines: list[str]) -> tuple[list[Student], int]:
    n, k = map(int, lines[0].split())
    students: list[Student] = []
    for i in range(1, n + 1):
        name, score, age = lines[i].split()
        students.append((name, int(score), int(age)))
    return students, k


def main() -> None:
    first = input().strip()
    if not first:
        return
    n, k = map(int, first.split())
    students: list[Student] = []
    for _ in range(n):
        name, score, age = input().split()
        students.append((name, int(score), int(age)))

    for name, score, age in rank_students(students, k):
        print(name, score, age)


if __name__ == "__main__":
    main()
