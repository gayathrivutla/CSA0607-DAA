# Analysis Summary

| Algorithm | Best | Average | Worst | Space |
|---|---|---|---|---|
| Linear | Theta(1) | Theta(n) | Theta(n) | O(1) |
| Binary iterative | Theta(1) | Theta(log n) | Theta(log n) | O(1) |
| Binary recursive | Theta(1) | Theta(log n) | Theta(log n) | O(log n) |

Recurrence (recursive): T(n) = T(n/2) + c -> Theta(log n).

## Measured comparisons
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


## Measured time
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


## Theory vs experiment
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


Full derivations: see Task_3 to Task_7 folders.
