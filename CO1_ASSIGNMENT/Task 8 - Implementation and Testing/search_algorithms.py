"""Three approaches for searching a student registration number.

1. linear_search            - sequential scan, O(n)
2. binary_search_iterative  - halving loop on a sorted array, O(log n)
3. binary_search_recursive  - divide and conquer on a sorted array, O(log n)
                              recurrence: T(n) = T(n/2) + c

Each algorithm exists in two forms:
  * plain version   (used for timing, no overhead)
  * *_counted       (returns (index, comparisons), used for operation counts)

A "comparison" is one test of the key against an array element
(equality test for linear search, one three-way key-vs-mid test for binary
search). All functions return the index of the key, or -1 if absent.
"""

import sys

sys.setrecursionlimit(10_000)


# ---------------------------------------------------------------- linear
def linear_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1


def linear_search_counted(arr, key):
    comps = 0
    for i in range(len(arr)):
        comps += 1
        if arr[i] == key:
            return i, comps
    return -1, comps


# ------------------------------------------------------ iterative binary
def binary_search_iterative(arr, key):
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        v = arr[mid]
        if v == key:
            return mid
        if v < key:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1


def binary_search_iterative_counted(arr, key):
    lo, hi = 0, len(arr) - 1
    comps = 0
    while lo <= hi:
        mid = (lo + hi) // 2
        comps += 1
        v = arr[mid]
        if v == key:
            return mid, comps
        if v < key:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1, comps


# ------------------------------------------------------ recursive binary
def binary_search_recursive(arr, key, lo=0, hi=None):
    if hi is None:
        hi = len(arr) - 1
    if lo > hi:
        return -1
    mid = (lo + hi) // 2
    v = arr[mid]
    if v == key:
        return mid
    if v < key:
        return binary_search_recursive(arr, key, mid + 1, hi)
    return binary_search_recursive(arr, key, lo, mid - 1)


def binary_search_recursive_counted(arr, key):
    comps = [0]

    def rec(lo, hi):
        if lo > hi:
            return -1
        mid = (lo + hi) // 2
        comps[0] += 1
        v = arr[mid]
        if v == key:
            return mid
        if v < key:
            return rec(mid + 1, hi)
        return rec(lo, mid - 1)

    return rec(0, len(arr) - 1), comps[0]


ALGORITHMS = {
    "Linear": (linear_search, linear_search_counted),
    "Binary (iterative)": (binary_search_iterative, binary_search_iterative_counted),
    "Binary (recursive)": (binary_search_recursive, binary_search_recursive_counted),
}
