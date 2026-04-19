"""Task 1: Sequence Clean

Input: one line of space-separated integers
Output:
- dedupe (preserve first appearance order)
- asc sort
- desc sort
- evens in original order
"""

from __future__ import annotations


def parse_numbers(line: str) -> list[int]:
    line = line.strip()
    if not line:
        return []
    return [int(x) for x in line.split()]


def dedupe_preserve_order(nums: list[int]) -> list[int]:
    seen: set[int] = set()
    out: list[int] = []
    for n in nums:
        if n not in seen:
            seen.add(n)
            out.append(n)
    return out


def sequence_clean(nums: list[int]) -> dict[str, list[int]]:
    return {
        "dedupe": dedupe_preserve_order(nums),
        "asc": sorted(nums),
        "desc": sorted(nums, reverse=True),
        "evens": [n for n in nums if n % 2 == 0],
    }


def fmt_line(label: str, nums: list[int]) -> str:
    if nums:
        return f"{label}: " + " ".join(str(n) for n in nums)
    return f"{label}:"


def main() -> None:
    nums = parse_numbers(input())
    result = sequence_clean(nums)
    print(fmt_line("dedupe", result["dedupe"]))
    print(fmt_line("asc", result["asc"]))
    print(fmt_line("desc", result["desc"]))
    print(fmt_line("evens", result["evens"]))


if __name__ == "__main__":
    main()
