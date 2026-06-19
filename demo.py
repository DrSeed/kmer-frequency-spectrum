import os, numpy as np, matplotlib; matplotlib.use("Agg")
from collections import Counter
import matplotlib.pyplot as plt
os.makedirs("figures",exist_ok=True); os.makedirs("results",exist_ok=True)
rng=np.random.default_rng(4); k=15
genome="".join(rng.choice(list("ACGT"),20000))
reads=[]
for _ in range(4000):
    s=rng.integers(0,len(genome)-150); r=list(genome[s:s+150])
    for i in rng.choice(150,3,replace=False): r[i]=rng.choice(list("ACGT"))
    reads.append("".join(r))
c=Counter()
for r in reads:
    for i in range(len(r)-k): c[r[i:i+k]]+=1
mult=Counter(c.values()); xs=sorted(m for m in mult if m<=60); ys=[mult[m] for m in xs]
plt.figure(figsize=(7,4)); plt.plot(xs,ys); plt.xlabel("k-mer multiplicity"); plt.ylabel("number of distinct k-mers")
plt.title("K-mer spectrum (demo data, k=15)")
plt.tight_layout(); plt.savefig("figures/demo.png",dpi=150)
open("results/summary.txt","w").write(f"distinct kmers: {len(c)}\n"); print("ok")