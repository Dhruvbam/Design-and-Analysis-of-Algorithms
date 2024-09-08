'''
CS 3364: Project 3
Authors: Atharva Dalvi, Apoorv Rana, Dhruv Maniar, Alex Murangira
Date   : 11/29/23
Program to find the shortest path to other buildings from the Computer Science building using Bellman-Ford and Dijkstra algorithms.
'''


# Definition of the Building class
class Building:

  def __init__(self, name):
    # Each building has a name and a dictionary of adjacent buildings
    self.name = name
    self.adjacents = {}  # key: adjacent building, value: distance

  # Adds an adjacent building and the distance to it
  def add_adjacent(self, building, distance):
    self.adjacents[building] = distance


# Definition of the Graph class
class Graph:

  def __init__(self):
    # Contains a dictionary of all buildings in the graph
    self.buildings = {}  # key: building name, value: Building object

  # Adds a building to the graph if it's not already present
  def add_building(self, name):
    if name not in self.buildings:
      self.buildings[name] = Building(name)

  # Adds an edge between two buildings
  def add_edge(self, from_name, to_name, distance):
    self.add_building(from_name)
    self.add_building(to_name)
    self.buildings[from_name].add_adjacent(self.buildings[to_name], distance)

  # Retrieves a building object by its name
  def get_building(self, name):
    return self.buildings.get(name, None)


# Parses data lines to create graph edges
def extract_data(graph, data_lines):
  for line in data_lines:
    parts = line.split(" - ")
    from_building = parts[0]
    for i in range(1, len(parts)):
      to_building, distance = parts[i].rsplit(' ', 1)
      graph.add_edge(from_building, to_building, int(distance))


# Implementation of the Bellman-Ford algorithm
def bellman_ford(graph, start_name):
  # Initialize distances and predecessors
  distances = {building: float('inf') for building in graph.buildings}
  predecessors = {building: None for building in graph.buildings}
  distances[start_name] = 0

  # Relax edges repeatedly
  for _ in range(len(graph.buildings) - 1):
    for building in graph.buildings.values():
      for adjacent, distance in building.adjacents.items():
        if distances[adjacent.name] > distances[building.name] + distance:
          distances[adjacent.name] = distances[building.name] + distance
          predecessors[adjacent.name] = building.name

  return distances, predecessors


# Implementation of Dijkstra's algorithm
def dijkstra(graph, start_name):
  # Initialize distances and predecessors
  distances = {building: float('inf') for building in graph.buildings}
  predecessors = {building: None for building in graph.buildings}
  distances[start_name] = 0
  unvisited = set(graph.buildings.keys())

  # Explore the graph
  while unvisited:
    current = min(unvisited, key=lambda building: distances[building])
    unvisited.remove(current)

    for adjacent, distance in graph.buildings[current].adjacents.items():
      alt_route = distances[current] + distance
      if alt_route < distances[adjacent.name]:
        distances[adjacent.name] = alt_route
        predecessors[adjacent.name] = current

  return distances, predecessors


# Print the shortest paths from the start building to all others
def print_paths(distances, predecessors, start_name):
  for building in distances:
    if building == start_name:
      continue
    print(f"Shortest path from {start_name} to {building}:")
    path = []
    current = building
    while current:
      path.append(current)
      current = predecessors[current]
    print(" -> ".join(reversed(path)), f"Distance: {distances[building]}")
    print()


# Data lines representing the graph
data_lines = [
    'College Square - Prince Center 300 - Lewis Science Center 200',
    'Prince Center - College Square 300 - Police Dept 100 - Torreyson Library 30 - Computer Science 80',
    'Police Dept - Prince Center 100 - Student Health Center 100 - Old Main 200 - Fine Art 50',
    'Student Health Center - Police Dept 100 - Student Center 50 - Brewer-Hegema 200',
    'Lewis Science Center - College Square 200 - Computer Science 150 - Speech Language Hearing 250',
    'Computer Science - Lewis Science Center 150 - Prince Center 80 - Torreyson Library 40 - Burdick 30',
    'Torreyson Library - Computer Science 40 - Prince Center 30 - Old Main 30 - Burdick 80',
    'Old Main - Torreyson Library 30 - Police Dept 200 - Fine Art 90 - McAlister Hall 100',
    'Fine Art - Old Main 90 - Police Dept 50 - Student Center 80 - McAlister Hall 100',
    'Student Center - Fine Art 80 - Student Health Center 50 - New Business Building 110 - Wingo 100 - McAlister Hall 100',
    'Burdick - Speech Language Hearing 100 - Computer Science 30 - Torreyson Library 80 - McAlister Hall 200 - Maintenance College 300',
    'McAlister Hall - Burdick 200 - Old Main 100 - Fine Art 180 - Student Center 100 - Wingo 50 - Maintenance College 150',
    'Wingo - McAlister Hall 50 - Student Center 100 - New Business Building 50 - Maintenance College 100',
    'New Business Building - Wingo 50 - Student Center 110 - Brewer-Hegema 20 - Maintenance College 150 - Oak Tree Apt 30',
    'Brewer-Hegema - New Business Building 20 - Student Health Center 200 - Bear Village Apt 350 - Oak Tree Apt 40',
    'Bear Village Apt - Brewer-Hegema 350',
    'Speech Language Hearing - Lewis Science Center 250 - Burdick 100 - Maintenance College 120',
    'Maintenance College - Speech Language Hearing 120 - Burdick 300 - McAlister Hall 150 - Wingo 100 - New Business Building 150 - Oak Tree Apt 160',
    'Oak Tree Apt - Maintenance College 160 - Brewer-Hegema 40 - New Business Building 30'
]

# Creating the graph and extracting data
graph = Graph()
extract_data(graph, data_lines)

# Running Bellman-Ford and Dijkstra algorithms from the Computer Science building
distances_bf, predecessors_bf = bellman_ford(graph, 'Computer Science')
distances_dj, predecessors_dj = dijkstra(graph, 'Computer Science')

# Printing the results of both algorithms
print("Bellman-Ford Algorithm Results:")
print_paths(distances_bf, predecessors_bf, 'Computer Science')
print("Dijkstra Algorithm Results:")
print_paths(distances_dj, predecessors_dj, 'Computer Science')
