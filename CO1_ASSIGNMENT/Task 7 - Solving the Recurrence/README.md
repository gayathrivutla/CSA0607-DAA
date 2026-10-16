# Task 7 - Solving the Recurrence

Solve T(n) = T(n/2) + c with T(1) = c. Take n = 2^k.

## 1. Substitution (iteration / unrolling)
T(n) = T(n/2) + c
     = T(n/4) + c + c = T(n/4) + 2c
     = T(n/8) + 3c
     ...
     = T(n/2^i) + i*c

Stop when n/2^i = 1, i.e. i = log2 n:

T(n) = T(1) + c log2 n = c + c log2 n = **c (log2 n + 1) = Theta(log n)**.

## 2. Master theorem
Form T(n) = a T(n/b) + f(n) with a = 1, b = 2, f(n) = c = Theta(1).
n^(log_b a) = n^(log_2 1) = n^0 = 1. f(n) = Theta(n^0) -> **Case 2**:

T(n) = Theta(n^(log_b a) log n) = **Theta(log n)**.

## 3. Recursion tree
Every level contains a single node costing c, and there are log2 n + 1 levels, so the total cost is c (log2 n + 1).

## 4. Proof by induction
Claim: T(n) = c(log2 n + 1) for n = 2^k.
Base: n = 1 -> T(1) = c = c(0 + 1). OK.
Step: assume T(n/2) = c(log2(n/2) + 1) = c log2 n. Then T(n) = T(n/2) + c = c log2 n + c = c(log2 n + 1). OK.

## Conclusion
The recursive binary search runs in **Theta(log n)** worst-case time, matching the iterative version and the measured comparison counts (19 comparisons for n = 10^6 against the bound floor(log2 10^6) + 1 = 20).
