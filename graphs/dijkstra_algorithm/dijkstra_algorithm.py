'''
https://youtu.be/pVfj6mxhdMw (Computer Science)
'''

import math


def find_shortest_unvisited(unvisited, tracking):
    '''
    From the unvisited list, find the vertext which has the shortest distance so far.
    Since we have set the intial shortest distance as 0 for the starting vertex, and other vertices
    as Infinity, for the first round of the while loop, it will be the starting vertex.
    '''
    shortest_distance = float('inf')
    result = ''

    for v in unvisited:
        dist = tracking[v]['shortest_dist']

        if not math.isinf(dist) and dist < shortest_distance:
            result = v
            shortest_distance = dist

    return result


def find_unvisited_neighbors(v, unvisited, g):
    '''
    From all the nighbors, find the ones that have not been visited.
    '''
    result = []

    for neighbor in g[v].keys():
        if neighbor in unvisited:
            result.append(neighbor)

    return result


def dijkstra(g, start):
    '''
    Create a tracking table which has all shortest distnances from the starting vertex
    '''
    visited = []
    unvisited = list(g.keys())  # initially, all vertices are unvisited

    # ========== Initial steps: 2 steps ==========

    # 1. create the shortest distance tracking table, intial shorest distance for
    # each vertex is infinity
    tracking_table = {}

    for vertex in unvisited:
        tracking_table[vertex] = {
            'shortest_dist': float('inf'),
            'previous_vertex': ''
        }

    # 2. make the shortest distance of starting vertex from itself 0
    tracking_table[start]['shortest_dist'] = 0

    # ========== Repeating steps ==========

    while unvisited:
        current_vertex = find_shortest_unvisited(unvisited, tracking_table)
        unvisited_neighbors = find_unvisited_neighbors(current_vertex, unvisited, graph)

        for neighbor in unvisited_neighbors:
            current_distance = tracking_table[current_vertex]['shortest_dist']
            edge = g[current_vertex][neighbor]

            # do relaxation for the neighbor
            if current_distance + edge < tracking_table[neighbor]['shortest_dist']:
                tracking_table[neighbor]['shortest_dist'] = current_distance + edge

                # if the known distance for the neighbor is updated, then
                # also update the previous vertex
                tracking_table[neighbor]['previous_vertex'] = current_vertex

        # add the current vertex to the visited list and remove it from the unvisited one
        unvisited.remove(current_vertex)
        visited.append(current_vertex)

    print(unvisited)
    print(visited)
    print(tracking_table)


graph = {
    'A': {
        'B': 6,
        'D': 1
    },
    'B': {
        'A': 6,
        'C': 5,
        'D': 2,
        'E': 2
    },
    'C': {
        'B': 5,
        'E': 5
    },
    'D': {
        'A': 1,
        'B': 2,
        'E': 1
    },
    'E': {
        'B': 2,
        'C': 5,
        'D': 1
    }
}

dijkstra(graph, 'A')
