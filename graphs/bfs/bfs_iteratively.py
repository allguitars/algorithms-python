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
5. 針對佇列最前面的元素開始"處理"，取出才處理(印出)。
6. 處理過後，就要標記為看過。
7. 查看該節點的"所有相鄰節點"，如果沒有被看到過，才放到佇列中
8. 繼續取佇列最前端的元素，直到佇列為空。

注意：有兩個地方需要判斷是否看過，感覺重複了。不是寫得很漂亮，但這個版本比較容易理解。
'''

# OUTPUT: A B C D E F
# graph = {
#     'A': ['B', 'C'],
#     'B': ['A', 'C', 'D'],
#     'C': ['A', 'B', 'D', 'E'],
#     'D': ['B', 'C', 'E', 'F'],
#     'E': ['C', 'D'],
#     'F': ['D']
# }

# another graph example from: https://youtu.be/pcKY4hjDrxk  (Abdul Bari)
# OUTPUT: 1 4 2 3 5 8 7 10 9 6
graph = {
    1: [4, 2],
    2: [5, 8, 7],
    3: [4, 2, 10, 9],
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

    # 佇列有了第一個元素，可以開始對佇列操作。
    # 取得在佇列最前面的節點並處理(印出)
    while queue:
        vertex = queue.pop(0)      # 跟 DFS 版本唯一的差別在這裡，取最先進來的元素。

        # process if not seen
        if vertex not in seen:
            print(vertex)        # process
            seen.add(vertex)     # 被處理過就算是被看過

        # After processing the vertex, exlpore all its adjanct nodes
        adj_vetexes = graph[vertex]
        for v in adj_vetexes:
            if v not in seen:     # 沒有看過的相鄰節點，才需要放到佇列中。
                queue.append(v)


# bfs('A')   # exmaple 1
bfs(1)       # example 2
