num = 0
sum_num = 0
sum_end_a = 0
sum_end_b = 0

new_list = []

for num in range(1, 1000, 2):
    new_list.append(num ** 3)

print(new_list)

for a in new_list:
    all_a = a
    while a > 0:
        num = a % 10
        sum_num = sum_num + num
        a = a // 10
    if sum_num % 7 == 0:
        sum_end_a = sum_end_a + all_a
    else:
        sum_num = 0
print(sum_end_a)
for b in new_list:
    b += 17
    all_b = b
    while b > 0:
        num = b % 10
        sum_num = sum_num + num
        b = b // 10
    if sum_num % 7 == 0:
        sum_end_b = sum_end_b + all_b
    else:
        sum_num = 0

print(sum_end_b)





