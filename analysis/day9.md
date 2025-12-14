# Day9

## ⚡️ Run

```bash
# Compile
g++ day9.c -o day9
# Execute
./day9 day9_example.txt
./day9 day9_input.txt
```

🛠️ requirements: 
- C++ 11
- boost

My test environ is `gcc 9.4.0`.

## 💡 Prompt

1️⃣ The main idea of Part II is to transform the problem of determining whether a rectangle lies inside a rectilinear polygon into: a problem of computing the intersection area between the rectangle and the set of rectangles by decomposing the rectilinear polygon.

The input red tile coordinates form a closed rectilinear polygon $P$.
The rectangle by 2 red tile as opposite corners form a set of rectangles $R$.

The pseudocode is as follows:
```C
Input:
    P // rectilinear polygon
    R // rectangles

S = Decompose2Rectangles(P)
for (r : R) {
    for (s : S)
        overlap += IntersectArea(r, s)
    if (overlap == Area(r))
        max_area = max(max_area, Area(r))
}
```

2️⃣ boost library provides a very efficient function `get_rectangles` (for `polygon_90_set_data` class) which decomposes a rectilinear polygon to rectangles.

Those who want to implement it themselves can refer to:
[*Minimum partitioning simple rectilinear polygons in O(n log log n) - time*](https://dl.acm.org/doi/10.1145/73833.73871)

### 📋 Idea not implemented

Another more time-efficient method is to test whether the four edges of a rectangle lie inside the rectlinear polygon.


## 📊 Analysis

time complexity:
- the number of decomposed rectangles: $\mathcal{O}(n)$ where $n$ is the number of input coordinates
- Part I: $\mathcal{O}(n^2)$
- Part II: $\mathcal{O}(n^3)$