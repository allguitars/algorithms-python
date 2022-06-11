'''
List 有個 pop() function 取得最後面的元素
註: pop(index)可取得特定位置元素

在 coding interview 時，要想到堆疊中的元素可以不只單純放一個數值。
而是可以放一個 list... 每一個 list 中存放相關的數值
例如在堆疊某一層，放置某節點的數值，以及其深度 -> [node, 2]
'''

# 如果想要堆疊中每個元素不只儲存一個值，可以用二維陣列。
stack = []

stack.append(['a', 1])
stack.append(['b', 2])
stack.append(['c', 3])

print(stack)

# Python 有個很好用的寫法是可以在等號左邊直接解構陣列

c, n = stack.pop()
print(c, n)        # c, 3

print(stack)       # 剩兩個元素

# 測試是否可以解構三個以上元素

stack.append(['hell', 'world', 2022])
print(stack)

c1, c2, year = stack.pop()
print(c1, c2, year)           # 可以 -> hello world 2022

print(stack)
