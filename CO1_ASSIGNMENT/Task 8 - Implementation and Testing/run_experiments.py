"""Experiments for Tasks 9, 10 and 12.

Usage:  python run_experiments.py [output_dir]
Writes results.json, CSV tables and PNG graphs into output_dir
(default: ../../Report/Tables_and_Graphs).
"""

import bisect
import csv
import json
import math
import os
import random
import sys
import time

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

from search_algorithms import ALGORITHMS

SIZES = [1_000, 10_000, 100_000, 1_000_000]
AVG_QUERIES = 200          # random present keys per (algorithm, size)
SEED = 2026
OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.join("..", "..", "Report", "Tables_and_Graphs")
os.makedirs(OUT, exist_ok=True)


def make_dataset(n, rng):
    """Sorted unique 12-digit registration numbers (e.g. 192210001234)."""
    base = 190_000_000_000
    return sorted(base + x for x in rng.sample(range(10**9), n))


def time_call(fn, arr, key, reps):
    t0 = time.perf_counter_ns()
    for _ in range(reps):
        fn(arr, key)
    return (time.perf_counter_ns() - t0) / reps / 1e3   # microseconds


def best_key(name, arr):
    # linear: first element; binary: the very first midpoint
    return arr[0] if name == "Linear" else arr[(len(arr) - 1) // 2]


def worst_key(name, arr):
    # linear: absent key (scans everything). binary: absent key (full descent)
    return arr[-1] + 1 if name == "Linear" else arr[0] - 1


rng = random.Random(SEED)
results = []
for n in SIZES:
    arr = make_dataset(n, rng)
    avg_keys = rng.sample(arr, AVG_QUERIES)
    for name, (fn, fnc) in ALGORITHMS.items():
        row = {"n": n, "algorithm": name}
        for case in ("best", "worst", "average"):
            if case == "average":
                keys = avg_keys
            else:
                keys = [best_key(name, arr) if case == "best" else worst_key(name, arr)]
            comps = [fnc(arr, k)[1] for k in keys]
            reps = 5 if (name == "Linear" and n >= 100_000) else (50 if name == "Linear" else 2000)
            if case == "average":
                sample = keys[:40] if name == "Linear" and n >= 100_000 else keys
                times = [time_call(fn, arr, k, 1 if name == "Linear" else 20) for k in sample]
            else:
                times = [time_call(fn, arr, k, reps) for k in keys]
            row[f"{case}_comparisons"] = sum(comps) / len(comps)
            row[f"{case}_time_us"] = sum(times) / len(times)
        results.append(row)
        print(f"n={n:>9,} {name:<19} worst comps={row['worst_comparisons']:>9.0f} "
              f"worst time={row['worst_time_us']:>12.2f} us")

# ---------------------------------------------------------- tables (CSV)
with open(os.path.join(OUT, "results_table.csv"), "w", newline="") as f:
    cols = ["n", "algorithm"] + [f"{c}_{m}" for c in ("best", "average", "worst")
                                 for m in ("comparisons", "time_us")]
    w = csv.DictWriter(f, fieldnames=cols)
    w.writeheader()
    for r in results:
        w.writerow({k: (round(v, 3) if isinstance(v, float) else v) for k, v in r.items()})

# ---------------------------------------------------- theory vs experiment
theory = []
for r in results:
    n = r["n"]
    if r["algorithm"] == "Linear":
        t_best, t_avg, t_worst = 1, (n + 1) / 2, n
    else:
        t_best, t_avg, t_worst = 1, math.log2(n + 1) - 1, math.floor(math.log2(n)) + 1
    theory.append({"n": n, "algorithm": r["algorithm"],
                   "theory_best": t_best, "exp_best": r["best_comparisons"],
                   "theory_avg": round(t_avg, 2), "exp_avg": round(r["average_comparisons"], 2),
                   "theory_worst": t_worst, "exp_worst": r["worst_comparisons"]})
with open(os.path.join(OUT, "theory_vs_experiment.csv"), "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(theory[0].keys()))
    w.writeheader()
    w.writerows(theory)

# ----------------------------------------------------------------- graphs
colors = {"Linear": "#d1495b", "Binary (iterative)": "#00798c", "Binary (recursive)": "#edae49"}


def plot(metric, title, ylabel, fname, logy=True):
    plt.figure(figsize=(7, 4.5))
    for name in ALGORITHMS:
        pts = [(r["n"], r[metric]) for r in results if r["algorithm"] == name]
        plt.plot(*zip(*pts), marker="o", label=name, color=colors[name])
    plt.xscale("log")
    if logy:
        plt.yscale("log")
    plt.xlabel("Number of records (n)")
    plt.ylabel(ylabel)
    plt.title(title)
    plt.grid(True, which="both", alpha=0.3)
    plt.legend()
    plt.tight_layout()
    plt.savefig(os.path.join(OUT, fname), dpi=140)
    plt.close()


plot("worst_time_us", "Worst-case search time", "Time per search (microseconds, log)", "graph_worst_time.png")
plot("average_time_us", "Average-case search time", "Time per search (microseconds, log)", "graph_average_time.png")
plot("best_time_us", "Best-case search time", "Time per search (microseconds, log)", "graph_best_time.png")
plot("worst_comparisons", "Worst-case comparisons", "Comparisons (log)", "graph_worst_comparisons.png")
plot("average_comparisons", "Average-case comparisons", "Comparisons (log)", "graph_average_comparisons.png")

# theory vs experiment graph (worst-case comparisons, theory dashed)
plt.figure(figsize=(7, 4.5))
for name in ("Linear", "Binary (iterative)"):
    pts = [(t["n"], t["exp_worst"]) for t in theory if t["algorithm"] == name]
    th = [(t["n"], t["theory_worst"]) for t in theory if t["algorithm"] == name]
    plt.plot(*zip(*pts), marker="o", color=colors[name], label=f"{name} - measured")
    plt.plot(*zip(*th), linestyle="--", color="black", alpha=0.6,
             label=f"{name} - theory" if name == "Linear" else "_nolegend_")
plt.xscale("log"); plt.yscale("log")
plt.xlabel("Number of records (n)"); plt.ylabel("Worst-case comparisons")
plt.title("Theory (dashed) vs measured comparisons")
plt.grid(True, which="both", alpha=0.3); plt.legend(); plt.tight_layout()
plt.savefig(os.path.join(OUT, "graph_theory_vs_experiment.png"), dpi=140)
plt.close()

# ------------------------------------------------ Task 12 design challenge
N = 1_000_000
REQ_PER_HOUR = 50_000
rng = random.Random(SEED + 1)
arr = make_dataset(N, rng)
present = rng.sample(arr, 450)
absent = [arr[0] + 2 * i + 1 for i in range(50)]
absent = [k for k in absent if k not in set(arr[:200])][:50]
queries = present + absent
rng.shuffle(queries)

design = {"requests_per_hour": REQ_PER_HOUR, "records": N, "required_rate_per_sec": REQ_PER_HOUR / 3600}
strategies = {}
for name, (fn, _) in ALGORITHMS.items():
    sample = queries[:40] if name == "Linear" else queries
    t0 = time.perf_counter()
    for q in sample:
        fn(arr, q)
    per = (time.perf_counter() - t0) / len(sample)
    strategies[name] = {"per_search_us": per * 1e6,
                        "time_for_50k_requests_s": per * REQ_PER_HOUR,
                        "utilisation_pct": per * REQ_PER_HOUR / 3600 * 100}

# hash index (extra data point for the recommendation)
index = {k: i for i, k in enumerate(arr)}
t0 = time.perf_counter()
for _ in range(20):
    for q in queries:
        index.get(q, -1)
per = (time.perf_counter() - t0) / (20 * len(queries))
strategies["Hash table (dict)"] = {"per_search_us": per * 1e6,
                                   "time_for_50k_requests_s": per * REQ_PER_HOUR,
                                   "utilisation_pct": per * REQ_PER_HOUR / 3600 * 100}
design["strategies"] = strategies

# daily insertion: one new record per day vs a day's batch merged
new_keys = [arr[-1] + 1000 + i for i in range(1, 501)]
copy = list(arr)
t0 = time.perf_counter()
for k in new_keys[:100]:
    bisect.insort(copy, k)
design["insort_per_insert_us"] = (time.perf_counter() - t0) / 100 * 1e6
copy = list(arr)
t0 = time.perf_counter()
merged = sorted(copy + new_keys)       # timsort merges two sorted runs in ~O(n)
design["batch_resort_500_records_ms"] = (time.perf_counter() - t0) * 1e3
t0 = time.perf_counter()
for k in new_keys:
    index[k] = 0
design["hash_insert_500_ms"] = (time.perf_counter() - t0) * 1e3
design["memory_list_mb"] = sys.getsizeof(arr) / 1e6
design["memory_dict_mb"] = sys.getsizeof(index) / 1e6

with open(os.path.join(OUT, "results.json"), "w") as f:
    json.dump({"experiments": results, "theory": theory, "design_challenge": design}, f, indent=2)

print("\nDesign challenge (n = 1,000,000, 50,000 requests/hour = %.1f req/s):" % design["required_rate_per_sec"])
for k, v in strategies.items():
    print(f"  {k:<20} {v['per_search_us']:>12.2f} us/search  "
          f"50k requests = {v['time_for_50k_requests_s']:>9.2f} s  ({v['utilisation_pct']:.3f}% of the hour)")
print(f"  insort per insert: {design['insort_per_insert_us']:.1f} us;  "
      f"batch re-sort of +500: {design['batch_resort_500_records_ms']:.1f} ms")
