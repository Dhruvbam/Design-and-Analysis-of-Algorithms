# Project 3: Shortest Path Finder 
![alt text](https://github.com/Dhruvbam/Design-and-Analysis-of-Algorithms/blob/main/Assignment%203%20-%20Shortest%20Path%20Finder/sp1.png)

Shortest Path Finder is a Python-powered solution developed for the Design and Analysis of Algorithms course to compute optimal routes between campus buildings. As project lead, I architected a dynamic system leveraging both Dijkstra’s (for non-negative weights) and Bellman-Ford (for negative weights) algorithms to cover all pathfinding scenarios, including shortcuts and delays. This tool models the campus map as a weighted graph, letting users specify building pairs for real-time calculations. Robustly detecting negative cycles and scalable to new map layouts, this project showcases advanced skills in graph algorithms, algorithm selection, and team leadership in complex, real-world applications.

## Features & Technical Details

- **Dual Algorithm Engine:** Implements Dijkstra’s O(E + V log V) for fast shortest path computation with non-negative weights and Bellman-Ford O(VE) for graphs with negative edge weights.
- **Graph Modeling:** Represents buildings as nodes and routes as weighted edges, adapting dynamically to data changes.
- **Cycle Detection:** Bellman-Ford implementation includes negative cycle detection to ensure path validity.
- **Extensible Architecture:** Easily adapts to new maps or data modifications without core algorithm changes.
- **Comprehensive Output:** Outputs both route and total distance for all pairs using both algorithms for validation.
- **Error Handling:** Handles disconnected nodes and improper data gracefully, ensuring real-world usability.
- **Team Leadership:** Project was directed from conception to implementation, with clear delegation and documentation.


## Built With
This project is implemented using:
- <a href="https://www.python.org/" target="_blank" rel="noreferrer"><img src="https://img.shields.io/badge/Python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54" width="36" height="36" alt="Python" /></a> **Python**: The main programming language used for implementing the algorithms.
- **Graph Data Structures**: Representing buildings and distances between them.



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
### Files in This Project
- **Shortest_Path_Finder.py**: Contains the implementation of Dijkstra and Bellman-Ford algorithms for shortest path calculation.
- **Campus Map Data**: A dataset that provides the distances between various buildings on the campus.

