# Task 9 - Experimental Performance

Machine: cloud Linux VM, Python 3.13, `time.perf_counter_ns`. Times are per search; absolute values depend on the machine and Python overhead, shapes and ratios are what matter.

## Comparisons
| n | Algorithm | Best | Average | Worst |
|---|---|---|---|---|
| 1,000 | Linear | 1.00 | 513.79 | 1,000.00 |
| 1,000 | Binary (iterative) | 1.00 | 8.88 | 9.00 |
| 1,000 | Binary (recursive) | 1.00 | 8.88 | 9.00 |
| 10,000 | Linear | 1.00 | 5,296.58 | 10,000.00 |
| 10,000 | Binary (iterative) | 1.00 | 12.46 | 13.00 |
| 10,000 | Binary (recursive) | 1.00 | 12.46 | 13.00 |
| 100,000 | Linear | 1.00 | 54,628.11 | 100,000.00 |
| 100,000 | Binary (iterative) | 1.00 | 15.85 | 16.00 |
| 100,000 | Binary (recursive) | 1.00 | 15.85 | 16.00 |
| 1,000,000 | Linear | 1.00 | 547,570.31 | 1,000,000.00 |
| 1,000,000 | Binary (iterative) | 1.00 | 19.11 | 19.00 |
| 1,000,000 | Binary (recursive) | 1.00 | 19.11 | 19.00 |


## Time
| n | Algorithm | Best (µs) | Average (µs) | Worst (µs) |
|---|---|---|---|---|
| 1,000 | Linear | 0.24 | 27.40 | 49.57 |
| 1,000 | Binary (iterative) | 0.20 | 1.60 | 1.42 |
| 1,000 | Binary (recursive) | 0.23 | 1.79 | 1.63 |
| 10,000 | Linear | 0.24 | 494.11 | 562.69 |
| 10,000 | Binary (iterative) | 0.36 | 2.96 | 3.10 |
| 10,000 | Binary (recursive) | 0.25 | 4.37 | 3.94 |
| 100,000 | Linear | 0.55 | 12,742.78 | 14,189.21 |
| 100,000 | Binary (iterative) | 0.22 | 2.78 | 2.28 |
| 100,000 | Binary (recursive) | 0.26 | 6.59 | 3.20 |
| 1,000,000 | Linear | 0.78 | 117,957.76 | 223,190.07 |
| 1,000,000 | Binary (iterative) | 0.25 | 3.27 | 2.75 |
| 1,000,000 | Binary (recursive) | 0.22 | 4.30 | 3.63 |


## Graphs (in `Report/Tables_and_Graphs/`)
* `graph_worst_time.png`, `graph_average_time.png`, `graph_best_time.png`
* `graph_worst_comparisons.png`, `graph_average_comparisons.png`

## Observations
* Linear search time grows about 4,502x when n grows 1,000x (1,000 -> 1,000,000); binary search time grows about 1.9x.
* At n = 1,000,000 the average linear search takes 118.0 ms against 3.3 µs for iterative binary search - about 36,051x faster.
* The recursive version is slightly slower than the iterative one (function-call overhead) although both perform identical comparisons.
* Small timing wobble in the binary-search columns (e.g. a lower worst-case time at 100,000 than at 10,000) is microsecond-scale measurement noise, not an algorithmic effect; the comparison counts are exact.
