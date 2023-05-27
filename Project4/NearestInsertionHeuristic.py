#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import sys
import numpy as np
from typing import List, Tuple
import pandas as pd
import csv
import os

def nearest_insertion(distances):
    n = len(distances)
    unvisited = set(range(1, n))
    current = 0
    path = [0]
    while unvisited:
        shortest_dist = sys.maxsize
        for i in unvisited:
            if distances[current][i] < shortest_dist:
                nearest_node = i
                shortest_dist = distances[current][i]
        best_insertion = None
        best_increase = sys.maxsize
        for i in range(len(path)):
            start = path[i]
            end = path[(i + 1) % len(path)]
            increase = distances[start][nearest_node] + distances[nearest_node][end] - distances[start][end]
            if increase < best_increase:
                best_insertion = i
                best_increase = increase
        path.insert(best_insertion + 1, nearest_node)
        unvisited.remove(nearest_node)
        current = nearest_node
    return path

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
#         file = "/Users/rishusingh/Dropbox/Mac/Documents/Upitt/5th Sem/Project4/Project4-Input-Files/Book1.csv"
        adj, n = get_adjacency_matrix(file)
#         print(adj)
        path = nearest_insertion(adj)
        distance = sum(adj[path[i-1]][path[i]] for i in range(len(path)))
        path.append(path[0])
        print("For File", n, "n: ")
        print("Path:", path)
        print("Distance:", distance, "\n")

