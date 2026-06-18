import random


def generate_data(n):
    return [random.randint(0, 10000) for _ in range(n)]
