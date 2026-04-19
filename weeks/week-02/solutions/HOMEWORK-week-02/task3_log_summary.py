"""Task 3: Log Summary

Input:
- first line m
- next m lines: user action

Output:
- user total counts sorted by count desc then user asc
- top_action line
"""

from __future__ import annotations

from collections import Counter


def summarize_logs(logs: list[tuple[str, str]]) -> tuple[list[tuple[str, int]], tuple[str, int]]:
    user_counter: Counter[str] = Counter()
    action_counter: Counter[str] = Counter()

    for user, action in logs:
        user_counter[user] += 1
        action_counter[action] += 1

    user_rows = sorted(user_counter.items(), key=lambda item: (-item[1], item[0]))

    if not action_counter:
        return user_rows, ("none", 0)

    top_action = min(action_counter.items(), key=lambda item: (-item[1], item[0]))
    return user_rows, top_action


def main() -> None:
    first = input().strip()
    if not first:
        return
    m = int(first)

    logs: list[tuple[str, str]] = []
    for _ in range(m):
        user, action = input().split()
        logs.append((user, action))

    users, top = summarize_logs(logs)

    for user, cnt in users:
        print(user, cnt)
    print(f"top_action: {top[0]} {top[1]}")


if __name__ == "__main__":
    main()
