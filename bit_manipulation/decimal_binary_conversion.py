decimal_num = 6
binary_of_decimal = bin(decimal_num).replace('0b', '')
print(f'binary_of_decimal {decimal_num}: {binary_of_decimal}')  # 110

binary_num = '1000'
decimal_of_binary = int(binary_num, 2)
print(f'decimal_of_binary {binary_num}: {decimal_of_binary}')  # 8

octal_num = '13'
decimal_of_octal = int(octal_num, 8)
print(f'decimal_of_octal {octal_num}: {decimal_of_octal}')
