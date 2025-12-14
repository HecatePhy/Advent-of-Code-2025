# Day8

## ⚡️ Run

```bash
python src/day8.py testcases/day8_example.txt 10
python src/day8.py testcases/day8_input.txt 1000
```

🛠️ requirements: `NULL`

## 💡 Prompt

1️⃣ UnionFind algorithm to manage the connected components.

2️⃣ Add a size attribute to represent the size of current connected component for UnionFind data structure.

3️⃣ Stop union procedure when the size reaches the number of boxes.

## 📊 Analysis

time complexity: 
- Sort the distances of box pairs: $\mathcal{O}(n^2 \log n)$ where $n$ is the number of boxes
- Part I: $\mathcal{O}(k \alpha(k)+ n^2 \log n)$ where $k$ is the number of input pairs to connect and $\alpha$ is the inverse Ackermann function
- Part II: the worst case is $\mathcal{O}(n^2 \alpha(n^2))$