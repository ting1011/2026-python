import json
import random
import bisect

from timing import timeit
from search import linear_search, binary_search, set_search


def generate_data(n):
    return [random.randint(0, 10000) for _ in range(n)]


NS = [10, 100, 1000, 10000]
TRIALS = 5


@timeit(repeat=TRIALS)
def bench_linear(data, target):
    return linear_search(data, target)


@timeit(repeat=TRIALS)
def bench_binary(data, target):
    return binary_search(data, target)


@timeit(repeat=TRIALS)
def bench_set(data, target):
    return set_search(data, target)


@timeit(repeat=TRIALS)
def bench_in(data, target):
    return target in data


@timeit(repeat=TRIALS)
def bench_bisect(data, target):
    i = bisect.bisect_left(data, target)
    return i < len(data) and data[i] == target


def run():
    results = {}
    for n in NS:
        data = generate_data(n)
        sorted_data = sorted(data)
        target = data[0]

        row = {"n": n}

        bench_linear(data, target)
        row["linear"] = round(bench_linear.last_elapsed, 8)

        bench_binary(sorted_data, target)
        row["binary"] = round(bench_binary.last_elapsed, 8)

        bench_set(data, target)
        row["set"] = round(bench_set.last_elapsed, 8)

        bench_in(data, target)
        row["in"] = round(bench_in.last_elapsed, 8)

        bench_bisect(sorted_data, target)
        row["bisect"] = round(bench_bisect.last_elapsed, 8)

        row["target_found"] = target
        results[f"n={n}"] = row

    with open("results.json", "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)

    print(json.dumps(results, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    run()
