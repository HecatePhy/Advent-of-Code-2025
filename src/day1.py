"""
Advent of Code 2025 - Day 1

Author: Xiaohan
Date: 2025-12-01

Description:
    Solution for Day 1 of Advent of Code 2025.
    Processes left/right movements on a circle.
"""
import sys

def find_passcode(lines):
    temp = 50
    circle = 100
    cnt1, cnt2 = 0, 0
    for line in lines:
        cnt1 += int(temp == 0)

        direction = -1 if line[0] == 'L' else 1
        step = int(line[1:])
        cnt2 += (step + direction * temp) // circle
        cnt2 += 1 if (direction == -1 and temp != 0) else 0 
        temp += direction * step
        temp %= circle

    return cnt1, cnt2


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("[ERROR] NO input file!")
        print("[INFO] Usage: python day1.py <input_file>")
        sys.exit(1)
    input_file = sys.argv[1]
    with open(input_file, 'r') as f:
        lines = f.readlines()
    res1, res2 = find_passcode(lines)
    print(res1, res2)