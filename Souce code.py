
from math import ceil, log2


def runtime_seconds(operations, ops_per_second=10**8):
    return operations / ops_per_second


def format_time(seconds):
    if seconds < 1:
        return f"{seconds:.9f} s" if seconds >= 0.000001 else f"{seconds:.3e} s"
    if seconds < 60:
        return f"{seconds:.3f} s"
    return f"{seconds / 60:.2f} min"


def main():
    n = 1_000_000
    ops_per_second = 10**8
    log_n = log2(n)

    # M1: every pair is compared once.
    m1 = n * (n - 1) // 2

    # M2: doubling loop; exact count is 2**ceil(log2(n)) - 1.
    m2 = 2 ** ceil(log2(n)) - 1

    # S2: conventional binary search on one million entries.
    # Maximum comparisons for a standard binary search at this n is 20.
    s2_worst = ceil(log2(n + 1))

    # M4 operation estimates use the leading terms of their recurrences.
    m4_current = n ** 2
    m4_redesign = int(round(n * log_n))

    # M5: recursion-tree estimate for T(n)=2T(n/2)+n log2(n).
    # For n=2**k and T(1)=1, T(n)=n*k*(k+1)/2+n.
    # Use log2(n) as a continuous estimate for n=1,000,000.
    m5 = n * log_n * (log_n + 1) / 2 + n

    # Report generator from the question bank.
    report_generator = 3 * n**2 + 10 * n * log_n + 50

    rows = [
        ("M1 Duplicate-listing detector", m1),
        ("M2 API rate limiter", m2),
        ("S2 Binary search (worst-case estimate)", s2_worst),
        ("M4 Current recommendation engine (leading term)", m4_current),
        ("M4 Redesigned recommendation engine (leading term)", m4_redesign),
        ("M5 Sales analytics engine (recursion-tree estimate)", m5),
        ("Nightly report generator f(n)", report_generator),
    ]

    print("SHOPSPHERE SCALABILITY AUDIT")
    print("=" * 72)
    print(f"Catalogue size n: {n:,}")
    print(f"Server capacity: {ops_per_second:,} basic operations/second")
    print()
    print(f"{'Module':56} {'Operations':>18} {'Estimated time':>16}")
    print("-" * 94)
    for label, operations in rows:
        print(f"{label:56} {operations:18,.2f} {format_time(runtime_seconds(operations)):>16}")
    print()
    print("M2 verification for n = 1,024:")
    print(f"  Exact Audit operations = 2^ceil(log2(1024)) - 1 = {2 ** ceil(log2(1024)) - 1:,}")
    print("  Therefore M2 is Theta(n), not Theta(n log n).")
    print()
    print("Decision for a 10-minute nightly window:")
    print("  M1: FAIL (about 83.33 minutes)")
    print("  M2: PASS")
    print("  S2: PASS")
    print("  M4 current design: FAIL (about 166.67 minutes under the n^2 leading-term model)")
    print("  M4 redesigned design: PASS")
    print("  M5: PASS under the stated recursion-tree estimate")
    print("  Report generator: FAIL (quadratic leading term; about 500 minutes)")
    print()
    print("Recommendation: replace M1's pairwise scan with a hash-based grouping/index")
    print("on (seller, normalized title); remove M4's replicated four-way recursion;")
    print("optimize the report generator to avoid its quadratic term.")


if __name__ == "__main__":
    main()
  
