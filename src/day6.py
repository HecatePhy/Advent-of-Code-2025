"""
Advent of Code 2025 - Day 6

Author: Xiaohan
Date: 2025-12-06

Description:
    Solution for Day 6 of Advent of Code 2025.
    Processes column-wise results as specified.
"""
import sys

def calculate_grand_total(lines):
    grand_tot = 0
    num_cols = len(lines[0].strip().split())
    mat = [[] for i in range(num_cols)]
    for i in range(len(lines)-1):
        terms = list(map(int, lines[i].strip().split()))
        for j in range(len(terms)):
            mat[j].append(terms[j])
    
    num_rows = len(lines) - 1
    symbols = lines[-1].strip().split()
    for i in range(num_cols):
        res = 0 if symbols[i] == '+' else 1
        for j in range(num_rows):
            res = res + mat[i][j] if symbols[i] == '+' \
                else res * mat[i][j]
        grand_tot += res
    
    return grand_tot

def calculate_grand_total_pixel(lines):
    grand_tot = 0
    lines = [line.rstrip('\n') for line in lines]
    num_rows = len(lines)
    num_cols = len(lines[0])

    cur_set = []
    for i in range(num_cols-1, -1, -1):
        cur_num = 0
        flag = False
        for j in range(num_rows-1):
            if lines[j][i] != ' ':
                cur_num = cur_num * 10 + int(lines[j][i])
                flag = True
        if flag:
            cur_set.append(cur_num)
        
        if i < len(lines[-1]) and lines[-1][i] != ' ':
            symbol = lines[-1][i]
            res = 0 if symbol == '+' else 1
            for num in cur_set:
                res = res + num if symbol == '+' \
                    else res * num
            cur_set = []
            grand_tot += res
    
    return grand_tot

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("[ERROR] NO input file!")
        print("[INFO] Usage: python day7.py <input_file>")
        sys.exit(1)
    input_file = sys.argv[1]
    with open(input_file, 'r') as f:
        lines = f.readlines()
    res1 = calculate_grand_total(lines)
    res2 = calculate_grand_total_pixel(lines)
    print(res1, res2)