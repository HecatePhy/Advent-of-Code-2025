"""
Advent of Code 2025 - Day 8

Author: Xiaohan
Date: 2025-12-05

Description:
    Solution for Day 5 of Advent of Code 2025.
    Processes graph connected components by UnionFind alg.
"""
import sys

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.sizes = [1] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x]) 
        return self.parent[x]

    def union(self, x, y):
        px = self.find(x)
        py = self.find(y)
        if px == py:
            return False 
        if self.rank[px] < self.rank[py]:
            self.parent[px] = py
            self.sizes[py] += self.sizes[px]
        else:
            self.parent[py] = px
            self.sizes[px] += self.sizes[py]
            if self.rank[px] == self.rank[py]:
                self.rank[px] += 1
        return True

    def connected(self, x, y):
        return self.find(x) == self.find(y)

def calculate_components(lines, topk):
    cnt_mult_sizes, cnt_mult_x = 0, 0
    coords = []
    for line in lines:
        x, y, z = map(int, line.strip().split(','))
        coords.append((x, y, z))
    
    num_boxes = len(coords)
    distances = []
    for i in range(num_boxes-1):
        for j in range(i+1, num_boxes):
            distance_square = (coords[i][0] - coords[j][0]) ** 2 + \
                (coords[i][1] - coords[j][1]) ** 2 + (coords[i][2] - coords[j][2]) ** 2
            distances.append((i, j, distance_square))
    
    union = UnionFind(num_boxes)
    distances.sort(key = lambda dis: dis[2])
    for i in range(len(distances)):
        distance_pair = distances[i]
        union.union(distance_pair[0], distance_pair[1])
        if i == topk - 1:
            sizes_root = {}
            for j in range(num_boxes):
                sizes_root[union.find(j)] = union.sizes[union.find(j)]
            sizes_sorted = sorted(sizes_root.items(), key = lambda x: x[1], reverse=True)
            cnt_mult_sizes = sizes_sorted[0][1] * sizes_sorted[1][1] * sizes_sorted[2][1]
        if union.sizes[union.find(distance_pair[0])] == num_boxes:
            cnt_mult_x = coords[distance_pair[0]][0] * coords[distance_pair[1]][0]
            break
    
    return cnt_mult_sizes, cnt_mult_x

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("[ERROR] Lack of Input!")
        print("[INFO] Usage: python day5.py <input_file> <topk>")
        sys.exit(1)
    input_file = sys.argv[1]
    topk = int(sys.argv[2])
    with open(input_file, 'r') as f:
        lines = f.readlines()
    res1, res2 = calculate_components(lines, topk)
    print(res1, res2)