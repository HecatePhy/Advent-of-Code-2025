"""
Advent of Code 2025 - Day 3

Author: Xiaohan
Date: 2025-12-03

Description:
    Solution for Day 3 of Advent of Code 2025.
    Functions for greedily finding largest joltage.
"""
import sys

def output_joltage(lines, num_digits):
    sum_joltage = 0
    for line in lines:
        line = line.strip()
        len_line = len(line)

        joltage_max, idx_tmp = 0, 0
        for cnt_digits in range(num_digits, 0, -1):
            max_tmp, idx_rec = -1, -1
            for i in range(idx_tmp, len_line - cnt_digits + 1):
                nat = int(line[i])
                if nat > max_tmp:
                    max_tmp = nat
                    idx_rec = i
            idx_tmp = idx_rec + 1
            joltage_max = joltage_max * 10 + max_tmp
        sum_joltage += joltage_max
    return sum_joltage


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("[ERROR] NO input file!")
        print("[INFO] Usage: python day3.py <input_file>")
        sys.exit(1)
    input_file = sys.argv[1]
    with open(input_file, 'r') as f:
        lines = f.readlines()
    res1, res2 = output_joltage(lines, 2), output_joltage(lines, 12)
    print(res1, res2)