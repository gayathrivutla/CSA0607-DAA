# Task 12 - Design Challenge

**Requirement:** 50,000 search requests per hour on 1,000,000 student records; new records are added once per day.

## 1. Load
50,000 / 3,600 = **13.9 requests per second**, i.e. one request every ~72 ms on average. Even a 10x peak is ~139 req/s.

## 2. Measured cost per strategy (n = 1,000,000, mix of 90% present / 10% absent keys)
| Strategy | Time per search | Time for 50,000 requests | Share of one hour |
|---|---|---|---|
| Linear | 127,118.85 µs | 6,355.94 s | 176.554% |
| Binary (iterative) | 6.42 µs | 0.32 s | 0.009% |
| Binary (recursive) | 5.63 µs | 0.28 s | 0.008% |
| Hash table (dict) | 0.17 µs | 0.01 s | 0.000% |

(Linear search figures are measured on a 40-query sample and scaled to 50,000 requests.)

**Linear search fails the requirement:** it needs 6,356 s (1.77 hours) of single-core work for one hour of requests - more than 100% of the available time, so the queue grows without bound. At ~127 ms per search a single core can serve only about 28,320 requests per hour.

**Binary search passes with huge margin:** 0.32 s of work per hour (under 0.01% utilisation). Theoretically it needs at most 20 comparisons per request.

## 3. Handling the daily update
The data changes once per day while it is read 50,000 times per hour (read-heavy, ~1.2 million reads per day per write batch). This favours a structure that is fast to read and may be somewhat costly to update:
* Insert into the sorted array with `bisect.insort`: O(n) shift, measured 25 µs per record at n = 10^6.
* Or collect the day's new records and merge: re-sorting 1,000,000 + 500 records took 199 ms (a linear merge of two sorted lists would be faster still).
* Either way this runs once a day, off-peak, and is negligible against ~1.2 million searches per day. Build the new array and swap it in (copy-on-write) so readers are never blocked.
* Keep the array sorted by registration number; no re-sorting is needed per request.

## 4. Alternatives considered
| Option | Search | Daily update | Memory (1M ints) | Verdict |
|---|---|---|---|---|
| Linear scan | O(n) - fails | O(1) append | 8.4 MB | rejected |
| **Sorted array + binary search** | O(log n) | O(n) once a day, ms | 8.4 MB | **recommended** |
| Hash table | O(1) average, 0.17 µs | O(1) | 41.9 MB (about 5x more) | good option if range queries and ordering are never needed |
| Balanced tree / database B-tree index | O(log n) | O(log n) | higher | useful if updates become frequent |

Binary search is recommended because it meets the requirement with a wide margin, uses the least memory, keeps data ordered (supports range queries and prefix lookups), and its simplicity makes it easy to test and maintain. A hash table is faster but the extra speed is unnecessary at 14 requests per second. If the load grew by ~1000x, or updates became continuous, move to a B-tree-backed database index.

## 5. Scalability and risks
* Capacity of one core with binary search: roughly 3,600 s / 6.4 µs = 560 million requests per hour in this Python test, versus the 50,000 needed. Real systems add network and I/O latency, which dominates the search cost.
* Duplicate registration numbers: must be rejected at insertion so the sorted array holds unique keys.
* Memory: 8.4 MB for the array of references (plus the integer objects); fits in memory easily.

## Conclusion
Use a sorted array (or database index) with iterative binary search, refreshed by a daily batch merge. It handles 50,000 requests per hour using a negligible fraction of capacity, while linear search would be overloaded by 76%.
