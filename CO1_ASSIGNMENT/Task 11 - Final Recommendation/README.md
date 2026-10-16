# Task 11 - Final Recommendation

**Recommended algorithm: iterative binary search on a sorted array of registration numbers.**

## Justification
1. **Complexity:** Theta(log n) worst and average, against Theta(n) for linear search. For n = 10^6 this is at most 20 comparisons against up to 1,000,000.
2. **Measured evidence:** at n = 1,000,000 iterative binary search averaged 3.3 µs per search against 118.0 ms for linear search (36,051x faster); its time was almost flat across a 1,000x increase in n.
3. **Iterative over recursive:** same comparisons, O(1) space instead of O(log n) stack, and measurably faster (no call overhead).
4. **When linear search is still fine:** very small or unsorted, one-off datasets (n below a few hundred) where sorting is not worth it.
5. **Trade-off:** binary search needs the data sorted. Registration numbers are comparable integers, so sorting is a one-off O(n log n) cost and new records can be inserted in order (see Task 12).

Task 12 explains why, for the 1,000,000-record / 50,000-requests-per-hour case, binary search is more than sufficient and when to consider a hash index.
