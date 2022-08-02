def digit_sum(n):
    current = 0
    while n > 0:
        temp = n % 10
        current += temp
        n = n // 10
    return current


num = 123
print(digit_sum(num))  # 1+2+3 = 6
