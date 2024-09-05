'''
Texas Tech University
CS 3364: Design and Analysis of Algorithms
Professor: Dr. Victor Sheng
November 1, 2023


Dhruv Maniar R11713343 
Atharva Dalvi R11765481 
Apoorv Rana R1172307 
Alex Murangira R11648884


FILE NAME: CourseOrder.py
PURPOSE: Extracts course data from 'data.txt' and organizes course prerequisites using topological sorting (DFS) for the optimal order a CS student should take the courses.
FOR: CS 3364 Design and Analysis of Algorithms: Project 2
'''

class CourseInfo:  # Represents course details including prerequisites
    def __init__(self, course_code, prereq) -> None:
        self.course_code = course_code
        self.prereq = prereq

class Node:  # Node creation for linked list
    def __init__(self, value) -> None:
        self.value = value
        self.next = None

class CourseGraph:
    def __init__(self, count) -> None:
        self.graph = {}
        self.count = count

    # Define graph connections; if no prerequisites ('N/A'), skip
    def add_connections(self, course_data):
        for i in range(len(course_data.prereq)):
            if course_data.prereq[i] == 'N/A':
                pass
            else:
                node = Node(course_data.course_code)
                node.next = self.graph[course_data.prereq[i]]
                self.graph[course_data.prereq[i]] = node

    # Add labels for each course in the graph
    def add_labels(self, course_data):
        self.graph[str(course_data.course_code)] = None

# Global variable for pre-visit and post-visit numbers during traversal
counter = 0

def explore(graph, v, visited, courses, index_map, pre_visit, post_visit):
    global counter
    counter += 1
    pre_visit[v] = counter
    visited[v] = True
    current = graph.graph[courses[v].course_code]

    while current is not None:
        # Explore if the course is not visited
        if not visited[index_map[current.value]]:
            explore(graph, index_map[current.value], visited, courses, index_map, pre_visit, post_visit)
        current = current.next
    counter += 1
    post_visit[v] = counter

def topological_sort_dfs(graph, courses, index_map, pre_visit, post_visit):
    visited = [False] * graph.count
    for i in range(len(courses)):
        if not visited[i]:
            explore(graph, i, visited, courses, index_map, pre_visit, post_visit)

# Read data from the file 'data.txt'
file_stream = open("Data.txt", "r", newline=None)

# Initialization and parsing data
flag = 0
course_list_1 = []
course_list_2 = []
courses_data = []
index_mapping = {}

# Parse data and store it as CourseInfo objects
while True:
    data = file_stream.readline()
    if not data:
        break
    values = data.strip()
    string1 = ''
    string2 = ''
    course_list_1 = []
    course_list_2 = []
    
    # Extract course name and prerequisites
    for char in values:
        # Extract course and its prerequisites
        if char == '(' and flag == 0:
            flag = 1
            continue
        if flag == 1:
            if char == ')':
                break
            string2 = string2 + char
            continue
        else:
            string1 = string1 + char
            flag = 0
    flag = 0
    string1 = string1[:string1.index('-') - 1]
    
    # Parse and format prerequisites for each course
    course_list_1 = string2.split(' and ')
    for item in course_list_1:
        if ',' in item:
            course_list_2 = item.split(', ')
            course_list_2.append(course_list_1[len(course_list_1) - 1])
            course_list_1 = course_list_2.copy()
            break

    # Store CourseInfo objects and index mapping for course codes
    courses_data.append(CourseInfo(string1, course_list_1))
    index_mapping[string1] = counter
    counter += 1

# Creating the CourseGraph and adding connections and labels
course_graph = CourseGraph(counter)
for i in range(len(courses_data)):
    course_graph.add_labels(courses_data[i])
    course_graph.add_connections(courses_data[i])

# Initialize arrays to store pre-visit and post-visit orders
pre_visit_order = [0] * (course_graph.count)
post_visit_order = [0] * (course_graph.count)

# Perform DFS for topological sorting of courses
topological_sort_dfs(course_graph, courses_data, index_mapping, pre_visit_order, post_visit_order)

# Map the post-visit numbers to course codes
j = 0
for course in index_mapping:
    index_mapping[course] = post_visit_order[j]
    j += 1

# Sort and print the courses based on their post-visit numbers (in descending order)
for course_key in sorted(index_mapping, key=index_mapping.get, reverse=True):
    print(course_key)


'''
The question file has a small error in the input data:
CS 3365 - Software Engineering I (CS 2365, CS2413 and MATH 3342) 
instead of 
CS 3365 - Software Engineering I (CS 2365, CS 2413 and MATH 3342)
We ran the code after adding a space between "CS" and "2413" in our Data.txt
'''