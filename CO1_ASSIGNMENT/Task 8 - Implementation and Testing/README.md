# Task 8 - Implementation and Testing

Source code: `Source_Code/`

| File | Purpose |
|---|---|
| `search_algorithms.py` | linear, iterative binary, recursive binary (plain and comparison-counting versions) |
| `test_algorithms.py` | 36 correctness tests |
| `run_experiments.py` | benchmark harness (Tasks 9, 10, 12) |

Run:
```
cd Task_8_Implementation_Testing/Source_Code
pip install matplotlib
python test_algorithms.py
python run_experiments.py
```

## Test cases (per algorithm, 12 tests x 3 algorithms = 36)
empty array; single element found/missing; first, last and middle element; key below minimum; key above maximum; key between two records; 300 random hits and random misses on 5,000 records; counting version agrees with the plain version.

Result: **All 36 tests passed** (`test_output.txt`).

## Dataset
Sorted, unique 12-digit registration numbers (190,000,000,000 + random) generated with a fixed seed (2026) for n = 1,000; 10,000; 100,000; 1,000,000. The same sorted array is used for all three algorithms so the comparison is fair.
