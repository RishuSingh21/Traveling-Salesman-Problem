#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from typing import List, Tuple
import pandas as pd
import csv
import os

def tsp_nn(distances: List[List[int]]) -> Tuple[int, List[int]]:
    n = len(distances)
    path = [0]
    visited = [False] * n
    visited[0] = True

    # Greedy algorithm: pick the nearest unvisited city
    for i in range(n - 1):
        current_city = path[-1]
        nearest_city = None
        min_distance = float('inf')
        for j in range(n):
            if not visited[j] and distances[current_city][j] < min_distance:
                nearest_city = j
                min_distance = distances[current_city][j]
        path.append(nearest_city)
        visited[nearest_city] = True

    # Complete the cycle by returning to the starting city
    path.append(0)

    # Calculate the total distance of the path
    total_distance = sum(distances[path[i]][path[i+1]] for i in range(n))

    return total_distance, path
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
#     file = "/Users/rishusingh/Dropbox/Mac/Documents/Upitt/5th Sem/Project4/Project4-Input-Files/5n.csv"
        adj, n = get_adjacency_matrix(file)
#         print(adj)

        min_dist, min_path = tsp_nn(adj)
        print("For File", n, "n: ")
        print("Minimum distance:", min_dist)
        print("Path:", min_path,"\n")


