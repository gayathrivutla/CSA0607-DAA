# Task 2 - Identification of the Basic Operation

The basic operation is the statement executed most often and that dominates running time.

| Algorithm | Basic operation | Why |
|---|---|---|
| Linear search | `A[i] == K` (key-to-element comparison) | Executed once per loop iteration; everything else (loop increment) is proportional to it |
| Iterative binary search | `A[mid] == K` / `A[mid] < K` (one three-way key-to-element comparison per iteration) | Executed once per halving step |
| Recursive binary search | the same three-way comparison at each call | Executed once per recursive call |

Convention used in the code: **one comparison = one key-vs-element test**. For binary search the equality and less-than tests are counted as a single three-way comparison, which is how the counters in `search_algorithms.py` work (`*_counted` functions).

The input size is `n`, the number of registration records. The basic-operation count is a function C(n) that Tasks 3-5 derive.
