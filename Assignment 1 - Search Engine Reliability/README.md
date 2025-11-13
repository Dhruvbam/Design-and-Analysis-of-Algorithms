# Project 1: Search Engine Analysis
![Image](https://github.com/Dhruvbam/Design-and-Analysis-of-Algorithms/blob/main/Assignment%201%20-%20Search%20Engine%20Reliability/img.png)

Search Engine Analyzer is a Python based project developed for the Design and Analysis of Algorithms course, focused on rigorously benchmarking the accuracy and consistency of web page rankings from three different search engines. By analyzing 10,000 web pages sourced from five datasets, this tool leverages Merge Sort, Quick Sort, and Insertion Sort to quantify ranking integrity through inversion counting, a robust metric for measuring ranking consistency. The analyzer identifies the most reliable search engine, presents comparative metrics, that highlights large scale data processing, and practical benchmarking while demonstrating the power of algorithm driven assessments to solve real world data engineering challenges.

## Features & Technical Details

- **Algorithmic Inversion Counting:** Benchmarks ranking lists using Merge Sort (\(O(n \log n)\)), Quick Sort, and Insertion Sort (\(O(n^2)\)) adapted for inversion-count analysis.
- **Large Data Handling:** Processes and validates rankings for 10,000 web pages across five source files.
- **Quantitative Evaluation:** Identifies the most reliable search engine by comparing inversion counts—lower values indicate greater ranking consistency.
- **Automated Data Rearrangement:** Rearranges source ranking data to match consolidated combined rankings for precise comparative analysis.
- **Performance Insights:** Experimental validation shows Search Engine 1 to be the most consistent, with Merge Sort as the most efficient.
- **Modular Design:** Clearly structured Python classes for extensible sorting, inversion computation, and result reporting.

## Built With
This project is implemented using:
- <a href="https://www.python.org/" target="_blank" rel="noreferrer"><img src="https://img.shields.io/badge/Python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54" width="36" height="36" alt="Python" /></a> **Python**: The primary programming language for implementing the sorting algorithms and handling data.


## Installation
To run this project locally:
1. Clone the repository:
    ```bash
    git clone https://github.com/your-repo/evaluating-search-engines.git
    ```
2. Ensure you have Python installed.
3. Run the program by executing:
    ```bash
    python Source_code.py
    ```
### Files in This Project
- **Source_code.py**: Contains the implementation of Merge Sort, Quick Sort, and Insertion Sort, as well as the functions to calculate and rearrange the rankings.
- **source1.txt, source2.txt, etc.**: Text files containing web page rankings from different search engines.

