'''
[Python] BFS和DFS算法(第2讲)
https://youtu.be/bD8RT0ub--0
- 黄浩杰
'''

from concurrent.futures import process
from readline import add_history


# graph = {
#     'A': ['B', 'C'],
#     'B': ['A', 'C', 'D'],
#     'C': ['A', 'B', 'D', 'E'],
#     'D': ['B', 'C', 'E', 'F'],
#     'E': ['C', 'D'],
#     'F': ['D']
# }

# another graph example from: https://youtu.be/pcKY4hjDrxk
# Abdul Bari
graph = {
    1: [4, 2],
    2: [5, 8, 7],
    3: [10, 9],
    4: [1, 3],
    5: [2, 6, 7, 8],
    6: [5],
    7: [2, 5, 8],
    8: [2, 5, 7],
    9: [3],
    10: [3]
}


def bfs(graph, starting_vertex):
    queue = []
    seen = set()

    # 起始動作，先把一個節點放到佇列，這樣後面的 while loop for repeating steps 才會開始。
    queue.append(starting_vertex)

    # 有被放到 queue 中的動作，等於是已經被看到過。
    seen.add(starting_vertex)

    # 佇列有了第一個元素，可以開始對佇列操作。
    # 取得在佇列最前面的節點並處理(印出)
    while queue:
        vertex = queue.pop(0)

        # process
        print(vertex)

        # After processing the vertex, exlpore all its adjanct nodes
        adj_vetexes = graph[vertex]

        for v in adj_vetexes:
            if v not in seen:     # 沒有看過的相鄰節點，才需要放到佇列中。
                queue.append(v)
                seen.add(v)       # 只要是放到佇列中，就表示被看過。


# bfs(graph, 'A')
bfs(graph, 1)
