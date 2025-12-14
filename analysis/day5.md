# Day5

## ⚡️ Run

```bash
python src/day5.py testcases/day5_example.txt
python src/day5.py testcases/day5_input.txt
```

🛠️ requirements: `NULL`

## 💡 Prompt

1️⃣ The first part could be solved by Interval Tree data structure.

2️⃣ The second part is a traversal on the intervals.

## 📊 Analysis

time complexity: 
- **Part I**: $\mathcal{O}((n+m)\log n)$ where $n$ is the number of input ranges and $m$ is the number of queries
- **Part II**: $\mathcal{O}(n)$ 