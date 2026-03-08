import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

replicas = [1, 2, 4, 8]

run1 = [1080, 1510, 1340, 1370]
run2 = [1090, 1470, 1330, 1330]
avg = [(a + b) / 2 for a, b in zip(run1, run2)]

x = np.arange(len(replicas))
width = 0.25

fig, ax = plt.subplots(figsize=(9, 5))

bars1 = ax.bar(
    x - width,
    run1,
    width,
    label="Run 1",
    color="#4C72B0",
    edgecolor="white",
    linewidth=0.5,
)
bars2 = ax.bar(
    x, run2, width, label="Run 2", color="#55A868", edgecolor="white", linewidth=0.5
)
bars3 = ax.bar(
    x + width,
    avg,
    width,
    label="Average",
    color="#C44E52",
    edgecolor="white",
    linewidth=0.5,
)

for bar, val in zip(bars3, avg):
    ax.text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height() + 15,
        f"{int(val):,}",
        ha="center",
        va="bottom",
        fontsize=8.5,
        fontweight="bold",
        color="#C44E52",
    )

ax.set_xlabel("Number of Replicas", fontsize=12)
ax.set_ylabel("Requests / Second", fontsize=12)
ax.set_title(
    "Docker Swarm whoami Service: Scaling Benchmark\n(2× t2.micro, 1 vCPU each — wrk -t4 -c5 -d30s)",
    fontsize=13,
)
ax.set_xticks(x)
ax.set_xticklabels([str(r) for r in replicas])
ax.set_ylim(0, 1800)
ax.legend()
ax.grid(axis="y", alpha=0.3)

plt.tight_layout()
plt.savefig("benchmark_histogram.pdf")
print("Saved benchmark_histogram.pdf")
