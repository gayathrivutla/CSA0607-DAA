"""Correctness tests for all three search algorithms."""

import random
from search_algorithms import ALGORITHMS

random.seed(1)
passed = 0


def check(name, cond):
    global passed
    assert cond, "FAILED: " + name
    passed += 1
    print("PASS:", name)


for algo, (fn, fn_counted) in ALGORITHMS.items():
    check(f"{algo}: empty array", fn([], 5) == -1)
    check(f"{algo}: single element found", fn([7], 7) == 0)
    check(f"{algo}: single element missing", fn([7], 8) == -1)
    arr = [10, 20, 30, 40, 50, 60, 70]
    check(f"{algo}: first element", fn(arr, 10) == 0)
    check(f"{algo}: last element", fn(arr, 70) == 6)
    check(f"{algo}: middle element", fn(arr, 40) == 3)
    check(f"{algo}: below minimum", fn(arr, 5) == -1)
    check(f"{algo}: above maximum", fn(arr, 99) == -1)
    check(f"{algo}: between elements", fn(arr, 35) == -1)
    big = sorted(random.sample(range(10**9), 5000))
    ok = all(fn(big, big[i]) == i for i in random.sample(range(5000), 300))
    check(f"{algo}: 300 random hits on 5000 records", ok)
    miss = [x for x in (random.randrange(10**9) for _ in range(300)) if x not in set(big)]
    check(f"{algo}: random misses", all(fn(big, x) == -1 for x in miss))
    ok = all(fn_counted(big, big[i])[0] == i for i in random.sample(range(5000), 100))
    check(f"{algo}: counted version agrees", ok)

print(f"\nAll {passed} tests passed.")
