# Task 5 - Asymptotic Analysis

## Linear search
* Worst: C(n) = n. Take c = 1, n0 = 1: n <= 1*n, so C(n) = **O(n)**; also n >= 1*n so C(n) = **Omega(n)** and hence **Theta(n)**.
* Best: C(n) = 1 = **Theta(1)**.
* Average: (n+1)/2; (1/2)n <= (n+1)/2 <= n for n >= 1 -> **Theta(n)**.

## Binary search
* Worst: C(n) = floor(log2 n) + 1.
  Upper bound: floor(log2 n) + 1 <= 2 log2 n for n >= 2 (c = 2, n0 = 2) -> **O(log n)**.
  Lower bound: floor(log2 n) + 1 >= log2 n for n >= 1 -> **Omega(log n)**, so **Theta(log n)**.
* Best: **Theta(1)**.
* Average: log2(n+1) - 1 = **Theta(log n)**.

## Order of growth comparison
n = 10^6: linear needs up to 1,000,000 comparisons, binary needs at most 20. log n = o(n), i.e. lim_{n->inf} log n / n = 0.

| n | log2 n | n / log2 n |
|---|---|---|
| 1,000 | 10 | 100 |
| 10,000 | 13.3 | 752 |
| 100,000 | 16.6 | 6,021 |
| 1,000,000 | 19.9 | 50,171 |

Hierarchy: 1 < log n < n.
