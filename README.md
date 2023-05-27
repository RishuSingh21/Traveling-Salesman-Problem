Traveling Salesman Problem Algorithms
This project aims to implement different algorithms for solving the Traveling Salesman Problem (TSP) and analyze their time complexity and performance. The TSP involves finding the shortest path that visits all given cities and returns to the starting city.

Objectives
The objectives of this project are as follows:

Theoretical Time Complexity Analysis: Analyze the theoretical time complexity of the 'Nearest Neighbor Heuristic' and 'Nearest Insertion Heuristic' algorithms.
Shortest Path Determination: Determine the shortest path with the minimum path weight for different degrees of weighted graphs using various TSP algorithms, including Nearest Neighbor, Nearest Insertion, Dynamic Programming, and Branch & Bound.
Number of Solutions: Find the number of solutions for different degrees of weighted graphs.
Algorithms Used
The following algorithms are implemented and evaluated in this project:

Nearest Neighbor Algorithm
The Nearest Neighbor algorithm starts with an arbitrary vertex and follows the edge with the least weight to the nearest unvisited vertex. It uses a greedy approach to construct the TSP path.

Nearest Insertion Algorithm
The Nearest Insertion algorithm starts with two cities and repeatedly finds the city not already in the path that is closest to any city in the current path. It adds the selected city to the path at the best position to minimize the total path weight.

Dynamic Programming Algorithm
The Dynamic Programming algorithm solves the TSP by breaking it down into simpler sub-problems and then optimizing the solution. It efficiently computes the shortest path using a bottom-up approach and memoization.

Branch & Bound Algorithm
The Branch & Bound algorithm helps find a better solution, if not the best solution, for optimization problems. It breaks down the problem into smaller sub-problems and uses a bounding function to eliminate sub-problems that cannot contain the optimal solution.

Analysis
The analysis of the algorithms used in this project yields the following observations:

Nearest Neighbor Heuristic: The Nearest Neighbor algorithm has a time complexity of O(n^2) for n nodes in a graph. This is because, for each node, all nodes are visited once to find the nearest unvisited node.
Nearest Insertion Heuristic: The Nearest Insertion algorithm has a time complexity of O(n^3) for n nodes in a graph. This is because, for each node, it adds n-1 nodes. For each added node, the algorithm considers all possible insertions, which takes O(n^2) time.
Usage
Clone the repository to your local machine.
Open the project in your preferred programming environment.
Ensure that the required dependencies are installed.
Run the main script to analyze and compare the TSP algorithms, measure their performance, and determine the shortest paths.
Please refer to the project code and documentation for detailed information on the implementation and usage.
