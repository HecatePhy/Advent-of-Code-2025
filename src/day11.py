"""
Advent of Code 2025 - Day 11

Author: Xiaohan
Date: 2025-12-11

Description:
    Solution for Day 11 of Advent of Code 2025.
    Calculate different paths by topological sort.
"""
import sys
import networkx as nx
import itertools

from numpy.ma import count

def cal_diff_paths(graph, source, sink):
    if not nx.is_directed_acyclic_graph(graph):
        return -1
    
    topo_order = list(nx.topological_sort(graph))
    dp = {node: 0 for node in topo_order}
    dp[source] = 1
    for u in topo_order:
        for v in graph.successors(u):
            dp[v] += dp[u]
    
    return dp[sink]

def count_paths(lines, source, sink, vias=None):
    G = nx.DiGraph()
    for line in lines:
        start_node = line.strip().split()[0].strip(':')
        if not G.has_node(start_node):
            G.add_node(start_node)
        end_nodes = line.strip().split()[1:]
        for end_node in end_nodes:
            if not G.has_node(end_node):
                G.add_node(end_node)
            G.add_edge(start_node, end_node)
    
    if vias is None:
        return cal_diff_paths(G, source, sink)
    else:
        cnt_path = 0
        for visit_order in itertools.permutations(vias):
            cnt = cal_diff_paths(G, source, visit_order[0])
            for i in range(1, len(visit_order)):
                cnt *= cal_diff_paths(G, visit_order[i-1], visit_order[i])
            cnt *= cal_diff_paths(G, visit_order[-1], sink)
            cnt_path += cnt
        return cnt_path
    
    return -1

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("[ERROR] NO input file!")
        print("[INFO] Usage: python day11.py <input_file>")
        sys.exit(1)
    input_file = sys.argv[1]
    with open(input_file, 'r') as f:
        lines = f.readlines()
    res1 = count_paths(lines, "you", "out")
    res2 = count_paths(lines, "svr", "out", ["dac", "fft"])
    print(res1, res2)