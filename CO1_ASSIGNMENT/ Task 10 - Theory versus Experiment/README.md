# Task 10 - Theory versus Experiment

Comparison counts (exact) against the formulas of Task 4. Theory for binary search worst case is floor(log2 n) + 1.

| n | Algorithm | Theory avg | Measured avg | Theory worst | Measured worst |
|---|---|---|---|---|---|
| 1,000 | Linear | 500.5 | 513.79 | 1,000 | 1,000.0 |
| 1,000 | Binary (iterative) | 8.97 | 8.88 | 10 | 9.0 |
| 1,000 | Binary (recursive) | 8.97 | 8.88 | 10 | 9.0 |
| 10,000 | Linear | 5,000.5 | 5,296.58 | 10,000 | 10,000.0 |
| 10,000 | Binary (iterative) | 12.29 | 12.46 | 14 | 13.0 |
| 10,000 | Binary (recursive) | 12.29 | 12.46 | 14 | 13.0 |
| 100,000 | Linear | 50,000.5 | 54,628.11 | 100,000 | 100,000.0 |
| 100,000 | Binary (iterative) | 15.61 | 15.85 | 17 | 16.0 |
| 100,000 | Binary (recursive) | 15.61 | 15.85 | 17 | 16.0 |
| 1,000,000 | Linear | 500,000.5 | 547,570.31 | 1,000,000 | 1,000,000.0 |
| 1,000,000 | Binary (iterative) | 18.93 | 19.11 | 20 | 19.0 |
| 1,000,000 | Binary (recursive) | 18.93 | 19.11 | 20 | 19.0 |


![theory vs experiment](../Report/Tables_and_Graphs/graph_theory_vs_experiment.png)

## Discussion
* **Linear:** worst case equals n exactly. Average measured is within about 10% of (n+1)/2 because the average uses a random sample of only 200 keys (sampling error, not a flaw in the theory).
* **Binary:** average comparisons match log2(n+1) - 1 within 0.3 comparisons. The measured worst case is one below the bound (e.g. 19 against 20 at n = 10^6) because the absent key used in the test falls off the left edge, a path that is one comparison shorter than the longest path; an absent key to the right or in a deep gap reaches the floor(log2 n)+1 bound.
* **Time:** time ratios follow the growth predicted by Theta(n) and Theta(log n). Linear search time scales roughly proportionally with n; binary search time changes very little. The constant factors (interpreter overhead, cache effects, call overhead for recursion) explain why measured time is not an exact multiple of the comparison count.
* Theory and experiment agree.
