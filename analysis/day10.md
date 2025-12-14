# Day10

## ⚡️ Run

```bash
python src/day10.py testcases/day10_example.txt
python src/day10.py testcases/day10_input.txt
```

🛠️ requirements: 
- NumPy
- Pulp

## 💡 Prompt

1️⃣ The whole problem can be formulated as linear programming.

The overall formulation:
$$
\begin{aligned}
\min_{\mathbf{x}} & \mathbf{1}^T \mathbf{x}  \\\\
s.t. & \mathbf{B} \mathbf{x} = \mathbf{t}
\end{aligned}
$$

where $\mathbf{B}$ is the basis vectors (indicated by buttons), and $\mathbf{t}$ is the target vector (indicated by joltage requirements).

For Part I, $\mathbf{B}\mathbf{x}$ is not required to equal to $\mathbf{t}$ but identical under mod 2.
Also $\mathbf{x}$ is element-wise binary.
Introduce additional variable $\mathbf{k}$ for constraint $\mathbf{B} \mathbf{x} = \mathbf{t} + 2 \cdot \mathbf{k}$.

## 📊 Analysis

time complexity: determined by the time complexity of LP solver