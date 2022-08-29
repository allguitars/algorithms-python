lst = [1, 2, 3]


# 直接報錯 IndexError: list index out of range
# 連判斷的機會都沒有
if not lst[3]:
    print('there is no fourth element')
