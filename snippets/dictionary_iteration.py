'''
Iterating all keys and values in a dictionary
'''

mydict = {
    'A': 10,
    'B': 20,
    'C': 30
}

for key in mydict:    # 不需要用 mydict.keys()
    print(key)

# 如果需要同時操作 key 跟 value，可以用 items()
for key, value in mydict.items():
    print(key, value)
