"""
Advent of Code 2025 - Day 10

Author: Xiaohan
Date: 2025-12-10

Description:
  Solution for Day 10 of Advent of Code 2025.
  Solve by linear programming.
"""
import sys
import numpy as np
from pulp import *

def call_lp(target, basis_set, upper_bounds=None, is_binary=False):
    num_dim = target.size
    num_basis = len(basis_set)

    prob = LpProblem("Presses", LpMinimize)
    vars = []
    if upper_bounds is None:
        vars = [LpVariable("x"+str(i), lowBound=0, cat="Integer") for i in range(num_basis)]
    else:
        vars = [LpVariable("x"+str(i), lowBound=0, upBound=upper_bounds[i], cat="Integer") for i in range(num_basis)]

    prob += (
        lpSum(vars),
        "minimize presses"
    )

    if not is_binary:
        for i in range(num_dim):
            prob += (
                lpSum([vars[j] * basis_set[j][i] for j in range(num_basis)]) == target[i],
                "Constraint %d" % i
                )
    else:
        k = pulp.LpVariable.dicts("k", range(num_dim), lowBound=0, cat="Integer")
        for i in range(num_dim):
            prob += (
                lpSum([vars[j] * basis_set[j][i] for j in range(num_basis)]) == target[i] + 2 * k[i],
                "Constraint %d" % i
                )            

    status = prob.solve()
    return pulp.value(prob.objective)

def calculate_button_presses(lines):
    num_tot1, num_tot2 = 0, 0
    for line in lines:
        str_target1 = line.strip().split()[0]
        str_target2 = line.strip().split()[-1]
        target1 = np.zeros(len(str_target1)-2)
        for i in range(1, len(str_target1)-1):
            target1[i-1] = 1 if str_target1[i] == '#' else 0
        target2 = np.array(list(map(int, str_target2[1:-1].split(','))))

        num_dim = target2.size
        str_basises = line.strip().split()[1:-1]
        basis_set = []
        for str_basis in str_basises:
            indexes = map(int, str_basis[1:-1].split(','))
            basis = np.zeros(num_dim)
            np.put(basis, list(indexes), 1)
            basis_set.append(basis)

        num_tot1 += call_lp(target1, basis_set, [1 for i in range(len(basis_set))], True)
        num_tot2 += call_lp(target2, basis_set)
    
    return int(num_tot1), int(num_tot2)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("[ERROR] NO input file!")
        print("[INFO] Usage: python day10.py <input_file>")
        sys.exit(1)
    input_file = sys.argv[1]
    with open(input_file, 'r') as f:
        lines = f.readlines()
    res1, res2 = calculate_button_presses(lines)
    print(res1, res2)