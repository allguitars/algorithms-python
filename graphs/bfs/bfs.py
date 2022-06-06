'''
2.1 BFS: Breadth First Search Implementation in Python | Graph Data Structure
https://youtu.be/PQhMkmhYZjQ
- PyTech Vision
'''

adj_list = {
    'A': ['B', 'D'],
    'B': ['A', 'C'],
    'C': ['B'],
    'D': ['A', 'E', 'F'],
    'E': ['D', 'F', 'G'],
    'F': ['D', 'E', 'H'],
    'G': ['E', 'H'],
    'H': ['G', 'F']
}
