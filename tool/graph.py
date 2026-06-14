import sys
import matplotlib.pyplot as plt

# ----------------------------
# argv
# ----------------------------
if len(sys.argv) < 2:
    print("Usage: python3 graph.py perf.log")
    sys.exit(1)

logfile = sys.argv[1]

# ----------------------------
# read file
# ----------------------------
with open(logfile, "r") as f:
    log = f.read()

# ----------------------------
# allowed metrics
# ----------------------------
valid_metrics = {
    "cycles:u",
    "instructions:u",
    "cache-misses:u",
    "page-faults:u"
}

data = {}

# ----------------------------
# robust parser
# ----------------------------
for line in log.split("\n"):
    line = line.strip()

    if not line or line.startswith("#"):
        continue

    parts = line.split()
    if len(parts) < 3:
        continue

    t, val, metric = parts[:3]

    if metric not in valid_metrics:
        continue

    try:
        t = float(t)
        val = int(val)
    except:
        continue

    data.setdefault(t, {})[metric] = val

# ----------------------------
# sort time
# ----------------------------
times = sorted(data.keys())

cycles = []
instructions = []
cache = []
pf = []

for t in times:
    cycles.append(data[t].get("cycles:u", 0))
    instructions.append(data[t].get("instructions:u", 0))
    cache.append(data[t].get("cache-misses:u", 0))
    pf.append(data[t].get("page-faults:u", 0))

# ----------------------------
# IPC
# ----------------------------
ipc = []
for c, i in zip(cycles, instructions):
    ipc.append(i / c if c != 0 else 0)

# ----------------------------
# smoothing
# ----------------------------
def smooth(arr, w=3):
    out = []
    for i in range(len(arr)):
        window = arr[max(0, i-w+1):i+1]
        out.append(sum(window) / len(window))
    return out

cycles = smooth(cycles)
ipc = smooth(ipc)
cache = smooth(cache)
pf = smooth(pf)

# ----------------------------
# normalization (stable range)
# ----------------------------
def norm(arr):
    mn, mx = min(arr), max(arr)
    if mx - mn == 0:
        return [0.5] * len(arr)
    return [(x - mn) / (mx - mn) * 0.8 + 0.1 for x in arr]

cycles = norm(cycles)
ipc = norm(ipc)
cache = norm(cache)
pf = norm(pf)

# ----------------------------
# plot
# ----------------------------
plt.figure(figsize=(12, 6))

plt.plot(times, cycles, label="cycles", linewidth=2)
plt.plot(times, ipc, label="IPC", linewidth=2)
plt.plot(times, cache, label="cache-misses", linewidth=2)
plt.plot(times, pf, label="page-faults", linewidth=2)

plt.ylim(0, 1)

plt.xlabel("Time (sec)")
plt.ylabel("Normalized value")
plt.title("perf full analysis (cycles + IPC + memory)")
plt.legend()
plt.grid(True)

plt.show()
