'''
* 隨著相鄰節點選擇的不同  traversal的結果也會不同

這裡的 iterative 方式是依照 Back To Back SWE 的演算法
https://youtu.be/TIbUeeksXcI

但我驚訝地發現 iterative 跟 recursive 的結果竟然不一樣
用 BrainWave 的例子去執行這裡的 iterative code
跟他影片中 (recursive) 執行結果不一樣
但是用遞迴的方式跑就結果就會跟他的影片一樣 -> 參照 dfs_recursive.py

仔細推演之後找到原因
不管是透過迴圈還是遞迴，都有可能走出不一樣的路徑。
關鍵是在有多個相鄰節點時，選擇不同的節點當作下一步，都會長出不一樣的 traversal 結果。
'''

# example from https://youtu.be/bD8RT0ub--0 (黄浩杰)
# OUTPUT: A C E D F B
# 執行結果與他的相同
# graph = {
#     'A': ['B', 'C'],
#     'B': ['A', 'C', 'D'],
#     'C': ['A', 'B', 'D', 'E'],
#     'D': ['B', 'C', 'E', 'F'],
#     'E': ['C', 'D'],
#     'F': ['D']
# }

# example graph from https://youtu.be/-LfSbp_6r7c (BrainWave)
# 影片中使用遞迴的結果是 A B C G F D E H
# 但是用這裡的 iterative 方法則變成 A E H B D F G C
graph = {
    'A': ['B', 'E'],
    'B': ['A', 'C', 'D'],
    'C': ['B', 'G'],
    'D': ['B', 'F'],
    'E': ['A', 'H'],
    'F': ['D', 'G'],
    'G': ['C', 'F'],
    'H': ['E']
}

# graph example from: https://youtu.be/pcKY4hjDrxk  (Abdul Bari)
# graph = {
#     1: [4, 2],
#     2: [8, 5, 7, 1, 3],
#     3: [4, 10, 9, 2],
#     4: [1, 3],
#     5: [2, 6, 7, 8],
#     6: [5],
#     7: [2, 5, 8],
#     8: [7, 5, 2],
#     9: [3],
#     10: [3]
# }


def bfs(starting_vertex):
    '''
    BFS版本跟DFS版本差別只在於 pop() 與 pop(0)
    '''
    stack = []
    seen = set()

    stack.append(starting_vertex)

    while stack:
        # pop the last element
        vertex = stack.pop()      # 跟 BFS 的唯一差別，這裡是取最後進來的元素。因為是堆疊。

        # process if not seen
        if vertex not in seen:
            print(vertex)      # process it
            seen.add(vertex)   # add to seen

        # exlpore all its adjanct nodes
        adj_vetexes = graph[vertex]
        for v in adj_vetexes:
            if v not in seen:
                stack.append(v)


# bfs(1)
bfs('A')
