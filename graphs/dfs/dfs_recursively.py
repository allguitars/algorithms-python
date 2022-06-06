
# if we use recursion, then we do not need to explicitly use a stack because
# recursive call automatically maintains a runtime stack

# graph 的長相是依照 https://youtu.be/-LfSbp_6r7c
# 其解釋很好地方在於，把 runtime stack 跟 pending adjacent nodes 結合說明
# 這樣可以看到遞迴呼叫在回溯的時候應該處理哪些節點

node_names = {
    0: 'A',
    1: 'B',
    2: 'C',
    3: 'D',
    4: 'E',
    5: 'F',
    6: 'G',
    7: 'H'
}

# 用 2D array 表示 grap:

#   A B C D E F G H
# A 0 1 0 0 1 0 0 0
# B 1 0 1 1 0 0 0 0
# C 0 1 0 0 0 0 1 0
# D 0 1 0 0 0 1 0 0
# E 1 0 0 0 0 0 0 1
# F 0 0 0 1 0 0 1 0
# G 0 0 1 0 0 1 0 0
# H 0 0 0 0 1 0 0 0

# 也可用 list of list 表示 graph： https://www.geeksforgeeks.org/graph-and-its-representations/
# 在 python 裏面，list 的每個元素可以長得不一樣，用這個表示法會比較具有彈性。

# outer list 的第一個元素代表第一個節點 A，他的相鄰節點有 B, E
# [B, E]
# 第二的節點 B 的相鄰節點有 A,C,D -> [A, C, D]
# 以此類推，整個 list of list 如下：

graph = [
    ['B', 'E'],             # A
    ['A', 'C', 'D'],        # B
    ['B', 'G'],             # C
    ['B', 'F'],             # D
    ['A', 'H'],             # E
    ['D', 'G'],             # F
    ['C', 'F'],             # G
    ['E']                   # H
]

# 但是外圍 list 很難表示節點名稱，例如 index 0 代表節點 A 還有多一個轉換。
# 因此我嘗試用 dictionary 來表示圖

adj_list = {
    'A': ['B', 'E'],
    'B': ['A', 'C', 'D'],
    'C': ['B', 'G'],
    'D': ['B', 'F'],
    'E': ['A', 'H'],
    'F': ['D', 'G'],
    'G': ['C', 'F'],
    'H': ['E']
}

# 用一個 set 來保存已經拜訪過的節點
visited = set()


def dfs(u):
    # set it as visited / seen
    visited.add(u)

    # process the node
    print(u)

    for v in adj_list[u]:
        if v not in visited:
            dfs(v)


# starting from A
dfs('A')
