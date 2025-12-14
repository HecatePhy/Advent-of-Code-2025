"""
Advent of Code 2025 - Day 4

Author: Xiaohan
Date: 2025-12-04

Description:
    Solution for Day 4 of Advent of Code 2025.
    Functions for manipulating matrix elements.
"""
import sys

def remove_rolls(paper_mat):
    row, col = len(paper_mat), len(paper_mat[0])
    cnt_removal = 0
    new_paper_mat = [['' for j in range(col)] for i in range(row)]
    for i in range(row):
        for j in range(col):
            new_paper_mat[i][j] = paper_mat[i][j]
            if paper_mat[i][j] != '@':
                continue

            cnt_neighbors = 0
            for idx_i in range(i-1, i+2):
                for idx_j in range(j-1, j+2):
                    if idx_i < 0 or idx_i >= row \
                        or idx_j < 0 or idx_j >= col \
                        or (idx_i == i and idx_j == j):
                        continue
                    if paper_mat[idx_i][idx_j] == '@':
                        cnt_neighbors += 1 
            if cnt_neighbors < 4:
                new_paper_mat[i][j] = '.'
                cnt_removal += 1
    
    return new_paper_mat, cnt_removal

def count_rolls_mat(paper_mat):
    return sum(paper_row.count('@') for paper_row in paper_mat)

def count_rolls(lines):
    lines = [line.strip() for line in lines]
    paper_mat = [[line[i] for i in range(len(line.strip()))] for line in lines]

    num_rolls_start = count_rolls_mat(paper_mat)

    tmp_paper_mat, cnt_removal = remove_rolls(paper_mat)
    num_rolls_step1 = count_rolls_mat(tmp_paper_mat)
    while cnt_removal != 0:
        tmp_paper_mat, cnt_removal = remove_rolls(tmp_paper_mat)
    num_rolls_end = count_rolls_mat(tmp_paper_mat)

    return num_rolls_start - num_rolls_step1, num_rolls_start - num_rolls_end


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("[ERROR] NO input file!")
        print("[INFO] Usage: python day4.py <input_file>")
        sys.exit(1)
    input_file = sys.argv[1]
    with open(input_file, 'r') as f:
        lines = f.readlines()
    res1, res2 = count_rolls(lines)
    print(res1, res2)