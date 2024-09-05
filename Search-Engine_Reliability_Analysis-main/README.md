# Project 1: Evaluating Search Engine Reliability through Sorting Algorithms
![Image](https://github.com/Dhruvbam/Search-Engine_Reliability_Analysis/blob/main/img.png)


## About
This project was completed as part of the Design and Analysis of Algorithms (CS 3364)course at Texas Tech University. The project focuses on assessing the reliability of search engines by comparing the rankings of web pages using various sorting algorithms. Three sorting algorithms—Merge Sort, Quick Sort, and Insertion Sort—were employed to calculate the number of inversions between the ranking results from different search engines. The search engine with the fewest inversions is deemed the most reliable.

## Problem Statement
The goal of this project is to determine the most reliable search engine from three options, each providing a ranking for 10,000 web pages. The reliability of each search engine is evaluated based on the number of inversions between its rankings and a combined ranking derived from five source files.

## Solution Overview
The solution involves the following steps:
1. **Combined Ranking**: Calculate a combined rank for each web page by summing the ranks from five source files.
2. **Rearranging Data**: Sort the combined ranks and rearrange the data in the source files accordingly.
3. **Sorting Algorithms**: Apply Merge Sort, Quick Sort, and Insertion Sort to the rearranged data to calculate the number of inversions.
4. **Evaluation**: The search engine with the fewest inversions is determined to be the most reliable.

### Features
- Calculates and compares rankings using three sorting algorithms: Merge Sort, Quick Sort, and Insertion Sort.
- Determines the most reliable search engine based on inversion counts.
- Provides experimental test cases and analysis of the results.

## Built With
This project is implemented using:
- <a href="https://www.python.org/" target="_blank" rel="noreferrer"><img src="https://img.shields.io/badge/Python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54" width="36" height="36" alt="Python" /></a> **Python**: The primary programming language for implementing the sorting algorithms and handling data.

## Files in This Project
- **Source_code.py**: Contains the implementation of Merge Sort, Quick Sort, and Insertion Sort, as well as the functions to calculate and rearrange the rankings.
- **source1.txt, source2.txt, etc.**: Text files containing web page rankings from different search engines.

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

## How It Works
1. **Data Extraction**: The rankings from five source files are extracted and combined to calculate a total ranking for each web page.
2. **Sorting Algorithms**: Merge Sort, Quick Sort, and Insertion Sort are applied to rearrange the web page rankings and calculate inversions.
3. **Reliability Assessment**: The search engine with the fewest inversions is deemed the most reliable.

### Results and Conclusion
After testing with the three sorting algorithms, **Search Engine 1** was found to be the most reliable due to the fewest number of inversions. Among the sorting algorithms, Merge Sort performed best due to its efficiency in handling large data sets.

