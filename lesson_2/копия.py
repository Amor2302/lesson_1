l_t = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

i = 0

for i in l_t:
    if i.isdigit():
        l_t.extend(['"', f'{i.zfill(2)}', '"'])
    elif i.startswith('+'):
        l_t.extend(['"', f'{i.zfill(3)}', '"'])

    else:
        l_t.append(i)

    print(l_t)

# while n < len(l_t):
#     if l_t[i].isdigit():
#         l_t[i] = l_t[i].zfill(2)
#     elif l_t[i].startswith('+'):
#         l_t[i] = l_t[i].zfill(3)
#     i += 1
# n = 1
# while n < len(l_t):
#     if l_t[n].isdigit():
#         l_t.insert(n, '"')
#         l_t.insert(n + 2, '"')
#     n +=2
#
# print(l_t)