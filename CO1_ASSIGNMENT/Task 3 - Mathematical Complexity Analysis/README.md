# Task 3 - Mathematical Complexity Analysis

## Linear search
The loop runs at most n times, with one comparison per iteration.

C(n) = sum_{i=1}^{k} 1 = k, where k is the number of elements inspected (1 <= k <= n).

For an unsuccessful search k = n, so C_worst(n) = n.

## Iterative binary search
After each comparison the search interval is at most half as large:
n -> floor(n/2) -> floor(n/4) -> ... -> 1 -> 0.
The interval reaches size 0 after at most floor(log2 n) + 1 steps, so

C_worst(n) = floor(log2 n) + 1.

## Recursive binary search
Each call does one comparison and makes at most one recursive call on a subarray of size <= floor(n/2); the count is the same as the iterative version:

C_worst(n) = floor(log2 n) + 1 (derived formally via the recurrence in Tasks 6-7).

## Space complexity
| Algorithm | Extra space |
|---|---|
| Linear | O(1) |
| Binary iterative | O(1) |
| Binary recursive | O(log n) stack frames |

## Time summary
| Algorithm | Time |
|---|---|
| Linear | Theta(n) worst/average, Theta(1) best |
| Binary (both) | Theta(log n) worst/average, Theta(1) best |
