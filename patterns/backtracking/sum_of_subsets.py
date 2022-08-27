'''
Abdul: https://youtu.be/kyLxTdsT8ws

#Backtracking
#Note(Notability)
'''


def sum_of_subsets(arr, m):
    res = []
    curr = []

    def dfs(i, total, rest):
        if total == m:
            res.append(curr.copy())
            return
        if total > m or (total + rest) < m:  # 如果已經爆了或是剩下的總和加上去也無法達到目標總和 m
            return

        # 取當前的數字，放入 curr 陣列
        # 剩下的總和 rest 也必須扣掉
        temp = arr[i]
        curr.append(temp)
        total += temp
        rest -= temp
        dfs(i+1, total, rest)

        # 不取當前數字，但仍要從 rest 中扣除，因為我們已經跳過這個數字。
        # rest 在上面已經扣除 temp 故保持不變，但是 total 要還原回沒有加數字的狀態。
        curr.pop()
        total -= temp
        dfs(i+1, total, rest)

    total = 0
    rest = sum(arr)
    dfs(0, total, rest)
    return(res)


# print(sum_of_subsets([5, 10, 12, 13, 15, 18], 30))
assert sum_of_subsets([5, 10, 12, 13, 15, 18], 30) == [[5, 10, 15], [5, 12, 13], [12, 18]]
