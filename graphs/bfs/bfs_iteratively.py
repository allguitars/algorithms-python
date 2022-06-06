'''
[Python] BFS和DFS算法(第2讲)
https://youtu.be/bD8RT0ub--0
- 黄浩杰
'''

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D', 'E'],
    'D': ['B', 'C', 'E', 'F'],
    'E': ['C', 'D'],
    'F': ['D']
}


def bfs(graph, starting_vertex):
    queue = []
    visited = set()

    # 起始動作，先把一個節點放到佇列
    queue.append(starting_vertex)

    # 佇列有了第一個元素，可以開始對佇列操作。
    while queue:
        vertex = queue.pop(0)

        # "not visited" means not processed yet
        if vertex not in visited:

            # mark it as visited
            visited.add(vertex)

            # process it
            print(vertex)

            # explore all adjacent vertexes
            adj_vetexes = graph[vertex]

            # 直接把所有相鄰節點加到 queue
            # queue 中會有重複的節點，但是因為有 visited list 控管，之後遇到相同節點不會重複處理。
            for v in adj_vetexes:
                queue.append(v)


bfs(graph, 'A')
