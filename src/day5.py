"""
Advent of Code 2025 - Day 5

Author: Xiaohan
Date: 2025-12-05

Description:
    Solution for Day 5 of Advent of Code 2025.
    Processes ranges and queries with IntervalTree.
"""
import sys

class IntervalNode:
    def __init__(self, interval):
        self.interval = interval
        self.max = interval[1]
        self.left = None
        self.right = None

class IntervalTree:
    def __init__(self):
        self.root = None

    def insert(self, root, interval):
        if root is None:
            return IntervalNode(interval)
        if interval[0] < root.interval[0]:
            root.left = self.insert(root.left, interval)
        else:
            root.right = self.insert(root.right, interval)
        root.max = max(root.max, interval[1])
        return root

    def add(self, interval):
        self.root = self.insert(self.root, interval)

    def overlap(self, int1, int2):
        return int1[0] <= int2[1] and int2[0] <= int1[1]

    def search_overlap(self, root, interval):
        if root is None:
            return None
        if self.overlap(root.interval, interval):
            return root.interval
        if root.left is not None and root.left.max >= interval[0]:
            return self.search_overlap(root.left, interval)
        return self.search_overlap(root.right, interval)

    def find_overlap(self, interval):
        return self.search_overlap(self.root, interval)

    def inorder(self, root, result):
        if root is not None:
            self.inorder(root.left, result)
            result.append(root.interval)
            self.inorder(root.right, result)

    def get_intervals(self):
        result = []
        self.inorder(self.root, result)
        return result

def count_available_ids_by_query(lines_range, lines_query):
    cnt_ids = 0
    tree = IntervalTree()
    for line in lines_range:
        left, right = map(int, line.split('-'))
        tree.add((left, right))
    
    for line in lines_query:
        query = int(line)
        overlap = tree.find_overlap((query, query))
        if overlap is not None:
            cnt_ids += 1
    
    return cnt_ids

def count_available_ids_by_range(lines_range):
    cnt_ids = 0
    intervals = []
    for line in lines_range:
        left, right = map(int, line.split('-'))
        intervals.append((left, right))
    intervals.sort(key = lambda interval: interval[0])

    intervals_merged = []
    interval_tmp = intervals[0]
    for idx in range(1, len(intervals)):
        if interval_tmp[1] >= intervals[idx][0]:
            interval_tmp = (interval_tmp[0], max(interval_tmp[1], intervals[idx][1]))
        else:
            intervals_merged.append(interval_tmp)
            interval_tmp = intervals[idx]
    intervals_merged.append(interval_tmp)

    for interval in intervals_merged:
        cnt_ids += interval[1] - interval[0] + 1
    
    return cnt_ids

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("[ERROR] NO input file!")
        print("[INFO] Usage: python day5.py <input_file>")
        sys.exit(1)
    input_file = sys.argv[1]
    lines_range = []
    lines_query = []
    with open(input_file, 'r') as f:
        while True:
            line = f.readline().strip()
            if line == "":
                break
            lines_range.append(line)
        while True:
            line = f.readline().strip()
            if not line:
                break
            lines_query.append(line)
    res1 = count_available_ids_by_query(lines_range, lines_query)
    res2 = count_available_ids_by_range(lines_range)
    print(res1, res2)