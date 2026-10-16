# Task 4 - Best, Average and Worst Case Analysis

## Linear search
* **Best case:** key is at index 0 -> C = 1 -> Omega(1).
* **Worst case:** key is last or absent -> C = n -> O(n).
* **Average case (successful search, all positions equally likely):**
  C_avg = (1/n) * sum_{i=1}^{n} i = (n+1)/2 -> Theta(n).
  If the key is present with probability p: C_avg = p(n+1)/2 + (1-p)n.

## Binary search (iterative and recursive)
* **Best case:** key is the first midpoint -> C = 1 -> Omega(1).
* **Worst case:** key absent (or found at the last level) -> C = floor(log2 n) + 1 -> O(log n).
* **Average case (successful search):** A decision tree of n nodes has 1 node at depth 1, 2 at depth 2, ..., 2^(j-1) at depth j. For n = 2^k - 1:

  C_avg = (1/n) * sum_{j=1}^{k} j * 2^(j-1) = ((k-1) 2^k + 1)/(2^k - 1) ~ log2(n+1) - 1 -> Theta(log n).

## Summary
| Case | Linear | Binary |
|---|---|---|
| Best | 1 | 1 |
| Average | (n+1)/2 | ~ log2(n+1) - 1 |
| Worst | n | floor(log2 n) + 1 |

## Test inputs used for each case (see Task 9)
* Best: linear -> first record; binary -> record at the first midpoint.
* Worst: absent key (all algorithms do the maximum work).
* Average: 200 random existing keys, results averaged.
