#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import sys
from typing import List, Tuple
import pandas as pd
import csv
import os

def tsp(distances: List[List[int]]) -> Tuple[int, List[int]]:
    n = len(distances)
    memo = {}

    def solve(current: int, visited: int) -> Tuple[int, List[int]]:
        if visited == (1 << n) - 1:
            return (distances[current][0], [0])

        if (current, visited) in memo:
            return memo[(current, visited)]

        min_dist = sys.maxsize
        min_path = []

        for next_city in range(n):
            if visited & (1 << next_city) == 0:
                new_visited = visited | (1 << next_city)
                dist, path = solve(next_city, new_visited)
                total_dist = distances[current][next_city] + dist
#                 print(distances[current][next_city])
                if total_dist < min_dist:
                    min_dist = total_dist
                    min_path = path + [next_city]  
#         min_path.append(current)
        memo[(current, visited)] = (min_dist, min_path)
        return (min_dist, min_path)

    return solve(0, 1)

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

        min_dist, min_path = tsp(adj)
        min_path.append(min_path[0])
        print("For File", n, "n: ")
        print("Minimum distance:", min_dist)
        print("Path:", min_path,"\n")

