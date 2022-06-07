'''
做這個實驗室因為在處理 Dijstra Algorithm 的時候
思考要如何去表達一個圖的 edge cost

或許用 dictionary in dictionary 比較可以解決雙向查詢的問題
'''

# compare tuples

a = (1, 0)
b = (0, 1)
c = (1, 0)

print(a == b)  # False
print(a == c)  # True


# comapre sets

d = {0, 1}
e = {1, 0}
print(d == e)  # True

# a dictionary which has sets as the key
# error: TypeError: unhashable type: 'set'
# edge_cost = {
#     {'A', 'B'}: 10,
#     {'A', 'C'}: 5
# }


# so maybe it's better to use tuples as the key
# but reversed tuples are not treated the same

edge_cost2 = {
    ('A', 'B'): 10,
    ('A', 'C'): 5
}

# print(edge_cost2[('A', 'B')])   # 10, tuples can be the key of a dictionary
# print(edge_cost2[('B', 'A')])   # KeyError: ('B', 'A'), reversed order is not the same


# 或許用 dictionary in dictionary 比較可以解決雙向查詢的問題
# 以下是一個 undirected graph 不論是從 A 查與 B 的距離，或是從 B 查與 A 的距離，都可以查得到。
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

print(graph['A']['B'], graph['B']['A'])  # 6 6
