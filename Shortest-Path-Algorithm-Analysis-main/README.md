# Project 3: Shortest Path Finder Using Dijkstra and Bellman-Ford Algorithms
![alt text](https://github.com/Dhruvbam/Shortest-Path-Finder/blob/main/sp1.png)


## About
This project was developed as part of the Design and Analysis of Algorithms (CS 3364) course at Texas Tech University. The primary objective is to determine the shortest path between various buildings on a university campus using two well-known algorithms: **Dijkstra's Algorithm** and **Bellman-Ford Algorithm**. The project focuses on finding the most efficient route, even when negative edge weights are present.

## Problem Statement
In real-world applications, finding the shortest path between two locations is a common problem. This project aims to apply shortest path algorithms to determine the optimal route between buildings on a university campus. While **Dijkstra's Algorithm** efficiently handles graphs with non-negative weights, **Bellman-Ford Algorithm** is used to address scenarios with negative edge weights.

## Solution Overview
The project implements the following:
- **Graph Representation**: The campus buildings and the distances between them are represented as a graph.
- **Dijkstra's Algorithm**: A greedy algorithm that finds the shortest path from the source to all other nodes in the graph.
- **Bellman-Ford Algorithm**: A dynamic programming algorithm used for graphs with negative edge weights.
  
Both algorithms are tested on the same graph, and their results are compared to ensure accuracy.

### Features
- Finds the shortest path between buildings using both Dijkstra and Bellman-Ford algorithms.
- Handles graphs with positive and negative edge weights.
- Outputs the shortest path and the corresponding distances for each building.

## Built With
This project is implemented using:
- <a href="https://www.python.org/" target="_blank" rel="noreferrer"><img src="https://img.shields.io/badge/Python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54" width="36" height="36" alt="Python" /></a> **Python**: The main programming language used for implementing the algorithms.
- **Graph Data Structures**: Representing buildings and distances between them.

## Files in This Project
- **Shortest_Path_Finder.py**: Contains the implementation of Dijkstra and Bellman-Ford algorithms for shortest path calculation.
- **Campus Map Data**: A dataset that provides the distances between various buildings on the campus.

## Installation
To run this project locally:
1. Clone the repository:
    ```bash
    git clone https://github.com/your-repo/shortest-path-finder.git
    ```
2. Ensure you have Python installed.
3. Run the program by executing:
    ```bash
    python Shortest_Path_Finder.py
    ```

## How It Works
1. **Graph Creation**: The campus buildings and their connections are modeled as a graph.
2. **Bellman-Ford Algorithm**: Applied to handle graphs with potential negative edge weights.
3. **Dijkstra’s Algorithm**: A faster solution for graphs with non-negative weights.
4. **Shortest Path Calculation**: The program outputs the shortest path and distance from the Computer Science building to all other buildings on campus.

### Example Output
The output displays the shortest path between the **Computer Science building** and all other buildings on campus. Both algorithms (Bellman-Ford and Dijkstra) are applied, and their results are printed for comparison.

## Conclusion
The project demonstrates how different algorithms can be applied to real-world problems involving graph traversal and shortest path calculation. By implementing both Dijkstra and Bellman-Ford algorithms, the project highlights the importance of choosing the right algorithm based on the characteristics of the graph (positive or negative edge weights).

