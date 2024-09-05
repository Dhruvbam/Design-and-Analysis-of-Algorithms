![Alt text](https://github.com/Dhruvbam/Search-Engine_Reliability_Analysis/blob/main/img.png)

# Search Engine Reliability Analysis

## Project Overview
This project, developed for CS 3364: Design and Analysis of Algorithms at Texas Tech University, aims to assess the reliability of search engines by comparing their ranking outcomes for 10,000 web pages. Utilizing Merge Sort, Quick Sort, and Insertion Sort, we analyze the accuracy of search engines by calculating the number of inversions in rankings, providing a data-driven approach to evaluate search engine performance.

## Problem Statement
Determining the most reliable search engine among three contenders by evaluating their ability to accurately rank web pages from five source files. The goal is to use algorithmic evaluations to find which search engine produces the most accurate and reliable rankings.

## Methodology
- **Combined Ranking Calculation**: Rank web pages by summing ranks from all search engines.
- **Sorting Algorithms**: Apply Merge Sort, Quick Sort, and Insertion Sort to calculate inversions in the rankings, with fewer inversions indicating higher reliability.

## Results
Our analysis identified the search engine with the least number of inversions as the most reliable, recommending its use for future web searches based on its accuracy and speed.

## Technologies Used
- Python for implementing sorting algorithms and analysis scripts.

## How to Run
Ensure Python is installed, then execute the main script:
```bash
python Source_code.py
