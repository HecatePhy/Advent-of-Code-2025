"""
Advent of Code 2025 - Day 2

Author: Xiaohan
Date: 2025-12-02

Description:
    Solution for Day 2 of Advent of Code 2025.
    Functions for detecting invalid IDs via string matching.
"""
import sys
import math

def get_factors(num):
    factors = []
    for i in range(1, num // 2 + 1):
        if num % i == 0:
            factors.append(i)
    return factors

def is_invalid(num):
    #num_bits = math.floor(math.log(num, 10)) + 1
    num_bits = len(str(num))

    factors = get_factors(num_bits)
    factors.sort(reverse=True)
    str_num = str(num)
    flag1, flag2 = 0, 0
    for factor in factors:
        rep_term = str_num[0:factor]
        num_rep = num_bits // factor
        rep_res = rep_term * num_rep
        if rep_res == str_num:
            flag1 = 1
            flag2 = 1 if num_rep == 2 else 0
            break
    
    return flag1, flag2

def invalid_ids(line):
    sum1, sum2 = 0, 0
    id_ranges = line.strip().split(',')
    for id_range in id_ranges:
        id_start, id_end = map(int, id_range.split('-'))
        for id in range(id_start, id_end+1):
            flag1, flag2 = is_invalid(id)
            sum1 += flag1 * id
            sum2 += flag2 * id
    
    return sum1, sum2

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("[ERROR] NO input file!")
        print("[INFO] Usage: python day2.py <input_file>")
        sys.exit(1)
    input_file = sys.argv[1]
    with open(input_file, 'r') as f:
        line = f.readline()
    res1, res2 = invalid_ids(line)
    print(res1, res2)