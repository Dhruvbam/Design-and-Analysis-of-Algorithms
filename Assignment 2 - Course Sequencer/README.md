# Project 2: Course Scheduling Using Topological Sorting
![Alt text](https://github.com/Dhruvbam/Design-and-Analysis-of-Algorithms/blob/main/Assignment%202%20-%20Course%20Sequencer/img.png)

## About
This project was developed for the Design and Analysis of Algorithms (CS 3364) class at Texas Tech University. The objective of this project is to implement a topological sorting algorithm using Depth-First Search (DFS) to determine the optimal order for completing courses in a Computer Science undergraduate program. The project tackles the challenge of sequencing courses based on their prerequisites.

## Problem Statement
Given a set of courses with prerequisites, the goal is to determine the correct sequence in which a student should take these courses. The problem is solved using topological sorting, which ensures that a course is only taken after all its prerequisites have been completed.

## Solution
The project implements:
- **Data Parsing**: Extracting course data from the provided `Data.txt` file, which lists each course along with its prerequisites.
- **Graph Creation**: Building an Abstract Data Type (ADT) graph to represent relationships between courses.
- **DFS-Based Topological Sorting**: Using DFS to traverse the graph and assign post-visit numbers to each course.
- **Optimal Course Sequence**: Sorting the courses based on their post-visit numbers to generate the correct sequence.

### Features
- Reads course data and prerequisites from `Data.txt`.
- Constructs a directed graph where nodes represent courses and edges represent prerequisite relationships.
- Uses DFS to determine the optimal course order for completion.
- Outputs the correct sequence of courses, considering all prerequisite constraints.

## Built With
This project is implemented using:
- <a href="https://www.python.org/" target="_blank" rel="noreferrer"><img src="https://img.shields.io/badge/Python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54" width="36" height="36" alt="Python" /></a> **Python**: The main programming language used for the implementation.
- **Graph Data Structures**: Representing courses and their relationships.

## Files in This Project
- **CourseOrder.py**: Contains the implementation of the topological sorting algorithm using DFS.
- **Data.txt**: Contains the list of courses and their prerequisites.

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

## How It Works
1. **Parse Data**: The `Data.txt` file is parsed to extract courses and their respective prerequisites.
2. **Build Graph**: A directed graph is created where courses are nodes and prerequisite relationships are edges.
3. **DFS Algorithm**: The DFS algorithm traverses the graph, assigning pre-visit and post-visit numbers to courses.
4. **Topological Sorting**: Courses are sorted by their post-visit numbers in descending order to generate the correct sequence.


## Conclusion 
The project successfully outputs the correct sequence of courses based on prerequisites using topological sorting. Future improvements could include graphical visualizations of the course sequence or optimizing the algorithm for larger datasets.

