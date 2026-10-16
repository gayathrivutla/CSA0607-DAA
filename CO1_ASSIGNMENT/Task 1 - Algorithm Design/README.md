Task 1 - Algorithm Design
Problem: given a collection of `n` student registration numbers (12-digit integers), decide whether a key `K` is present and return its position.
Approach 1 - Linear search
Scan the records from the first to the last until `K` is found. Works on unsorted data.
```
LINEAR-SEARCH(A, n, K)
1  for i <- 0 to n-1
2      if A[i] = K then return i
3  return -1
```
Approach 2 - Iterative binary search
Requires `A` sorted. Compare `K` with the middle element and discard the half that cannot contain it.
```
BINARY-SEARCH-ITERATIVE(A, n, K)
1  lo <- 0 ; hi <- n-1
2  while lo <= hi
3      mid <- floor((lo+hi)/2)
4      if A[mid] = K then return mid
5      else if A[mid] < K then lo <- mid+1
6      else hi <- mid-1
7  return -1
```
Approach 3 - Recursive binary search
Same idea expressed as divide and conquer; each call solves a subproblem of half the size.
```
BINARY-SEARCH-RECURSIVE(A, lo, hi, K)
1  if lo > hi then return -1
2  mid <- floor((lo+hi)/2)
3  if A[mid] = K then return mid
4  if A[mid] < K then return BINARY-SEARCH-RECURSIVE(A, mid+1, hi, K)
5  else return BINARY-SEARCH-RECURSIVE(A, lo, mid-1, K)
```
Flowchart (binary search, both versions)
```
 start -> lo=0, hi=n-1 -> lo>hi? --yes--> return -1
                              |no
                         mid=(lo+hi)/2
                              |
                A[mid]==K? --yes--> return mid
                              |no
                A[mid]<K? --yes--> lo=mid+1 --+
                              |no             |
                          hi=mid-1 -----------+--> back to "lo>hi?"
```
Design notes
Linear search needs no preprocessing; binary search needs a sorted array (registration numbers are naturally sortable integers).
The recursive version uses O(log n) stack space, the iterative one O(1).
