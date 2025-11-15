# Project 2: Course Sequencer
<p align="center">
<img src="https://github.com/Dhruvbam/Design-and-Analysis-of-Algorithms/blob/main/Assignment%202%20-%20Course%20Sequencer/csm.gif">
</p>

Course Sequencer is a Python based application developed for the Design and Analysis of Algorithms course to efficiently solve course scheduling for computer science undergraduates. By parsing raw curriculum data and modeling courses and prerequisites as nodes and directed edges within a directed acyclic graph (DAG), Course Sequencer employs Depth-First Search (DFS) and topological sorting to generate an optimal order for course completion. This minimizes scheduling conflicts and streamlines academic planning, ensuring all prerequisite constraints are met. The project showcases advanced skills in graph theory, algorithm design, and the practical application of computer science concepts to curriculum planning and real-world problems.


## Features & Technical Details

- **Graph-Based Prerequisite Modeling:** Reads and parses a real course prerequisite dataset and creates a directed graph mapping dependencies between courses.
- **DFS Topological Sort:** Implements a linear-time O(V + E) DFS algorithm to assign pre-visit and post-visit numbers, producing a valid topological ordering.
- **Automated Course Ordering:** Outputs the correct sequence for all courses, such that no course appears before any of its required prerequisites.
- **Error Handling:** Handles data inconsistencies, such as missing or misformatted prerequisites, to ensure robust performance on real-world data.
- **Modular and Readable Implementation:** Well-structured Python code separates data parsing, graph construction, and topological sorting for clarity and extensibility.
- **Scalable for Large Datasets:** Algorithm and data structures are designed to maintain efficiency and correctness, even as the number of courses or dependencies increases.


## Built With
This project is implemented using:
- <a href="https://www.python.org/" target="_blank" rel="noreferrer"><img src="https://img.shields.io/badge/Python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54" width="36" height="36" alt="Python" /></a> **Python**: The main programming language used for the implementation.
- **Graph Data Structures**: Representing courses and their relationships.


## Installation
To run the project locally:
1. Clone the repository:
    ```bash
    git clone https://github.com/your-repo/course-scheduling.git
    ```
2. Ensure you have Python installed on your machine.
3. Run the `CourseOrder.py` file to generate the topological ordering of the courses:
    ```bash
    python CourseOrder.py
    ```
### Files in This Project
- **CourseOrder.py**: Contains the implementation of the topological sorting algorithm using DFS.
- **Data.txt**: Contains the list of courses and their prerequisites.


