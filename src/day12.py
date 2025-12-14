"""
Advent of Code 2025 - Day 12

Author: Xiaohan
Date: 2025-12-12

Description:
    Solution for Day 12 of Advent of Code 2025.
    Try with searching and backtracking.
"""
import sys
import numpy as np

def parse_shape(lines_shape):
    mat = []
    for line in lines_shape:
        mat.append([1 if ch == '#' else 0 for ch in line])
    return mat

def get_rotations_and_flips(shape):
    shapes = set()
    arr_shape = np.array(shape)
    for flip in [False, True]:
        arr_flip = np.flip(arr_shape, axis=1) if flip else arr_shape
        for rot in range(4):
            arr_rot = np.rot90(arr_flip, rot)
            rows = np.any(arr_rot, axis=1)
            cols = np.any(arr_rot, axis=0)
            bound = arr_rot[np.ix_(rows, cols)]
            shapes.add(tuple(tuple(row) for row in bound))
    
    return [np.array(shape) for shape in shapes]

def pack_shapes(height, width, shapes, klist):
    placements_all = []
    shape_areas = []

    for shape in shapes:
        orientations = get_rotations_and_flips(shape)
        placements = []
        for shape_orient in orientations:
            h_shape, w_shape = shape_orient.shape
            for i in range(height - h_shape + 1):
                for j in range(width - w_shape +1):
                    placements.append((shape_orient, i, j))
        placements_all.append(placements)
        shape_areas.append(np.sum(orientations[0]))

    tot_shape_area = sum([k * area for k, area in zip(klist, shape_areas)])
    if tot_shape_area > height * width:
        return False
    
    mat = np.zeros((height, width), dtype=np.int32)

    def backtrack(m, idx_shape, placements_marked):
        if idx_shape == len(shapes):
            return True
        
        klist[idx_shape]
        placements = placements_all[idx_shape]

        def place(m, placed, idx_start, placements_marked_tmp):
            if placed == klist[idx_shape]:
                return backtrack(m, idx_shape+1, placements_marked_tmp)
            for idx in range(idx_start, len(placements)):
                if idx in placements_marked_tmp[idx_shape]:
                    continue
                orient, i, j = placements[idx]
                h_shape, w_shape = orient.shape
                region = m[i:i+h_shape, j:j+w_shape]
                if np.all((orient + region) <= 1):
                    m[i:i+h_shape, j:j+w_shape] += orient
                    placements_marked_new = [set(p) for p in placements_marked_tmp]
                    placements_marked_new[idx_shape].add(idx)
                    if place(m, placed+1, idx, placements_marked_new):
                        return True
                    m[i:i+h_shape, j:j+w_shape] -= orient
            return False
        return place(m, 0, 0, [set(p) for p in placements_marked])

    return backtrack(mat, 0, [set() for shape in shapes])

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("[ERROR] NO input file!")
        print("[INFO] Usage: python day12.py <input_file>")
        sys.exit(1)
    input_file = sys.argv[1]
    lines_shape = []
    lines_region = []
    with open(input_file, 'r') as f:
        lines = f.readlines()
        ptr = 0
        while ptr < len(lines):
            line = lines[ptr].strip()
            if len(line) > 0 and line[-1] == ':':
                shape = []
                while True:
                    ptr += 1
                    if lines[ptr].strip() == "":
                        break
                    shape.append(lines[ptr].strip())
                lines_shape.append(shape)
            elif len(line) > 0:
                lines_region.append(line)
            ptr += 1
    shapes = [parse_shape(shape) for shape in lines_shape]
    cnt = 0
    for line in lines_region:
        height, width = map(int, line.strip().split()[0].strip(':').split('x'))
        klist = list(map(int, line.strip().split()[1:]))
        cnt += 1 if pack_shapes(height, width, shapes, klist) else 0
    print(cnt)