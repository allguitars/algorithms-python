d = {"A": 3, "B": 1, "C": 100}

# find key with lowest value
lowest_key = min(d, key=d.get)

# find key with lowest value
highest_key = max(d, key=d.get)

print(lowest_key)   # B
print(highest_key)  # C
