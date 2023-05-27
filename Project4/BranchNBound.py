#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import pandas as pd
import csv
import os

def tsp_bb(distances):
    n = len(distances)
    all_nodes = set(range(n))
    best_path = None
    best_cost = float('inf')

    def tsp_bb_helper(visited, unvisited, curr_cost):
        nonlocal best_path, best_cost
        
        if len(visited) == n:
            curr_cost += distances[visited[-1]][visited[0]]
            if curr_cost < best_cost:
                best_path = visited
                best_cost = curr_cost
        else:
            for node in unvisited:
                if curr_cost + min(distances[node][j] for j in unvisited) < best_cost:
                    tsp_bb_helper(visited + [node], unvisited - {node}, curr_cost + distances[visited[-1]][node])

    tsp_bb_helper([0], all_nodes - {0}, 0)

    return best_cost, best_path




def get_adjacency_matrix(path):
    df = pd.read_csv(path, header = None, encoding='latin1')
    n = len(df)
    adj = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(i+1,n):
            adj[i][j] = df[i][j]
            adj[j][i] = df[j][i]
    return adj, n
if __name__ == '__main__':
    
    files = os.scandir("/Users/rishusingh/Dropbox/Mac/Documents/Upitt/5th Sem/Project4/Project4-Input-Files/")
    
    for file in files:
#     file = "/Users/rishusingh/Dropbox/Mac/Documents/Upitt/5th Sem/Project4/Project4-Input-Files/4n.csv"
        adj, n = get_adjacency_matrix(file)
#         print(adj)
        min_dist, min_path = tsp_bb(adj)
        print("For File", n, "n: ")
        print("Minimum distance:", min_dist)
        print("Path:", min_path, "\n")

