"""
Advent of Code 2025 - Day 7

Author: Xiaohan
Date: 2025-12-07

Description:
    Solution for Day 7 of Advent of Code 2025.
    Processes aggregation via recursion.
"""
import sys

def calculate_times(lines):
    cnt_split, cnt_timeline = 0, 0
    lines = [line.strip() for line in lines]
    num_rows = len(lines)
    num_cols = len(lines[0])
    mat_timeline = [[0 for j in range(num_cols)] for i in range(num_rows)]

    for i in range(num_cols):
        mat_timeline[0][i] = 1 if lines[0][i] == 'S' else 0
    
    for i in range(1, num_rows):
        to_be_lights = []
        for j in range(num_cols):
            if lines[i-1][j] == 'S' or lines[i-1][j] == '|':
                if lines[i][j] == '^':
                    to_be_lights.append(j-1)
                    to_be_lights.append(j+1)
                    mat_timeline[i][j-1] += mat_timeline[i-1][j]
                    mat_timeline[i][j+1] += mat_timeline[i-1][j]
                    cnt_split += 1
                elif lines[i][j] == '.':
                    to_be_lights.append(j)
                    mat_timeline[i][j] += mat_timeline[i-1][j]
        
        for j in to_be_lights:
            if lines[i][j] != '^' and j >= 0 and j < num_cols:
                lines[i] = lines[i][:j] + '|' + lines[i][j+1:]
    
    cnt_timeline = sum(mat_timeline[num_rows-1])
    return cnt_split, cnt_timeline

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("[ERROR] NO input file!")
        print("[INFO] Usage: python day7.py <input_file>")
        sys.exit(1)
    input_file = sys.argv[1]
    with open(input_file, 'r') as f:
        lines = f.readlines()
    res1, res2 = calculate_times(lines)
    print(res1, res2)