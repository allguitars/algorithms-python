lst = [1, 2, 3, 4, 5]

lst[0] = lst.pop()  # the tailing element will be 'cut' out

print(lst)  # [5, 2, 3, 4]
print(len(lst))  # 4

# 這個語法有個問題
# 如果串列中只有一個元素，執行 pop 之後會變為空串列。
# 這時候 lst[0] 會出現 index out of range 因為已經是空的，連第一個元素都沒有。

#lst = [10]
# lst[0] = lst.pop()  # IndexError: list assignment index out of range
# print(lst)

# 所以只有一個元素的話  就直接 pop out heap 頂端  也就是第一個元素就好
# 如果有兩個以上元素  才用最上面的方式
lst = [100, 200]
lst[0] = lst.pop()
print(lst)  # 200
