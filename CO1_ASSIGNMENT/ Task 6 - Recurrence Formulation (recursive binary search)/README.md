# Task 6 - Recurrence Formulation (recursive binary search)

Let T(n) be the number of comparisons for a subarray of n elements.

* Divide: compute `mid` - one step, one comparison.
* Conquer: recurse into exactly one half, of size at most floor(n/2) (worst case).
* Combine: nothing; the answer of the subcall is returned.

**Worst-case recurrence**

T(n) = T(floor(n/2)) + 1 for n > 1
T(1) = 1, T(0) = 0

In the common form with constant work c per call:

**T(n) = T(n/2) + c, T(1) = c**

Best case: T(n) = 1 (key at the midpoint, no recursion).

Linear search written recursively would give T(n) = T(n-1) + 1, T(0) = 0, which solves to T(n) = n; it is shown only for contrast - the assignment's recursive approach is binary search.

Recursion depth: the recursion depth equals T(n), at most floor(log2 n) + 1 = 20 for n = 10^6, so there is no stack-overflow risk.
