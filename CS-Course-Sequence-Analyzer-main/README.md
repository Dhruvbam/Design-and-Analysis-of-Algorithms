![Alt text](https://github.com/Dhruvbam/CS-Course-Sequence-Analyzer/blob/main/img.png)

# CS Course Sequence Analyzer

## Project Overview
This project, developed for CS 3364: Design and Analysis of Algorithms at Texas Tech University, implements a topological ordering algorithm to determine the optimal sequence for undertaking courses within a Computer Science undergraduate program. It addresses the challenge of course sequencing with prerequisites through a Depth-First Search (DFS) based approach.

## Problem Statement
The goal is to identify the correct sequence of courses for a Computer Science major, considering their prerequisites, using a practical and algorithmic solution.

## Solution
Utilizing an Abstract Data Type (ADT) graph and DFS, the project achieves topological sorting of courses. It focuses on outputting the course sequence sorted by post-visit numbers from DFS traversal, offering a strategic plan for course completion.

## Features
- **Course Data Parsing**: Extraction and organization of course details and their prerequisites.
- **Graph Construction**: Creation of an ADT graph to map courses and prerequisites.
- **DFS-Based Topological Sorting**: Implementation of DFS for topological sorting and sequence determination.

## How to Run
Ensure Python is installed. Run the script with:
```bash
python CourseOrder.py
