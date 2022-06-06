'''
黄浩杰 - [Python] BFS和DFS算法(第2讲)
https://youtu.be/bD8RT0ub--0


Abdul Bari - 5.1 Graph Traversals - BFS & DFS -Breadth First Search and Depth First Search
https://youtu.be/pcKY4hjDrxk

Back To Back SWE - Depth First & Breadth First Graph Search - DFS & BFS Graph Searching Algorithms
https://youtu.be/TIbUeeksXcI

思考方向：
1. 需要額外的 queue 跟 seen
2. 只要是被放到佇列中的，表示已經被看到過，之後再遇到的時候就不需要再放到佇列了。
3. 起手式 - 先將第一個節點放到佇列中，這樣後面以佇列為空作為停止條件的迴圈才有辦法進入執行。
4. 當然這第一個節點也算是被看過
5. 針對佇列最前面的元素開始"處理"，取出才處理(印出)
6. 處理之後，查看該節點的"所有相鄰節點"，如果沒有被看到過，才放到佇列中
7. 記得一放到佇列中就要標示為看過
'''

# graph = {
#     'A': ['B', 'C'],
#     'B': ['A', 'C', 'D'],
#     'C': ['A', 'B', 'D', 'E'],
#     'D': ['B', 'C', 'E', 'F'],
#     'E': ['C', 'D'],
#     'F': ['D']
# }

# another graph example from: https://youtu.be/pcKY4hjDrxk  (Abdul Bari)
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


def bfs(starting_vertex):
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


# bfs('A')   # exmaple 1
bfs(1)       # example 2
